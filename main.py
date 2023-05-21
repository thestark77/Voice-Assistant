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
from settings.config import DEFAULT_ASSISTANT_LANGUAGE, AUDIO_CAPTURE_MODE, PUSH_TO_TALK_KEY, INPUT_MODE, SPEECH_SPEED, GPT_MAX_TOKENS, RECORD_INTERVAL, LANGUAGE_SETTINGS, BING_WAKE_WORDS, GPT_WAKE_WORDS, BARD_WAKE_WORDS, EXIT_WORDS, RESET_WORDS, CHANGE_LANGUAGE_WORDS, YOUTUBE_KEYWORDS, SPOTIFY_KEYWORDS, WIKIPEDIA_KEYWORDS, WOLFRAM_KEYWORDS, WEB_KEYWORDS, GPT_INITIAL_CONTEXT, BARD_INITIAL_CONTEXT, LOADING_PHRASES, ACTIVATION_PHRASES, CONTINUE_CHAT_PHRASES, FINISH_CHAT_PHRASES, DID_NOT_UNDERSTAND_PHRASES, NOT_WAKE_WORD_PHRASES, WELCOME_PHRASES, FUNCTION_YOUTUBE, FUNCTION_SPOTIFY, FUNCTION_WIKIPEDIA, FUNCTION_WOLFRAM, FUNCTION_WEB, FUNCTION_ASSISTANT, FUNCTION_RESET, BARD_ASSISTANT_NAME, GPT_ASSISTANT_NAME, BING_ASSISTANT_NAME, ASSISTANT_TEXT_COLOR, USER_TEXT_COLOR, TEXT_MARKUP, SYSTEM_TEXT_COLOR


assistant_language = DEFAULT_ASSISTANT_LANGUAGE


def handle_keyboard_interrupt(signal, frame):
    # Acciones a realizar al recibir una interrupción de teclado
    print_system_output("Programa detenido por el usuario")
    goodbye_phrase = get_random_phrase(FINISH_CHAT_PHRASES[assistant_language])
    print_and_play(goodbye_phrase)
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
            VoiceId=LANGUAGE_SETTINGS[assistant_language]["voice_id"],
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
        # TODO: create a list with 2 arrays of text like this in both languages
        print(f"{ASSISTANT_TEXT_COLOR}Asistente: {message}{TEXT_MARKUP}")
        synthesize_speech(message, 'audio/response.mp3')
        play_audio('audio/response.mp3')


def get_text_from_audio(audio, recognizer, awake=True):
    phrase = ''
    returning_phrase = ''
    try:
        textFromAudio = recognizer.recognize_google(
            audio, language=LANGUAGE_SETTINGS[assistant_language]["language"])
        phrase = textFromAudio.lower()
        if phrase is not None and phrase.strip() != '':
            if awake:
                print(f"{USER_TEXT_COLOR}Usuario: {phrase}{TEXT_MARKUP}")

            returning_phrase = phrase
        else:
            if awake:
                did_not_understand_phrase = get_random_phrase(
                    DID_NOT_UNDERSTAND_PHRASES[assistant_language])
                print_and_play(did_not_understand_phrase)
            else:
                not_wake_word_phrase = get_random_phrase(
                    NOT_WAKE_WORD_PHRASES[assistant_language])
                print_and_play(not_wake_word_phrase)
    except sr.RequestError:
        print_and_play("No me he podido conectar con la API")
    except sr.UnknownValueError:
        if awake:
            did_not_understand_phrase = get_random_phrase(
                DID_NOT_UNDERSTAND_PHRASES[assistant_language])
            print_and_play(did_not_understand_phrase)
        else:
            not_wake_word_phrase = get_random_phrase(
                NOT_WAKE_WORD_PHRASES[assistant_language])
            print_and_play(not_wake_word_phrase)
    except Exception as e:
        print_system_output(
            "Error transcribiendo audio: ", e)
        print_and_play("Error transcribiendo audio")

    return returning_phrase


def ptt_audio_to_text(awake=True):
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

        audio = sr.AudioData(
            audio_frame_data, sample_rate=44100, sample_width=2)

        phrase = get_text_from_audio(audio, recognizer, awake)
        if phrase != '':
            break
    print(phrase)
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

        phrase = get_text_from_audio(audio, recognizer, awake)
        if phrase != '':
            break

    return phrase


def system_functions_from_phrase(phrase):
    global assistant_language
    system_function = ''
    if any_word_of_list_in_phrase(EXIT_WORDS[assistant_language], phrase):
        goodbye_phrase = get_random_phrase(
            FINISH_CHAT_PHRASES[assistant_language])
        print_and_play(goodbye_phrase)
        sys.exit(0)
    elif any_word_of_list_in_phrase(RESET_WORDS[assistant_language], phrase):
        system_function = FUNCTION_RESET
    else:
        if assistant_language == 'en' and any_word_of_list_in_phrase(CHANGE_LANGUAGE_WORDS[assistant_language], phrase):
            assistant_language = "es"
            system_function = FUNCTION_RESET
        elif assistant_language == 'es' and any_word_of_list_in_phrase(CHANGE_LANGUAGE_WORDS[assistant_language], phrase):
            assistant_language = "en"
            system_function = FUNCTION_RESET

    return system_function


def wake_word_from_phrase(phrase):
    system_function = system_functions_from_phrase(phrase)
    if system_function != '':
        wake_word = system_function
    elif any_word_of_list_in_phrase(BARD_WAKE_WORDS, phrase):
        wake_word = BARD_ASSISTANT_NAME
    elif any_word_of_list_in_phrase(GPT_WAKE_WORDS, phrase):
        wake_word = GPT_ASSISTANT_NAME
    elif any_word_of_list_in_phrase(BING_WAKE_WORDS, phrase):
        wake_word = BING_ASSISTANT_NAME
    else:
        wake_word = ''
    return wake_word


def check_words_in_order_in_a_phrase(phrase, words_list):  # (frase1, frase2)
    phrase = phrase.split()
    words_list = words_list.split()

    # Verificar si todas las palabras de frase2 están en frase1 en el mismo orden
    if all(word in phrase for word in words_list):
        # Verificar si el índice de cada palabra en frase1 es igual al índice correspondiente en frase2
        if all(phrase.index(words_list[i]) == i for i in range(len(words_list))):
            return True

    return False


def check_a_list_of_words_in_order_in__phrases(phrase, list_of_list_of_words):
    for list in list_of_list_of_words:
        key_phrase = check_words_in_order_in_a_phrase(phrase, list)
        if key_phrase:
            return True
    return False


def function_prompt_from_phrase(phrase):
    system_function = system_functions_from_phrase(phrase)
    if system_function != '':
        execute_function = system_function
    elif check_a_list_of_words_in_order_in__phrases(phrase, YOUTUBE_KEYWORDS[assistant_language]):
        execute_function = FUNCTION_YOUTUBE
    elif check_a_list_of_words_in_order_in__phrases(phrase, SPOTIFY_KEYWORDS[assistant_language]):
        execute_function = FUNCTION_SPOTIFY
    elif check_a_list_of_words_in_order_in__phrases(phrase, WIKIPEDIA_KEYWORDS[assistant_language]):
        execute_function = FUNCTION_WIKIPEDIA
    elif check_a_list_of_words_in_order_in__phrases(phrase, WOLFRAM_KEYWORDS[assistant_language]):
        execute_function = FUNCTION_WOLFRAM
    elif check_a_list_of_words_in_order_in__phrases(phrase, WEB_KEYWORDS[assistant_language]):
        execute_function = FUNCTION_WEB
    else:
        execute_function = FUNCTION_ASSISTANT
    return execute_function


# def open_youtube(prompt):
# def open_spotify(prompt):
# def open_wikipedia(prompt):
# def open_wolfram(prompt):
# def open_web(prompt):


def execute_special_function(function, prompt):
    if function == FUNCTION_YOUTUBE:  # TODO:
        print('youtube')
    elif function == FUNCTION_SPOTIFY:  # TODO:
        print('spotify')
    elif function == FUNCTION_WIKIPEDIA:  # TODO:
        print('wikipedia')
    elif function == FUNCTION_WOLFRAM:  # TODO:
        print('wolfram')
    elif function == FUNCTION_WEB:  # TODO: # format the keywords to avoyd spaces on url and know when they start and end
        print('web')


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
        initial_context = GPT_INITIAL_CONTEXT[assistant_language].replace(
            "[ASSISTANT_NAME]", LANGUAGE_SETTINGS[assistant_language]["assistant_name"])
        context = {"role": "system",
                   "content": initial_context}
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
            max_tokens=GPT_MAX_TOKENS,
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

    if not response:
        return False
    bot_response = response["choices"][0]["message"]["content"]

    messages.append({"role": "assistant", "content": bot_response})

    response = {
        "bot_response": bot_response,
        "messages": messages
    }

    return response


def get_bard_response(prompt, bard_bot):
    print_system_output("Conectando con Google Bard...")
    initial_time = time.time()
    if assistant_language != 'en':
        prompt = translate_text(prompt, es_to_en=True)
    try:
        if not prompt:
            return False
        response = bard_bot.ask(prompt)
    except Exception as e:
        print_system_output(
            "No se ha podido conectar con Bard get_bard_response: ", e)
        print_and_play("No me he podido conectar con Bard")
        return False
    bard_response = clear_text(response['content'])
    if assistant_language != 'en':
        bard_response = translate_text(bard_response, es_to_en=False)
    if not bard_response:
        return False
    final_time = time.time() - initial_time
    print(f"{SYSTEM_TEXT_COLOR}Tiempo de respuesta de Bard: {round(final_time, 1)} segundos{TEXT_MARKUP}")
    return bard_response


def contextualize_bard(bard_bot):
    initial_context = BARD_INITIAL_CONTEXT.replace(
        "[ASSISTANT_NAME]", LANGUAGE_SETTINGS[assistant_language]["assistant_name"])
    try:
        bard_bot.ask(initial_context)
    except Exception as e:
        pass


def get_user_input(awake):
    if INPUT_MODE == 'text':
        user_input = input(f"{USER_TEXT_COLOR}Usuario: {TEXT_MARKUP}")
    else:
        if AUDIO_CAPTURE_MODE == 'listen':
            user_input = listen_audio_to_text(awake)
        else:
            user_input = ptt_audio_to_text(awake)

    return user_input


def get_wake_word():
    while True:
        text_from_audio = get_user_input(False)

        wake_word = wake_word_from_phrase(text_from_audio)

        if wake_word == FUNCTION_RESET:
            print_and_play('Empezando un nuevo chat...')
            return FUNCTION_RESET
        elif wake_word != '':
            break
        else:
            not_wake_word_phrase = get_random_phrase(
                NOT_WAKE_WORD_PHRASES[assistant_language])
            print_and_play(not_wake_word_phrase)
    return wake_word


async def main():
    create_audio_folder()

    while True:
        assistant_name = LANGUAGE_SETTINGS[assistant_language]["assistant_name"]
        loading_phrase = get_random_phrase(LOADING_PHRASES[assistant_language])
        print_and_play(loading_phrase)

        bing_bot = await Chatbot.create(cookie_path='settings/cookies.json')
        bard_bot = BardBot(BARD_TOKEN)
        contextualize_bard(bard_bot)

        welcome_phrase = get_random_phrase(WELCOME_PHRASES[assistant_language])
        parsed_welcome_phrase = welcome_phrase.replace("{}", assistant_name)
        print_and_play(parsed_welcome_phrase)

        print_system_output(
            f"Di una palabra clave ({BARD_WAKE_WORDS[0]}, {GPT_WAKE_WORDS[0]}, {BING_WAKE_WORDS[0]})...")

        wake_word = get_wake_word()
        if wake_word == FUNCTION_RESET:
            continue

        if wake_word == 'bard':
            print_system_output(
                "Modelo seleccionado: Bard...")
        elif wake_word == 'gpt':
            print_system_output(
                "Modelo seleccionado: Chat GPT...")
        elif wake_word == 'bing':
            print_system_output(
                "Modelo seleccionado: Bing+GPT...")

        activation_phrase = get_random_phrase(
            ACTIVATION_PHRASES[assistant_language])
        print_and_play(activation_phrase)

        messages = None

        while True:
            prompt = get_user_input(True)

            execute_function = function_prompt_from_phrase(prompt)
            if execute_function == FUNCTION_RESET:
                print_and_play('Empezando un nuevo chat...')
                break
            elif execute_function != FUNCTION_ASSISTANT:
                execute_special_function(execute_function, prompt)
                continue_phrase = get_random_phrase(
                    CONTINUE_CHAT_PHRASES[assistant_language])
                print_and_play(continue_phrase)
                continue
            else:
                if wake_word == BING_ASSISTANT_NAME:
                    bot_response = await get_bing_response(prompt, bing_bot)
                elif wake_word == GPT_ASSISTANT_NAME:
                    response = get_chatgpt_response(prompt, messages)
                    if response:
                        bot_response = response["bot_response"]
                        messages = response["messages"]
                elif wake_word == BARD_ASSISTANT_NAME:
                    bot_response = get_bard_response(prompt, bard_bot)

            if not bot_response:
                break
            else:
                print_and_play(bot_response)
                if not any_word_of_list_in_phrase(["?", "¿"], bot_response):
                    continue_phrase = get_random_phrase(
                        CONTINUE_CHAT_PHRASES[assistant_language])
                    print_and_play(continue_phrase)

if __name__ == "__main__":
    asyncio.run(main())
