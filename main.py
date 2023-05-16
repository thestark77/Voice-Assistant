import os
import openai
import asyncio
import re
import whisper
import boto3
import pydub
from pydub import playback
import speech_recognition as sr
from EdgeGPT import Chatbot, ConversationStyle
from dotenv import load_dotenv
from settings.config import BING_WAKE_WORD, GPT_WAKE_WORD

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

def get_wake_word(phrase):
    if BING_WAKE_WORD in phrase.lower():
        return BING_WAKE_WORD
    elif GPT_WAKE_WORD in phrase.lower():
        return GPT_WAKE_WORD
    else:
        return None


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

    # Comprobar si la carpeta 'audio' existe
    audio_folder = os.path.join(current_path, 'audio')

    if not os.path.exists(audio_folder):
        os.mkdir(audio_folder)

def print_and_play(message):
    print(message)
    synthesize_speech(message, 'audio/response.mp3')
    play_audio('audio/response.mp3')


def audio_to_text(filename):
    phrase = ''
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        # recognizer.adjust_for_ambient_noise(source)
        recognizer.pause_threshold = 1.5
        audio = recognizer.listen(source)

        try:
            with open(filename, "wb") as f:
                f.write(audio.get_wav_data())
            model = whisper.load_model("tiny")
            result = model.transcribe(filename, language="spanish", fp16=False)
            phrase = result["text"]
            # textFromAudio = recognizer.recognize_google(audio, language="es-CO")
            # phrase = textFromAudio.lower()
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
        phrase = audio_to_text("audio/audio.wav")
        wake_word = get_wake_word(phrase)
        if wake_word is not None:
            break
        else:
            print("Di una palabra clave")
    return wake_word


async def get_bing_response(prompt):
    bot = Chatbot(cookie_path='settings/cookies.json')

    print("Conectando con Bing...")
    response = await bot.ask(prompt=prompt, conversation_style=ConversationStyle.creative)
    print("Bing answered")
    # Select only the bot response from the response dictionary
    for message in response["item"]["messages"]:
        if message["author"] == "bot":
            bot_response = message["text"]
    # Remove [^#^] citations in response
    bot_response = re.sub('\[\^\d+\^\]', '', bot_response)
    await bot.close()
    return bot_response


def get_chatgpt_response(prompt):
    # Send prompt to GPT-3.5-turbo API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content":
             "Eres un asistente muy útil."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.5,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        n=1,
        stop=["\nUser:"],
    )

    bot_response = response["choices"][0]["message"]["content"]
    return bot_response


async def main():
    create_audio_folder()

    while True:

        print(
            f"Esperando las palabras clave {BING_WAKE_WORD} o {GPT_WAKE_WORD}...")

        wake_word = wake_word_from_audio()

        print('Respuesta del bot: ')
        print_and_play('¿En qué puedo ayudarte?')

        prompt = audio_to_text("audio/audio_prompt.wav")

        if wake_word == BING_WAKE_WORD:
            bot_response = await get_bing_response(prompt)
            # bot_response = prompt
        # else:
            # bot_response = get_chatgpt_response(prompt)
            # bot_response = prompt

        print("Respuesta del bot: ")
        print_and_play(bot_response)

if __name__ == "__main__":
    asyncio.run(main())
