import os
import sys
import re
import time
import random
import threading
import msvcrt
import keyboard
import openai
import asyncio
import boto3
import pydub
from pydub import playback
import speech_recognition as sr
from EdgeGPT import Chatbot, ConversationStyle
from dotenv import load_dotenv
from settings.config import BING_WAKE_WORDS, GPT_WAKE_WORDS, EXIT_WORDS, FINISH_CHAT_PHRASES, RESET_WORDS, DID_NOT_UNDERSTAND_PHRASES, CONTINUE_CHAT_PHRASES, INITIAL_CONTEXT, ACTIVATION_PHRASES, TEXT_MARKUP, ASSISTANT_TEXT_COLOR, USER_TEXT_COLOR, SYSTEM_TEXT_COLOR, SPEECH_SPEED, PUSH_TO_TALK_KEY, RECORD_INTERVAL, AUDIO_CAPTURE_MODE

load_dotenv()

GPT_API_KEY = os.environ['GPT_API_KEY']
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

# Initialize the OpenAI API
openai.api_key = GPT_API_KEY

# Initialize the AWS BOTO3 API
session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)


def print_system_output(message, element=None):
    if element is not None:
        print(f"{SYSTEM_TEXT_COLOR}{message}{element}{TEXT_MARKUP}")
    else:
        print(f"{SYSTEM_TEXT_COLOR}{message}{TEXT_MARKUP}")


# def exit_key():
#     while True:
#         if msvcrt.kbhit():
#             key = msvcrt.getch()
#             if key.upper() == b'F':  # Verificar si se presiona la tecla "F"
#                 print_system_output(¡Se presionó la tecla F! Finalizando el programa...)

#                 os._exit(0)


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
    # recognizer.pause_threshold = 0.6
    while True:
        with sr.Microphone() as source:
            # Inicializar audio vacío
            audio = sr.AudioData(
                frame_data=b'', sample_rate=44100, sample_width=2)
            play_audio('audio/wake_detected.mp3')
            # print_system_output("Presiona la tecla espacio para empezar a grabar...")
            # Esperar a que el usuario presione la tecla PTT
            keyboard.wait(PUSH_TO_TALK_KEY)
            while True:
                # Grabar audio en fragmentos de 0.3 segundos
                audio_chunk = recognizer.record(
                    source, duration=RECORD_INTERVAL)
                # print(audio_chunk)
                # Agregar el fragmento de audio al audio total
                new_frame_data = audio.frame_data + audio_chunk.frame_data
                audio = sr.AudioData(
                    frame_data=new_frame_data, sample_rate=44100, sample_width=2)
                if not keyboard.is_pressed(PUSH_TO_TALK_KEY):
                    break
                # time.sleep(0.1)

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
        except sr.RequestError:
            print_and_play("No me he podido conectar con la API")
        except sr.UnknownValueError:
            if awake:
                did_not_understand_phrase = get_random_phrase(
                    DID_NOT_UNDERSTAND_PHRASES)
                print_and_play(did_not_understand_phrase)
        except Exception as e:
            print_and_play(f"Error transcribiendo audio: {e}")

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
                break
            else:
                if awake:
                    did_not_understand_phrase = get_random_phrase(
                        DID_NOT_UNDERSTAND_PHRASES)
                    print_and_play(did_not_understand_phrase)
        except sr.RequestError:
            print_and_play("No me he podido conectar con la API")
        except sr.UnknownValueError:
            if awake:
                did_not_understand_phrase = get_random_phrase(
                    DID_NOT_UNDERSTAND_PHRASES)
                print_and_play(did_not_understand_phrase)
        except Exception as e:
            print_and_play(f"Error transcribiendo audio: {e}")

    return phrase


def wake_word_from_phrase(phrase):
    if any_word_of_list_in_phrase(EXIT_WORDS, phrase):
        wake_word = 'exit'
    elif any_word_of_list_in_phrase(BING_WAKE_WORDS, phrase):
        wake_word = 'bing'
    elif any_word_of_list_in_phrase(GPT_WAKE_WORDS, phrase):
        wake_word = 'chat'
    else:
        wake_word = ''
    return wake_word


def function_prompt_from_phrase(phrase):
    if any_word_of_list_in_phrase(EXIT_WORDS, phrase):
        prompt = 'exit'
    elif any_word_of_list_in_phrase(RESET_WORDS, phrase):
        prompt = 'reset'
    elif any_word_of_list_in_phrase(EXIT_WORDS, phrase):  # TODO:
        prompt = 'youtube'
    elif any_word_of_list_in_phrase(EXIT_WORDS, phrase):  # TODO:
        prompt = 'spotify'
    elif any_word_of_list_in_phrase(EXIT_WORDS, phrase):  # TODO:
        prompt = 'wikipedia'
    elif any_word_of_list_in_phrase(EXIT_WORDS, phrase):  # TODO:
        prompt = 'wolfram'
    else:
        prompt = 'assistant'
    return prompt


def execute_special_function(function):
    if function == 'exit':
        goodbye_phrase = get_random_phrase(FINISH_CHAT_PHRASES)
        print_and_play(goodbye_phrase)
        sys.exit(0)
    elif function == 'youtube':  # TODO:
        prompt = 'youtube'
    elif function == 'spotify':  # TODO:
        prompt = 'spotify'
    elif function == 'wikipedia':  # TODO:
        prompt = 'wikipedia'
    elif function == 'wolfram':  # TODO:
        prompt = 'wolfram'


def clear_bing_text(response):
    # Select only the bot response from the response dictionary
    for message in response["item"]["messages"]:
        if message["author"] == "bot":
            bot_response = message["text"]
    # Remove [^#^] citations in response
    bot_response = re.sub('\[\^\d+<>\^`]', '', bot_response)
    return bot_response


async def get_bing_response(prompt, bot):
    # bot = Chatbot(cookie_path='settings/cookies.json')
    print_system_output("Conectando con Bing...")
    try:
        response = await bot.ask(prompt=prompt, conversation_style=ConversationStyle.creative)
        # print(response)
        bot_response = clear_bing_text(response)
        await bot.close()
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
    # Send prompt to GPT-3.5-turbo API
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.5,
            max_tokens=80,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            n=1,
            stop=["\nUser:"],
        )
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


async def main():
    create_audio_folder()
    # Crear y ejecutar el hilo para verificar la tecla "F"
    # thread = threading.Thread(target=exit_key)
    # thread.start()

    while True:
        print_system_output("Di una palabra clave (chat, hola)...")
        bot = await Chatbot.create(cookie_path='settings/cookies.json')

        while True:
            if AUDIO_CAPTURE_MODE == 'listen':
                wake_prompt = listen_audio_to_text(False)
            else:
                wake_prompt = ptt_audio_to_text(False)
            wake_word = wake_word_from_phrase(wake_prompt)
            if wake_word == 'exit':
                goodbye_phrase = get_random_phrase(FINISH_CHAT_PHRASES)
                print_and_play(goodbye_phrase)
                sys.exit(0)
            elif wake_word != '':
                break

        # play_audio('audio/wake_detected.mp3')
        activation_phrase = get_random_phrase(ACTIVATION_PHRASES)
        print_and_play(activation_phrase)

        messages = None

        while True:
            if AUDIO_CAPTURE_MODE == 'listen':
                prompt = listen_audio_to_text()
            else:
                prompt = ptt_audio_to_text()
            wake_prompt = function_prompt_from_phrase(prompt)
            if wake_prompt == 'reset':
                print_and_play('Empezando un nuevo chat...')
                break
            elif wake_prompt != 'assistant':
                execute_special_function(wake_prompt)
                continue
            else:
                if wake_word == 'bing':
                    # break  # TODO: EdgeGPT currently unavailable
                    bot_response = await get_bing_response(prompt, bot)
                    if not bot_response:
                        break
                else:
                    response = get_chatgpt_response(prompt, messages)
                    if not response:
                        break
                    bot_response = response["bot_response"]
                    messages = response["messages"]

            print_and_play(bot_response)
            if not any_word_of_list_in_phrase(["?", "¿"], bot_response):
                continue_phrase = get_random_phrase(CONTINUE_CHAT_PHRASES)
                print_and_play(continue_phrase)
                time.sleep(0.5)

if __name__ == "__main__":
    asyncio.run(main())
