import os
import sys
import re
import time
import random
import openai
import asyncio
import boto3
import pydub
from pydub import playback
import speech_recognition as sr
from EdgeGPT import Chatbot, ConversationStyle
from dotenv import load_dotenv
from settings.config import BING_WAKE_WORDS, GPT_WAKE_WORDS, EXIT_WORDS, CONTINUE_CHAT_PHRASES, FINISH_CHAT_PHRASES, RESET_WORDS, DID_NOT_UNDERSTAND_PHRASES

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


def any_word_of_list_in_phrase(list, phrase):
    for word in list:
        if word in phrase:
            return True

    return False

# def get_wake_word(phrase):
#     for word in GPT_WAKE_WORDS:
#         if word in phrase:
#             return 'chat'

#     for word in BING_WAKE_WORDS:
#         if word in phrase:
#             return 'bing'

#     return None


# def get_exit_confirmation(phrase):
#     for word in EXIT_WORDS:
#         if word in phrase:
#             return True

#     return False


def get_random_phrase(list):
    random_phrase = random.choice(list)

    return random_phrase


def synthesize_speech(text, output_filename):
    polly = session.client('polly', region_name='us-east-1')
    response = polly.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId='Lupe',
        Engine='neural'
    )

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
    print(f"Asistente: {message}")
    synthesize_speech(message, 'audio/response.mp3')
    play_audio('audio/response.mp3')


def audio_to_text():
    phrase = ''
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        # recognizer.adjust_for_ambient_noise(source)
        recognizer.pause_threshold = 1.5
        audio = recognizer.listen(source)

        try:
            textFromAudio = recognizer.recognize_google(
                audio, language="es-CO")
            phrase = textFromAudio.lower()
            print(f"Usuario: {phrase}")

        except sr.RequestError:
            print_and_play("No me he podido conectar con la API")
        except sr.UnknownValueError:
            print_and_play("No entendí lo que dijiste, por favor repítelo")
        except Exception as e:
            print_and_play(f"Error transcribiendo audio: {e}")

    return phrase


def wake_word_from_audio():
    while True:
        phrase = audio_to_text()
        if any_word_of_list_in_phrase(BING_WAKE_WORDS, phrase):
            wake_word = 'bing'
            break
        elif any_word_of_list_in_phrase(GPT_WAKE_WORDS, phrase):
            wake_word = 'chat'
            break
        elif any_word_of_list_in_phrase(RESET_WORDS, phrase):
            wake_word = 'reset'
            break
        elif any_word_of_list_in_phrase(EXIT_WORDS, phrase):
            wake_word = 'exit'
            break
        else:
            print("Di una palabra clave")
    return wake_word


def clear_bing_text(response):
    # Select only the bot response from the response dictionary
    for message in response["item"]["messages"]:
        if message["author"] == "bot":
            bot_response = message["text"]
    # Remove [^#^] citations in response
    bot_response = re.sub('\[\^\d+\^\]', '', bot_response)
    return bot_response


async def get_bing_response(prompt):
    bot = Chatbot(cookie_path='settings/cookies.json')

    print("Conectando con Bing...")
    response = await bot.ask(prompt=prompt, conversation_style=ConversationStyle.creative)
    bot_response = clear_bing_text(response)
    await bot.close()
    return bot_response


def get_chatgpt_response(prompt, messages=None):
    if messages is None:
        print("🆕 Nueva conversación creada")
        context = {"role": "system",
                   "content": "Eres un asistente muy útil."}
        messages = [context]

    user_prompt = {"role": "user", "content": prompt}
    messages.append(user_prompt)

    # Send prompt to GPT-3.5-turbo API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.5,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        n=1,
        stop=["\nUser:"],
    )

    bot_response = response["choices"][0]["message"]["content"]

    messages.append({"role": "assistant", "content": bot_response})

    return [bot_response, messages]


async def main():
    create_audio_folder()

    while True:

        print("Esperando una palabra clave...")

        wake_word = wake_word_from_audio()
        if wake_word == 'exit':
            goodbye_phrase = get_random_phrase(FINISH_CHAT_PHRASES)
            print_and_play(goodbye_phrase)
            sys.exit(0)

        print_and_play('¿En qué puedo ayudarte?')

        messages = None

        while True:
            prompt = audio_to_text()
            if prompt is not None and prompt.strip() != '':
                if any_word_of_list_in_phrase(EXIT_WORDS, prompt):
                    goodbye_phrase = get_random_phrase(FINISH_CHAT_PHRASES)
                    print_and_play(goodbye_phrase)
                    sys.exit(0)
                elif wake_word == 'reset':
                    print_and_play('Empezando un nuevo chat...')
                    break
                elif wake_word == 'bing':
                    bot_response = await get_bing_response(prompt)
                else:
                    response = get_chatgpt_response(prompt, messages)
                    bot_response = response[0]
                    messages = response[1]
                print_and_play(bot_response)
                continue_phrase = get_random_phrase(CONTINUE_CHAT_PHRASES)
                print_and_play(continue_phrase)
                time.sleep(1.5)
            else:
                did_not_understand_phrase = get_random_phrase(
                    DID_NOT_UNDERSTAND_PHRASES)
                print_and_play(did_not_understand_phrase)
                time.sleep(1.5)

if __name__ == "__main__":
    asyncio.run(main())
