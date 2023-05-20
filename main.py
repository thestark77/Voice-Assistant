import signal
import os
import sys
import re
import time
import random
import keyboard
import openai
import asyncio
import boto3
import pydub
import pyaudio
from deep_translator import GoogleTranslator as Translator
from pydub import playback
import speech_recognition as sr
from EdgeGPT import Chatbot, ConversationStyle
from Bard import Chatbot as BardBot
from dotenv import load_dotenv
from settings.config import BING_WAKE_WORDS, GPT_WAKE_WORDS, EXIT_WORDS, FINISH_CHAT_PHRASES, RESET_WORDS, DID_NOT_UNDERSTAND_PHRASES, CONTINUE_CHAT_PHRASES, INITIAL_CONTEXT, ACTIVATION_PHRASES, TEXT_MARKUP, ASSISTANT_TEXT_COLOR, USER_TEXT_COLOR, SYSTEM_TEXT_COLOR, SPEECH_SPEED, PUSH_TO_TALK_KEY, RECORD_INTERVAL, AUDIO_CAPTURE_MODE, BARD_WAKE_WORDS, FUNCTION_YOUTUBE, FUNCTION_SPOTIFY, FUNCTION_WIKIPEDIA, FUNCTION_WOLFRAM, FUNCTION_WEB, BING_ASSISTANT_NAME, GPT_ASSISTANT_NAME, BARD_ASSISTANT_NAME, FUNCTION_EXIT, FUNCTION_RESET, FUNCTION_ASSISTANT, BARD_CONTEXT, NOT_WAKE_WORD_PHRASES, WELCOME_PHRASES


def handle_keyboard_interrupt(signal, frame):
    # Acciones a realizar al recibir una interrupción de teclado
    print("Programa detenido por el usuario")
    sys.exit(0)  # Finaliza el programa sin mostrar el traceback


# Configurar el manejador de la señal de interrupción de teclado
signal.signal(signal.SIGINT, handle_keyboard_interrupt)

# Carga las variables de entorno
load_dotenv()

GPT_API_KEY = os.environ['GPT_API_KEY']
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
BARD_TOKEN = os.environ['BARD_TOKEN']
# Initialize the OpenAI API
openai.api_key = GPT_API_KEY

# Initialize the AWS BOTO3 API
session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)


def translate_text(text, es_to_en=True):
    try:
        if es_to_en:
            translated_text = Translator(
                source='es', target='en').translate(text=text)
        else:
            translated_text = Translator(
                source='en', target='es').translate(text=text)
    except Exception as e:
        print_system_output(
            "Error al conectar con el traductor de Google: ", e)
        print_and_play("Error al conectar con el traductor de Google")
        return False

    return translated_text


def print_system_output(message, element=None):
    if element is not None:
        print(f"{SYSTEM_TEXT_COLOR}{message}{element}{TEXT_MARKUP}")
    else:
        print(f"{SYSTEM_TEXT_COLOR}{message}{TEXT_MARKUP}")


def any_word_of_list_in_phrase(list, phrase):
    for word in list:
        if word in phrase:
            return True

    return False


def get_random_phrase(list):
    random_phrase = random.choice(list)

    return random_phrase


def synthesize_speech(text, output_filename):
    ssml_text = f"<speak><prosody rate='{SPEECH_SPEED}%'>{text}</prosody></speak>"
    try:
        polly = session.client('polly', region_name='us-east-1')
        response = polly.synthesize_speech(
            TextType='ssml',
            Text=ssml_text,
            OutputFormat='mp3',
            VoiceId='Lupe',
            Engine='neural'
        )
    except Exception as e:
        print_system_output("Error sintetizando voz synthesize_speech: ", e)
        print_and_play("Error sintetizando voz")
    with open(output_filename, 'wb') as f:
        f.write(response['AudioStream'].read())


def play_audio(file):
    sound = pydub.AudioSegment.from_file(file, format="mp3")
    playback.play(sound)


def create_audio_folder():
    # Obtener el directorio actual
    current_path = os.getcwd()

    # Obtiene la ruta de la carpeta
    audio_folder = os.path.join(current_path, 'audio')

    # Comprobar si la carpeta 'audio' existe
    if not os.path.exists(audio_folder):
        # Crea la carpeta 'audio'
        os.mkdir(audio_folder)


def print_and_play(message):
    if message is not None and message.strip() != '':
        print(f"{ASSISTANT_TEXT_COLOR}Asistente: {message}{TEXT_MARKUP}")
        synthesize_speech(message, 'audio/response.mp3')
        play_audio('audio/response.mp3')


def ptt_audio_to_text(awake=True):
    phrase = ''
    recognizer = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            # Inicializar audio vacío
            audio_frame_data = b''
            play_audio('audio/wake_detected.mp3')
            # Esperar a que el usuario presione la tecla PTT
            keyboard.wait(PUSH_TO_TALK_KEY)
            while True:
                # Grabar audio en fragmentos de 0.3 segundos
                audio_chunk = recognizer.record(
                    source, duration=RECORD_INTERVAL)
                # Agregar el fragmento de audio al audio total
                audio_frame_data = audio_frame_data + audio_chunk.frame_data
                if not keyboard.is_pressed(PUSH_TO_TALK_KEY):
                    break
                # time.sleep(0.1)

        audio = sr.AudioData(
            audio_frame_data, sample_rate=44100, sample_width=2)
        try:
            textFromAudio = recognizer.recognize_google(
                audio, language="es-CO")
            phrase = textFromAudio.lower()
            if phrase is not None and phrase.strip() != '':
                if awake:
                    print(f"{USER_TEXT_COLOR}Usuario: {phrase}{TEXT_MARKUP}")
                break
            else:
                if awake:
                    did_not_understand_phrase = get_random_phrase(
                        DID_NOT_UNDERSTAND_PHRASES)
                    print_and_play(did_not_understand_phrase)
                else:
                    not_wake_word_phrase = get_random_phrase(
                        NOT_WAKE_WORD_PHRASES)
                    print_and_play(not_wake_word_phrase)
        except sr.RequestError:
            print_and_play("No me he podido conectar con la API")
        except sr.UnknownValueError:
            if awake:
                did_not_understand_phrase = get_random_phrase(
                    DID_NOT_UNDERSTAND_PHRASES)
                print_and_play(did_not_understand_phrase)
            else:
                not_wake_word_phrase = get_random_phrase(NOT_WAKE_WORD_PHRASES)
                print_and_play(not_wake_word_phrase)
        except Exception as e:
            print_system_output(
                "Error transcribiendo audio: ", e)
            print_and_play("Error transcribiendo audio")

    return phrase


def listen_audio_to_text(awake=True):
    phrase = ''
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 0.6
    while True:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            play_audio('audio/wake_detected.mp3')
            audio = recognizer.listen(source)
        try:
            textFromAudio = recognizer.recognize_google(
                audio, language="es-CO")
            phrase = textFromAudio.lower()
            if phrase is not None and phrase.strip() != '':
                if awake:
                    print(f"{USER_TEXT_COLOR}Usuario: {phrase}{TEXT_MARKUP}")
                else:
                    not_wake_word_phrase = get_random_phrase(
                        NOT_WAKE_WORD_PHRASES)
                    print_and_play(not_wake_word_phrase)
                break
            else:
                if awake:
                    did_not_understand_phrase = get_random_phrase(
                        DID_NOT_UNDERSTAND_PHRASES)
                    print_and_play(did_not_understand_phrase)
                else:
                    not_wake_word_phrase = get_random_phrase(
                        NOT_WAKE_WORD_PHRASES)
                    print_and_play(not_wake_word_phrase)
        except sr.RequestError:
            print_and_play("No me he podido conectar con la API")
        except sr.UnknownValueError:
            if awake:
                did_not_understand_phrase = get_random_phrase(
                    DID_NOT_UNDERSTAND_PHRASES)
                print_and_play(did_not_understand_phrase)
        except Exception as e:
            print_system_output(
                "Error transcribiendo audio: ", e)
            print_and_play("Error transcribiendo audio")

    return phrase


def wake_word_from_phrase(phrase):
    if any_word_of_list_in_phrase(EXIT_WORDS, phrase):
        wake_word = FUNCTION_EXIT
    elif any_word_of_list_in_phrase(BARD_WAKE_WORDS, phrase):
        wake_word = BARD_ASSISTANT_NAME
    elif any_word_of_list_in_phrase(GPT_WAKE_WORDS, phrase):
        wake_word = GPT_ASSISTANT_NAME
    elif any_word_of_list_in_phrase(BING_WAKE_WORDS, phrase):
        wake_word = BING_ASSISTANT_NAME
    else:
        wake_word = ''
    return wake_word


def function_prompt_from_phrase(phrase):
    if any_word_of_list_in_phrase(EXIT_WORDS, phrase):
        prompt = FUNCTION_EXIT
    elif any_word_of_list_in_phrase(RESET_WORDS, phrase):
        prompt = FUNCTION_RESET
    elif any_word_of_list_in_phrase(EXIT_WORDS, phrase):  # TODO:
        prompt = FUNCTION_YOUTUBE
    elif any_word_of_list_in_phrase(EXIT_WORDS, phrase):  # TODO:
        prompt = FUNCTION_SPOTIFY
    elif any_word_of_list_in_phrase(EXIT_WORDS, phrase):  # TODO:
        prompt = FUNCTION_WIKIPEDIA
    elif any_word_of_list_in_phrase(EXIT_WORDS, phrase):  # TODO:
        prompt = FUNCTION_WOLFRAM
    elif any_word_of_list_in_phrase(EXIT_WORDS, phrase):  # TODO:
        prompt = FUNCTION_WEB
    else:
        prompt = FUNCTION_ASSISTANT
    return prompt


def execute_special_function(function):
    if function == FUNCTION_EXIT:
        goodbye_phrase = get_random_phrase(FINISH_CHAT_PHRASES)
        print_and_play(goodbye_phrase)
        sys.exit(0)
    elif function == FUNCTION_YOUTUBE:  # TODO:
        prompt = 'youtube'
    elif function == FUNCTION_SPOTIFY:  # TODO:
        prompt = 'spotify'
    elif function == FUNCTION_WIKIPEDIA:  # TODO:
        prompt = 'wikipedia'
    elif function == FUNCTION_WOLFRAM:  # TODO:
        prompt = 'wolfram'
    elif function == FUNCTION_WEB:  # TODO:
        prompt = 'web'


def clear_text(text):
    cleared_text = text.replace("\n\n", "\n")
    cleared_text = cleared_text.replace(".", ". ")
    cleared_text = cleared_text.replace(".  ", ". ")
    cleared_text = cleared_text.replace(" .", ".")
    cleared_text = cleared_text.replace("  .", ".")
    annoying_characters = ["<", ">", "`", "*", "\r", "markdown"]
    for caracter in annoying_characters:
        cleared_text = cleared_text.replace(caracter, "")

    return cleared_text


def clear_bing_text(response):
    # Select only the bot response from the response dictionary
    for message in response["item"]["messages"]:
        if message["author"] == "bot":
            bot_response = message["text"]
    # Remove [^#^] citations in response
    bot_response = re.sub('\[\^\d+\^]', '', bot_response)
    # bot_response = bot_response.replace("markdown", "")
    bot_response = clear_text(bot_response)

    return bot_response


async def get_bing_response(prompt, bing_bot):
    print_system_output("Conectando con Bing...")
    initial_time = time.time()
    try:
        response = await bing_bot.ask(prompt=prompt, conversation_style=ConversationStyle.creative)
        final_time = time.time() - initial_time
        print(f"{SYSTEM_TEXT_COLOR}Tiempo de respuesta de Bing GPT: {round(final_time, 1)} segundos{TEXT_MARKUP}")
        bot_response = clear_bing_text(response)
        await bing_bot.close()
    except Exception as e:
        print_system_output(
            "No se ha podido conectar con Bing Edge GPT get_bing_response: ", e)
        print_and_play("No me he podido conectar con Bing Edge GPT")
        return False
    return bot_response


def get_chatgpt_response(prompt, messages=None):
    if messages is None:
        context = {"role": "system",
                   "content": INITIAL_CONTEXT}
        messages = [context]

    user_prompt = {"role": "user", "content": prompt}
    messages.append(user_prompt)

    print_system_output("Conectando con Chat GPT...")
    initial_time = time.time()
    # Send prompt to GPT-3.5-turbo API
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=80,
            # temperature=0.5,
            # frequency_penalty=0,
            # presence_penalty=0,
            # n=1,
            # stop=["\n"],
        )
        final_time = time.time() - initial_time
        print(f"{SYSTEM_TEXT_COLOR}Tiempo de respuesta de Chat GPT: {round(final_time, 1)} segundos{TEXT_MARKUP}")
    except Exception as e:
        print_system_output(
            "No se ha podido conectar con Chat GPT get_chatgpt_response: ", e)
        print_and_play("No me he podido conectar con Chat GPT")
        return False
    bot_response = response["choices"][0]["message"]["content"]

    messages.append({"role": "assistant", "content": bot_response})

    response = {
        "bot_response": bot_response,
        "messages": messages
    }

    return response


def get_bard_response(spanish_prompt, bard_bot):
    print_system_output("Conectando con Google Bard...")
    initial_time = time.time()
    english_prompt = translate_text(spanish_prompt, es_to_en=True)
    try:
        if not english_prompt:
            return False
        response = bard_bot.ask(english_prompt)
    except Exception as e:
        print_system_output(
            "No se ha podido conectar con Bard get_bard_response: ", e)
        print_and_play("No me he podido conectar con Bard")
        return False
    cleared_response = clear_text(response['content'])
    spanish_response = translate_text(cleared_response, es_to_en=False)
    if not spanish_response:
        return False
    final_time = time.time() - initial_time
    print(f"{SYSTEM_TEXT_COLOR}Tiempo de respuesta de Bard: {round(final_time, 1)} segundos{TEXT_MARKUP}")
    return spanish_response


def contextualize_bard(bard_bot):
    try:
        response = bard_bot.ask(BARD_CONTEXT)
    except Exception as e:
        pass


def get_wake_word():
    while True:
        if AUDIO_CAPTURE_MODE == 'listen':
            wake_prompt = listen_audio_to_text(False)
        else:
            wake_prompt = ptt_audio_to_text(False)
        wake_word = wake_word_from_phrase(wake_prompt)
        if wake_word == FUNCTION_EXIT:
            goodbye_phrase = get_random_phrase(FINISH_CHAT_PHRASES)
            print_and_play(goodbye_phrase)
            sys.exit(0)
        elif wake_word != '':
            break
    return wake_word


async def main(): #TODO: typing prompt feature
    create_audio_folder()

    while True:
        print_system_output(
            "Preparando a tu asistente...")  # TODO: Waking phrases wake keyyyy
        bing_bot = await Chatbot.create(cookie_path='settings/cookies.json')
        bard_bot = BardBot(BARD_TOKEN)
        contextualize_bard(bard_bot)
        
        welcome_phrase = get_random_phrase(WELCOME_PHRASES)
        print_and_play(welcome_phrase)

        print_system_output(
            f"Di una palabra clave ({BARD_WAKE_WORDS[0]}, {GPT_WAKE_WORDS[0]}, {BING_WAKE_WORDS[0]})...")

        wake_word = get_wake_word()

        activation_phrase = get_random_phrase(ACTIVATION_PHRASES)
        print_and_play(activation_phrase)

        messages = None

        while True:
            if AUDIO_CAPTURE_MODE == 'listen':
                prompt = listen_audio_to_text()
            else:
                prompt = ptt_audio_to_text()

            wake_prompt = function_prompt_from_phrase(prompt)
            if wake_prompt == FUNCTION_RESET:
                print_and_play('Empezando un nuevo chat...')
                break
            elif wake_prompt != FUNCTION_ASSISTANT:
                execute_special_function(wake_prompt)
                continue
            else:
                if wake_word == BING_ASSISTANT_NAME:
                    bot_response = await get_bing_response(prompt, bing_bot)
                    if not bot_response:
                        break
                elif wake_word == GPT_ASSISTANT_NAME:
                    response = get_chatgpt_response(prompt, messages)
                    if not response:
                        break
                    bot_response = response["bot_response"]
                    messages = response["messages"]
                elif wake_word == BARD_ASSISTANT_NAME:
                    bot_response = get_bard_response(prompt, bard_bot)
                    if not bot_response:
                        break

            print_and_play(bot_response)
            if not any_word_of_list_in_phrase(["?", "¿"], bot_response):
                continue_phrase = get_random_phrase(CONTINUE_CHAT_PHRASES)
                print_and_play(continue_phrase)
                # time.sleep(0.5)

if __name__ == "__main__":
    asyncio.run(main())
