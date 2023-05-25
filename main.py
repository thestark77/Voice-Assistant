from settings.config import DEFAULT_ASSISTANT_LANGUAGE, DEFAULT_INPUT_MODE, PUSH_TO_TALK_KEYS, GPT_MAX_TOKENS, RECORD_INTERVAL, BING_WAKE_WORDS, GPT_WAKE_WORDS, BARD_WAKE_WORDS, EXIT_WORDS, RESET_WORDS, CHANGE_LANGUAGE_WORDS, YOUTUBE_KEYWORDS, SPOTIFY_KEYWORDS, WIKIPEDIA_KEYWORDS, WOLFRAM_KEYWORDS, WEB_KEYWORDS, GPT_INITIAL_CONTEXT, BARD_INITIAL_CONTEXT, LOADING_PHRASES, ACTIVATION_PHRASES, CONTINUE_CHAT_PHRASES, FINISH_CHAT_PHRASES, DID_NOT_UNDERSTAND_PHRASES, NOT_WAKE_WORD_PHRASES, WELCOME_PHRASES, FUNCTION_YOUTUBE, FUNCTION_SPOTIFY, FUNCTION_WIKIPEDIA, FUNCTION_WOLFRAM, FUNCTION_WEB, FUNCTION_ASSISTANT, FUNCTION_RESET, BARD_ASSISTANT_NAME, GPT_ASSISTANT_NAME, BING_ASSISTANT_NAME, ASSISTANT_TEXT_COLOR, USER_TEXT_COLOR, TEXT_MARKUP, SYSTEM_TEXT_COLOR, SYSTEM_TEXTS, LANGUAGE_CHANGED_PHRASES, ASSISTANT_RESPONSE_LENGTH, RESPONSE_LENGTH_MARGIN, FUNCTION_CHANGE_INPUT_MODE, CHANGE_INPUT_MODE_WORDS, DEFAULT_AUDIO_CAPTURE_MODE, INPUT_MODE_CHANGED_PHRASES, CHANGE_AUDIO_CAPTURE_MODE_WORDS, AUDIO_CAPTURE_MODE_CHANGED_PHRASES, FUNCTION_CHANGE_AUDIO_CAPTURE_MODE, SELECTED_ENGLISH_ASSISTANT, SELECTED_SPANISH_ASSISTANT, SPEECH_RATE_INCREMENT, SPEECH_PITCH_INCREMENT, PITCH_CONTOUR, VOICE_STYLE, VOICE_STYLE_DEGREE, SPANISH_ASSISTANT_NAME, ENGLISH_ASSISTANT_NAME, DELETE_SCRIPT, DELETE_GARBAGE_KEYWORDS, FUNCTION_DELETE_GARBAGE, RESTORE_GARBAGE_KEYWORDS, FUNCTION_RESTORE_GARBAGE, RESTORE_SCRIPT, SYSTEM_TASK, WHATSAPP_KEYWORDS, FUNCTION_WHATSAPP, EXIT_WOLFRAM_KEYWORDS, EXIT_WHATSAPP_KEYWORDS
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
import threading
import pydub
import subprocess
import pywhatkit
import webbrowser
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import wikipedia
import wolframalpha
import urllib.parse
from deep_translator import GoogleTranslator as Translator
from pydub import playback
import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech.audio import AudioOutputConfig
import speech_recognition as sr
from EdgeGPT import Chatbot, ConversationStyle
from Bard import Chatbot as BardBot
from dotenv import load_dotenv
import warnings
from bs4 import GuessedAtParserWarning
warnings.filterwarnings('ignore', category=GuessedAtParserWarning)

# Carga las variables de entorno
load_dotenv()

assistant_language = DEFAULT_ASSISTANT_LANGUAGE
input_mode = DEFAULT_INPUT_MODE
audio_capture_mode = DEFAULT_AUDIO_CAPTURE_MODE
garbage_cleaned = False

GPT_API_KEY = os.environ['GPT_API_KEY']
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
BARD_TOKEN = os.environ['BARD_TOKEN']
AZURE_SPEECH_API_KEY = os.environ['AZURE_SPEECH_API_KEY']
AZURE_SPEECH_REGION = os.environ['AZURE_SPEECH_REGION']
SPOTIFY_ID_CLIENT = os.environ['SPOTIFY_ID_CLIENT']
SPOTIFY_CLIENT_SECRET = os.environ['SPOTIFY_CLIENT_SECRET']
WOLFRAM_API_KEY = os.environ['WOLFRAM_API_KEY']
# Initialize the OpenAI API
openai.api_key = GPT_API_KEY


# Initialize the AWS BOTO3 API

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

azure_speech_config = speechsdk.SpeechConfig(
    subscription=AZURE_SPEECH_API_KEY,
    region=AZURE_SPEECH_REGION,
)
audio_config = AudioOutputConfig(use_default_speaker=True)

# Autenticación
client_credentials_manager = SpotifyClientCredentials(
    SPOTIFY_ID_CLIENT, SPOTIFY_CLIENT_SECRET)
spotify = spotipy.Spotify(
    client_credentials_manager=client_credentials_manager)

wolframClient = wolframalpha.Client(WOLFRAM_API_KEY)


def handle_keyboard_interrupt(signal, frame):
    # Acciones a realizar al recibir una interrupción de teclado
    print_system_output(get_system_text('1'))
    goodbye_phrase = get_random_phrase(FINISH_CHAT_PHRASES[assistant_language])
    print_and_play(goodbye_phrase)
    if garbage_cleaned:
        restore_garbage()
    sys.exit(0)  # Finaliza el programa sin mostrar el traceback


# Configurar el manejador de la señal de interrupción de teclado
signal.signal(signal.SIGINT, handle_keyboard_interrupt)


def get_assistant_name():
    if assistant_language == 'en':
        assistant_name = ENGLISH_ASSISTANT_NAME
    else:
        assistant_name = SPANISH_ASSISTANT_NAME
    return assistant_name


def get_system_text(system_text_id, aditional_string=''):
    system_text = f"{SYSTEM_TEXTS[assistant_language][str(system_text_id)]}{aditional_string}"
    if system_text:
        return system_text
    else:
        return ''


def get_urls_from_phrase(phrase):
    # Expresión regular para detectar URLs
    pattern = r'(https?://\S+)'

    # Encontrar todas las coincidencias de URLs en el texto
    urls = re.findall(pattern, phrase)

    return urls


def translate_text(text, es_to_en=True):
    try:
        if es_to_en:
            translated_text = Translator(
                source='es', target='en').translate(text=text)
        else:
            translated_text = Translator(
                source='en', target='es').translate(text=text)
    except Exception as e:
        print_system_output(get_system_text('2', ' translate_text: '), e)
        print_and_play(get_system_text('2'))
        return False

    return translated_text


def print_system_output(message, element=None):
    if element is not None:
        print(f"{SYSTEM_TEXT_COLOR}{message}{element}{TEXT_MARKUP}")
    else:
        print(f"{SYSTEM_TEXT_COLOR}{message}{TEXT_MARKUP}")


def print_user_output(message):
    print(f"{USER_TEXT_COLOR}{message}{TEXT_MARKUP}")


def any_word_of_list_in_phrase(list, phrase):
    for word in list:
        if word in phrase:
            return True

    return False


def get_random_phrase(list):
    random_phrase = random.choice(list)

    return random_phrase


def synthesize_to_speaker(text):
    if assistant_language == 'en':
        voice_id = SELECTED_ENGLISH_ASSISTANT['voice_id']
        language = SELECTED_ENGLISH_ASSISTANT['language']
    else:
        voice_id = SELECTED_SPANISH_ASSISTANT['voice_id']
        language = SELECTED_SPANISH_ASSISTANT['language']
    try:
        speech_synthesizer = speechsdk.SpeechSynthesizer(
            speech_config=azure_speech_config, audio_config=audio_config)
        ssml_text = f'''
        <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="{language}">
        <voice name="{voice_id}">
        [EXPRESSION-OPEN]
        <prosody rate="{SPEECH_RATE_INCREMENT}%" pitch="{SPEECH_PITCH_INCREMENT}%" contour="{PITCH_CONTOUR}">
        {text}
        </prosody>
        [EXPRESSION-CLOSE]
        </voice>
        </speak>
        '''
        if VOICE_STYLE != '' and VOICE_STYLE.lower() != 'default' and any_word_of_list_in_phrase(SELECTED_ENGLISH_ASSISTANT['styles'], VOICE_STYLE):
            if VOICE_STYLE_DEGREE != '' and str(VOICE_STYLE_DEGREE) != '1':
                style_open = f"<mstts:express-as style='{VOICE_STYLE}' styledegree='{VOICE_STYLE_DEGREE}'>"
            else:
                style_open = f"<mstts:express-as style='{VOICE_STYLE}'>"
            style_close = "</mstts:express-as>"
            ssml_text = ssml_text.replace("[EXPRESSION-OPEN]", style_open)
            ssml_text = ssml_text.replace("[EXPRESSION-CLOSE]", style_close)
        else:
            ssml_text = ssml_text.replace("[EXPRESSION-OPEN]", '')
            ssml_text = ssml_text.replace("[EXPRESSION-CLOSE]", '')
            
            speech_synthesis_result = speech_synthesizer.speak_ssml_async(
            ssml_text).get()

        if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            # print("Speech synthesized for text [Jorge]".format(text))
            pass
        elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_synthesis_result.cancellation_details
            print_system_output(get_system_text(
                '26', ' synthesize_to_speaker: '), cancellation_details.reason)
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    print_system_output(get_system_text(
                        '27'), cancellation_details.error_details)
                    print_system_output(get_system_text('28'))
    except Exception as e:
        print_system_output(get_system_text(
            '3', ' synthesize_to_speaker: '), e)


def synthesize_speech(text, output_filename):
    ssml_text = f"<speak><prosody rate='{SPEECH_RATE_INCREMENT}%'>{text}</prosody></speak>"
    if assistant_language == "en":
        voice_id = "Ruth"
    else:
        voice_id = "Lupe"
    try:
        polly = session.client('polly', region_name='us-east-1')
        response = polly.synthesize_speech(
            TextType='ssml',
            Text=ssml_text,
            OutputFormat='mp3',
            VoiceId=voice_id,
            Engine='neural'
        )
        with open(output_filename, 'wb') as f:
            f.write(response['AudioStream'].read())
    except Exception as e:
        print_system_output(get_system_text('3', ' synthesize_speech: '), e)


def play_audio(file):
    sound = pydub.AudioSegment.from_file(file, format="mp3")
    playback.play(sound)


def create_folders():
    # Obtener el directorio actual
    current_path = os.getcwd()

    # Obtiene la ruta de la carpeta
    audio_folder = os.path.join(current_path, 'audio')

    # Comprobar si la carpeta 'audio' existe
    if not os.path.exists(audio_folder):
        # Crea la carpeta 'audio'
        os.mkdir(audio_folder)

    # Obtiene la ruta de la carpeta
    cache_folder = os.path.join(current_path, 'cache')

    # Comprobar si la carpeta 'audio' existe
    if not os.path.exists(cache_folder):
        # Crea la carpeta 'audio'
        os.mkdir(cache_folder)


def print_and_play(message):
    if message is not None and message.strip() != '':
        print(f"{ASSISTANT_TEXT_COLOR}{get_system_text('4')}{message}{TEXT_MARKUP}")
        if (assistant_language == 'es' and SELECTED_SPANISH_ASSISTANT['voice_id'] == 'Lupe') or (assistant_language == 'en' and SELECTED_ENGLISH_ASSISTANT['voice_id'] == 'Ruth'):
            synthesize_speech(message, 'audio/response.mp3')
            play_audio('audio/response.mp3')
        else:
            synthesize_to_speaker(message)


def get_text_from_audio(audio, recognizer, awake=True):
    phrase = ''
    returning_phrase = ''
    if assistant_language == 'en':
        recognition_language = 'en-US'
    else:
        recognition_language = 'es-CO'
    try:
        textFromAudio = recognizer.recognize_google(
            audio, language=recognition_language)
        phrase = textFromAudio.lower()
        if phrase is not None and phrase.strip() != '':
            # if awake:
            print_user_output(f"{get_system_text('5')}{phrase}")

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
        print_and_play(get_system_text('6', ' get_text_from_audio: '))
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
        print_system_output(get_system_text('7', ': '), e)
        print_and_play(get_system_text('7'))

    return returning_phrase


def ptt_audio_to_text(awake=True):
    recognizer = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            # Inicializar audio vacío
            audio_frame_data = b''
            play_audio('audio/wake_detected.mp3')
            # Esperar a que el usuario presione la tecla PTT
            lock = True
            key_pressed = None
            while lock:
                for word in PUSH_TO_TALK_KEYS:
                    if keyboard.is_pressed(word):
                        key_pressed = word
                        lock = False
                        break
            while True:
                # Grabar audio en fragmentos de 0.3 segundos
                audio_chunk = recognizer.record(
                    source, duration=RECORD_INTERVAL)
                # Agregar el fragmento de audio al audio total
                audio_frame_data = audio_frame_data + audio_chunk.frame_data
                if not keyboard.is_pressed(key_pressed):
                    break

        audio = sr.AudioData(
            audio_frame_data, sample_rate=44100, sample_width=2)

        phrase = get_text_from_audio(audio, recognizer, awake)
        if phrase != '':
            break

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
    global input_mode
    global audio_capture_mode
    system_function = ''
    if any_word_of_list_in_phrase(EXIT_WORDS[assistant_language], phrase):
        if garbage_cleaned:
            restore_garbage()
        goodbye_phrase = get_random_phrase(
            FINISH_CHAT_PHRASES[assistant_language])
        print_and_play(goodbye_phrase)
        sys.exit(0)
    elif any_word_of_list_in_phrase(RESET_WORDS[assistant_language], phrase):
        system_function = FUNCTION_RESET

    elif any_word_of_list_in_phrase(CHANGE_INPUT_MODE_WORDS[assistant_language], phrase):
        system_function = FUNCTION_CHANGE_INPUT_MODE
        if input_mode == 'voice':
            change_input_mode_phrase = get_random_phrase(
                INPUT_MODE_CHANGED_PHRASES[assistant_language])
            input_mode = "text"
            # system_function = FUNCTION_RESET # Not necessary but recommended
        else:
            change_input_mode_phrase = get_random_phrase(
                INPUT_MODE_CHANGED_PHRASES[assistant_language])
            input_mode = "voice"
            # system_function = FUNCTION_RESET # Not necessary but recommended
        print_and_play(change_input_mode_phrase)
        print_system_output(f"{get_system_text('23')}{input_mode}")

    elif any_word_of_list_in_phrase(CHANGE_AUDIO_CAPTURE_MODE_WORDS[assistant_language], phrase):
        system_function = FUNCTION_CHANGE_AUDIO_CAPTURE_MODE
        if audio_capture_mode == 'listen':
            change_audio_capture_mode = get_random_phrase(
                AUDIO_CAPTURE_MODE_CHANGED_PHRASES[assistant_language])
            (change_audio_capture_mode)
            audio_capture_mode = "ppt"
            # system_function = FUNCTION_RESET # Not necessary but recommended
        else:
            change_audio_capture_mode = get_random_phrase(
                AUDIO_CAPTURE_MODE_CHANGED_PHRASES[assistant_language])
            audio_capture_mode = "listen"
            # system_function = FUNCTION_RESET # Not necessary but recommended
        print_and_play(change_audio_capture_mode)
        print_system_output(f"{get_system_text('25')}{audio_capture_mode}")

    elif any_word_of_list_in_phrase(CHANGE_LANGUAGE_WORDS[assistant_language], phrase):
        system_function = FUNCTION_RESET
        # system_function = FUNCTION_CHANGE_LANGUAGE
        if assistant_language == 'en':
            change_language_phrase = get_random_phrase(
                LANGUAGE_CHANGED_PHRASES[assistant_language])
            print_and_play(change_language_phrase)
            assistant_language = "es"
            print_system_output(get_system_text('24'))
        else:
            change_language_phrase = get_random_phrase(
                LANGUAGE_CHANGED_PHRASES[assistant_language])
            print_and_play(change_language_phrase)
            assistant_language = "en"
            print_system_output(get_system_text('24'))

    return system_function


def check_words_in_order_in_a_phrase(phrase1, phrase2):
    words_phrase1 = phrase1.split()
    words_phrase2 = phrase2.split()

    i = 0
    for palabra in words_phrase2:
        if i < len(words_phrase1) and palabra == words_phrase1[i]:
            i += 1

    return i == len(words_phrase1)


def check_a_list_of_words_in_order_in_phrases(phrase, list_of_list_of_words):
    for sentence in list_of_list_of_words:
        key_phrase = check_words_in_order_in_a_phrase(sentence, phrase)
        if key_phrase:
            return sentence
    return False


def wake_word_from_phrase(phrase):
    function_and_keyphrase = {
        "function": FUNCTION_ASSISTANT,
        "key_phrase": ''
    }
    system_function = system_functions_from_phrase(phrase)
    if system_function != '':
        if system_function == FUNCTION_RESET:
            function_and_keyphrase = {
                "function": FUNCTION_RESET,
                "key_phrase": ''
            }
        else:
            function_and_keyphrase = {
                "function": SYSTEM_TASK,
                "key_phrase": ''
            }
    elif any_word_of_list_in_phrase(BARD_WAKE_WORDS, phrase):
        function_and_keyphrase = {
            "function": BARD_ASSISTANT_NAME,
            "key_phrase": ''
        }
    elif any_word_of_list_in_phrase(GPT_WAKE_WORDS, phrase):
        function_and_keyphrase = {
            "function": GPT_ASSISTANT_NAME,
            "key_phrase": ''
        }
    elif any_word_of_list_in_phrase(BING_WAKE_WORDS, phrase):
        function_and_keyphrase = {
            "function": BING_ASSISTANT_NAME,
            "key_phrase": ''
        }
    else:  # Special functions
        key_phrase = check_a_list_of_words_in_order_in_phrases(
            phrase, YOUTUBE_KEYWORDS[assistant_language])
        if key_phrase:
            function_and_keyphrase = {
                "function": FUNCTION_YOUTUBE,
                "key_phrase": key_phrase
            }

        key_phrase = check_a_list_of_words_in_order_in_phrases(
            phrase, SPOTIFY_KEYWORDS[assistant_language])
        if key_phrase:
            function_and_keyphrase = {
                "function": FUNCTION_SPOTIFY,
                "key_phrase": key_phrase
            }

        key_phrase = check_a_list_of_words_in_order_in_phrases(
            phrase, WIKIPEDIA_KEYWORDS[assistant_language])
        if key_phrase:
            function_and_keyphrase = {
                "function": FUNCTION_WIKIPEDIA,
                "key_phrase": key_phrase
            }

        key_phrase = check_a_list_of_words_in_order_in_phrases(
            phrase, WOLFRAM_KEYWORDS[assistant_language])
        if key_phrase:
            function_and_keyphrase = {
                "function": FUNCTION_WOLFRAM,
                "key_phrase": key_phrase
            }

        key_phrase = check_a_list_of_words_in_order_in_phrases(
            phrase, WEB_KEYWORDS[assistant_language])
        if key_phrase:
            function_and_keyphrase = {
                "function": FUNCTION_WEB,
                "key_phrase": key_phrase
            }

        key_phrase = check_a_list_of_words_in_order_in_phrases(
            phrase, WHATSAPP_KEYWORDS[assistant_language])
        if key_phrase:
            function_and_keyphrase = {
                "function": FUNCTION_WHATSAPP,
                "key_phrase": key_phrase
            }

        key_phrase = check_a_list_of_words_in_order_in_phrases(
            phrase, DELETE_GARBAGE_KEYWORDS[assistant_language])
        if key_phrase:
            function_and_keyphrase = {
                "function": FUNCTION_DELETE_GARBAGE,
                "key_phrase": key_phrase
            }

        key_phrase = check_a_list_of_words_in_order_in_phrases(
            phrase, RESTORE_GARBAGE_KEYWORDS[assistant_language])
        if key_phrase:
            function_and_keyphrase = {
                "function": FUNCTION_RESTORE_GARBAGE,
                "key_phrase": key_phrase
            }

    return function_and_keyphrase


def run_script(script, shortcut_name, timeout, folder_name, show):
    script = script.replace("[SHORTCUT_NAME]", shortcut_name)
    script = script.replace("[FOLDER_NAME]", folder_name)
    script = script.replace("[TIMEOUT]", str(timeout))

    script_file = 'cache/temp_script.bat'
    try:
        with open(script_file, 'w') as file:
            file.write(script)
        script_path = os.path.abspath(script_file)

        if show:
            # Ejecutar el script de forma visible
            subprocess.call(
                ['start', 'cmd.exe', '/K', script_path], shell=True)
        else:
            # Ejecutar el script de forma invisible
            subprocess.run(script_path, stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, shell=True)
    except Exception as e:
        print_system_output(get_system_text('41', ' run_script: '), e)


def delete_garbage():
    timeout = 3
    run_script(DELETE_SCRIPT, "valorant", timeout, "trash", True)
    time.sleep(timeout * 3)
    run_script(DELETE_SCRIPT, "legend", timeout, "trash", True)


def restore_garbage():
    timeout = 0
    run_script(RESTORE_SCRIPT, "valorant", timeout, "trash", False)
    run_script(RESTORE_SCRIPT, "legend", timeout, "trash", False)


def simulate_deletion():
    global garbage_cleaned
    timeout = 2
    print_and_play(get_system_text('29'))
    time.sleep(timeout)
    print_and_play(get_system_text('30'))
    time.sleep(timeout)
    print_and_play(get_system_text('31'))
    time.sleep(timeout)
    print_and_play(get_system_text('32'))
    time.sleep(timeout)
    print_and_play(get_system_text('33'))
    time.sleep(timeout)
    delete_garbage_thread = threading.Thread(
        target=delete_garbage, daemon=True)
    delete_garbage_thread.start()
    print_and_play(get_system_text('34'))
    time.sleep(timeout)
    print_and_play(get_system_text('35'))
    time.sleep(timeout)
    print_and_play(get_system_text('36'))
    time.sleep(timeout)
    print_and_play(get_system_text('37'))
    time.sleep(timeout)
    delete_garbage_thread.join()
    print_and_play(get_system_text('38'))
    garbage_cleaned = True


def simulate_restoration():
    print_and_play(get_system_text('39'))
    restore_garbage()
    print_and_play(get_system_text('40'))


def cut_phrase_before_a_word(phrase, words_list):
    phrase_words = phrase.split()
    for word in words_list:
        if word in phrase_words:
            indice = phrase_words.index(word)
            if indice < len(phrase_words) - 1:
                return ' '.join(phrase_words[indice + 1:])

    return phrase


def open_url(url):
    try:
        webbrowser.open(url)
    except Exception as e:  # Search on Google
        pywhatkit.search(url)


def open_youtube(prompt, key_phrase):
    print_and_play(get_system_text('42'))
    youtube_search_prompt = get_user_input(True)
    print_and_play(get_system_text('43') +
                   youtube_search_prompt + get_system_text('44'))
    pywhatkit.playonyt(youtube_search_prompt)


def first_result_on_spotify(song_name):
    result = spotify.search(q=song_name, type='track', limit=1)
    items = result['tracks']['items']
    if len(items) > 0:
        url = items[0]['external_urls']['spotify']
        return 'spotify:' + url
    else:
        return False


def open_spotify(prompt, key_phrase):
    print_and_play(get_system_text('45'))
    spotify_search_prompt = get_user_input(True)
    url_song = first_result_on_spotify(spotify_search_prompt)
    if url_song:
        print_and_play(get_system_text('43') +
                       spotify_search_prompt + get_system_text('46'))
        open_url(url_song)
    else:
        print_and_play(get_system_text('47'))


def search_on_wikipedia(text):
    language = assistant_language
    success = False
    message = ''
    suggestion = None
    error = None
    try:
        wikipedia.set_lang(language)
        # Realizar la búsqueda en Wikipedia
        results = wikipedia.search(text)

        if len(results) == 0:
            message = get_system_text('47')
        else:
            # Obtener el primer resultado de la búsqueda
            first_result = results[0]

            try:
                # Obtener el artículo correspondiente al primer resultado
                page = wikipedia.page(first_result)

                # Obtener la URL del artículo
                url = page.url
                # Abrir el enlace en el navegador
                webbrowser.open(url)

                summary = wikipedia.summary(text, sentences=1)

                if summary and page:
                    success = True
                    message = re.sub(r'\[\d+\]', '', summary)
            except wikipedia.DisambiguationError as e:
                suggest = e.options
                if len(suggest) > 0:
                    first_suggestion = suggest[0]
                    suggestion = first_suggestion
                else:
                    message = get_system_text('47')
                    error = e
            except wikipedia.PageError as e:
                message = get_system_text('50')
                error = e
            except wikipedia.exceptions.HTTPTimeoutError as e:
                message = get_system_text('51')
                error = e
            except wikipedia.exceptions.RedirectError as e:
                message = get_system_text('52')
                error = e
            except TypeError as e:
                message = get_system_text('53')
                error = e
            except Exception as e:
                message = "Error: ", str(e)
                error = str(e)

    except wikipedia.exceptions.WikipediaException as e:
        message = get_system_text('54')
        error = e
    except Exception as e:
        message = "Error: ", str(e)
        error = str(e)

    func_return = {
        "success": success,
        "message": message,
        "error": error,
        "suggestion": suggestion
    }

    return func_return


def open_wikipedia(prompt, key_phrase):
    print_and_play(get_system_text('48'))
    wikipedia_search_prompt = get_user_input(True)
    result = search_on_wikipedia(wikipedia_search_prompt)
    if result["success"]:
        print_and_play(get_system_text('55') + result["message"])
    else:
        if result["suggestion"]:
            new_result = search_on_wikipedia(result["suggestion"])
            if new_result:
                print_and_play(get_system_text('55') + new_result["message"])
            else:
                print_and_play(get_system_text('47'))
        else:
            print_system_output("open_wikipedia: " + str(result["error"]))


def search_wolframalpha(prompt):
    success = False
    message = ''
    try:
        result = wolframClient.query(str(prompt))
        # Extraer la respuesta principal
        wolfram_response = next(result.results).text
        if wolfram_response:
            success = True
            message = wolfram_response
    except StopIteration as e:
        message = get_system_text('57')
        print_system_output(message + ' search_wolframalpha: ' + str(e))
    except wolframalpha.WolframAlphaError as e:
        message = get_system_text('58')
        print_and_play(get_system_text('58'))
        print_system_output(message + 'search_wolframalpha: ' + str(e))
    except Exception as e:
        print_system_output(message + 'search_wolframalpha: ' + str(e))

    returne_object = {
        "success": success,
        "message": message,
    }

    return returne_object


def open_wolfram(prompt, key_phrase):
    while True:
        print_and_play(get_system_text('59'))
        wolfram_search_prompt = get_user_input(True)
        if check_a_list_of_words_in_order_in_phrases(
                wolfram_search_prompt, EXIT_WOLFRAM_KEYWORDS[assistant_language]):
            break
        if assistant_language != 'en':
            wolfram_search_prompt = translate_text(
                wolfram_search_prompt, es_to_en=True)
        response = search_wolframalpha(wolfram_search_prompt)
        if response["success"]:
            if assistant_language != 'en':
                wolfram_response = wolfram_search_prompt = translate_text(
                    response["message"], es_to_en=False)
            wolfram_response = wolfram_response.replace(" |", ",")
            print_and_play(get_system_text('56') + wolfram_response)
            print_and_play(get_system_text('60'))
        else:
            print_and_play(response["message"] + ' ' + get_system_text('69'))


def open_web(prompt, key_phrase):
    print_and_play(get_system_text('61'))
    check_prompt = get_user_input(True)
    if any_word_of_list_in_phrase(["google"], check_prompt):
        print_and_play(get_system_text('62'))
        google_prompt = get_user_input(True)
        pywhatkit.search(google_prompt)
    else:
        print_and_play(get_system_text('63'))
        url = str(
            input(f"{USER_TEXT_COLOR}{get_system_text('5')}{TEXT_MARKUP}"))
        url = url.strip()
        open_url(url)


def send_whatsapp_message_script():
    time.sleep(3)

    keyboard.press('ctrl')
    keyboard.press('f')
    keyboard.release('f')
    keyboard.release('ctrl')

    keyboard.press('shift')
    for i in range(5):
        keyboard.press('tab')
        keyboard.release('tab')
    keyboard.release('shift')

    keyboard.press('enter')
    keyboard.release('enter')
    time.sleep(.2)

    keyboard.press('alt')
    keyboard.press('tab')
    time.sleep(.2)
    keyboard.release('tab')
    time.sleep(.2)
    keyboard.press('tab')
    time.sleep(.2)
    keyboard.release('tab')
    keyboard.release('alt')


def send_message_to_whatsapp(number, message):
    if message is not None and message != '':
        parsed_message = urllib.parse.quote(str(message))
        url = f"https://wa.me/57{number}?text={parsed_message}"

        webbrowser.open(url)
        send_whatsapp_message_script()


def open_whatsapp(prompt, key_phrase):
    while True:
        print_and_play(get_system_text('64'))
        phone_number = str(
            input(f"{USER_TEXT_COLOR}{get_system_text('5')}{TEXT_MARKUP}"))
        phone_number = phone_number.strip()
        phone_number = phone_number.replace(" ", "")
        if re.match(r'^\d+$', phone_number) is not None:
            break
        else:
            print_and_play(get_system_text('68'))
    print_and_play(get_system_text('65'))
    while True:
        user_prompt = get_user_input(True)
        if check_a_list_of_words_in_order_in_phrases(
                user_prompt, EXIT_WHATSAPP_KEYWORDS[assistant_language]):
            break
        print_and_play(get_system_text('66'))
        send_message_to_whatsapp(phone_number.strip(), user_prompt.strip())
        print_and_play(get_system_text('67'))


def execute_special_function(function, prompt, key_phrase):
    if function == FUNCTION_YOUTUBE:
        open_youtube(prompt, key_phrase)
    elif function == FUNCTION_SPOTIFY:
        open_spotify(prompt, key_phrase)
    elif function == FUNCTION_WIKIPEDIA:
        open_wikipedia(prompt, key_phrase)
    elif function == FUNCTION_WOLFRAM:
        open_wolfram(prompt, key_phrase)
    elif function == FUNCTION_WEB:
        open_web(prompt, key_phrase)
    elif function == FUNCTION_WHATSAPP:
        open_whatsapp(prompt, key_phrase)
    elif function == FUNCTION_DELETE_GARBAGE:
        simulate_deletion()
    elif function == FUNCTION_RESTORE_GARBAGE:
        simulate_restoration()


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


def cut_text(text):
    if len(text) > int(ASSISTANT_RESPONSE_LENGTH):
        i = int(ASSISTANT_RESPONSE_LENGTH)
        while i < len(text) and i < (int(ASSISTANT_RESPONSE_LENGTH) + int(RESPONSE_LENGTH_MARGIN)) and text[i] not in ('.', '!', '?', '\n'):
            i += 1
        cut_text = text[:i+1]
    else:
        cut_text = text
    return cut_text


async def get_bing_response(prompt, bing_bot):
    print_system_output(get_system_text('8'))
    initial_time = time.time()
    try:
        response = await bing_bot.ask(prompt=prompt, conversation_style=ConversationStyle.creative)
        final_time = time.time() - initial_time
        print_system_output(
            f"{get_system_text('9')}{round(final_time, 1)} {get_system_text('10')}")
        bot_response = clear_bing_text(response)
        bot_response = cut_text(bot_response)
        # await bing_bot.close()
    except Exception as e:
        print_system_output(get_system_text('11', ' get_bing_response: '), e)
        print_and_play(get_system_text('11'))
        return False
    return bot_response


def get_chatgpt_response(prompt, assistant_name, messages=None):
    response = None
    if messages is None:
        initial_context = GPT_INITIAL_CONTEXT[assistant_language].replace(
            "[ASSISTANT_NAME]", assistant_name)
        context = {"role": "system",
                   "content": initial_context}
        messages = [context]

    user_prompt = {"role": "user", "content": prompt}
    messages.append(user_prompt)

    print_system_output(get_system_text('12'))
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
        print_system_output(
            f"{get_system_text('13')}{round(final_time, 1)} {get_system_text('10')}")
    except Exception as e:
        print_system_output(get_system_text(
            '14', ' get_chatgpt_response: '), e)
        print_and_play(get_system_text('14'))

    if not response:
        return False
    bot_response = response["choices"][0]["message"]["content"]
    bot_response = cut_text(bot_response)

    messages.append({"role": "assistant", "content": bot_response})

    response = {
        "bot_response": bot_response,
        "messages": messages
    }

    return response


def get_bard_response(prompt, bard_bot):
    response = None
    print_system_output(get_system_text('15'))
    initial_time = time.time()
    if assistant_language != 'en':
        prompt = translate_text(prompt, es_to_en=True)
    try:
        if not prompt:
            return False
        response = bard_bot.ask(prompt)
    except Exception as e:
        print_system_output(get_system_text('16', ' get_bard_response: '), e)
        print_and_play(get_system_text('16'))
        return False
    if not response:
        return False
    bot_response = clear_text(response['content'])
    bot_response = cut_text(bot_response)
    if assistant_language != 'en':
        bot_response = translate_text(bot_response, es_to_en=False)
    if not bot_response:
        return False
    final_time = time.time() - initial_time
    print_system_output(
        f"{get_system_text('17')}{round(final_time, 1)} {get_system_text('10')}")
    return bot_response


def contextualize_bard(bard_bot, assistant_name):
    initial_context = BARD_INITIAL_CONTEXT.replace(
        "[ASSISTANT_NAME]", assistant_name)
    try:
        bard_bot.ask(initial_context)
    except Exception as e:
        pass


def get_user_input(awake):
    if input_mode == 'text':
        user_input = str(
            input(f"{USER_TEXT_COLOR}{get_system_text('5')}{TEXT_MARKUP}"))
        user_input = user_input.strip()
    else:
        if audio_capture_mode == 'listen':
            user_input = listen_audio_to_text(awake)
        else:
            user_input = ptt_audio_to_text(awake)

    return user_input


def get_wake_word(awake):
    while True:
        prompt = get_user_input(awake)

        function_and_keyphrase = wake_word_from_phrase(prompt)

        function = function_and_keyphrase["function"]

        if function != SYSTEM_TASK:
            if function == FUNCTION_RESET:
                function_and_prompt = {
                    "function": FUNCTION_RESET,
                    "prompt": ""
                }
                return function_and_prompt
            elif function == FUNCTION_YOUTUBE or function == FUNCTION_SPOTIFY or function == FUNCTION_WIKIPEDIA or function == FUNCTION_WOLFRAM or function == FUNCTION_WEB or function == FUNCTION_DELETE_GARBAGE or function == FUNCTION_RESTORE_GARBAGE or function == FUNCTION_WHATSAPP:
                execute_special_function(
                    function, prompt, function_and_keyphrase["key_phrase"])
                continue_phrase = get_random_phrase(
                    CONTINUE_CHAT_PHRASES[assistant_language])
                print_and_play(continue_phrase)
            elif not awake:
                if function == BARD_ASSISTANT_NAME or function == GPT_ASSISTANT_NAME or function == BING_ASSISTANT_NAME:
                    print_system_output(
                        f"{get_system_text('20')}{function}")
                    function_and_prompt = {
                        "function": function,
                        "prompt": ""
                    }
                    return function_and_prompt
                else:
                    not_wake_word_phrase = get_random_phrase(
                        NOT_WAKE_WORD_PHRASES[assistant_language])
                    print_and_play(not_wake_word_phrase)
            else:
                function_and_prompt = {
                    "function": FUNCTION_ASSISTANT,
                    "prompt": prompt
                }
                return function_and_prompt


async def start_binggpt():
    try:
        bing_bot = await Chatbot.create()
        return bing_bot
    except Exception as e:
        print_system_output("Bing GPT: " + str(e))
        return False


async def reset_binggpt(bing_bot):
    try:
        await bing_bot.reset()
    except Exception as e:
        print_system_output(get_system_text('21'))


def start_bard():
    try:
        bard_bot = BardBot(BARD_TOKEN)
        return bard_bot
    except Exception as e:
        return False



async def main():
    create_folders()

    while True:
        loading_phrase = get_random_phrase(LOADING_PHRASES[assistant_language])
        print_system_output(loading_phrase)
        assistant_name = get_assistant_name()

        # Bots initialization
        messages = None  # Chat GPT messages
        bing_bot = await start_binggpt()
        bard_bot = start_bard()
        bard_thread = threading.Thread(
            target=contextualize_bard, daemon=True, args=(bard_bot, assistant_name))
        bard_thread.start()
        
        if not bard_bot:
            print_system_output(get_system_text('22'))
        if not bing_bot:
            print_system_output(get_system_text('21'))

        welcome_phrase = get_random_phrase(WELCOME_PHRASES[assistant_language])
        parsed_welcome_phrase = welcome_phrase.replace(
            "{}", assistant_name)
        print_and_play(parsed_welcome_phrase)

        print_system_output(
            f"{get_system_text('19')}({BARD_ASSISTANT_NAME}: {BARD_WAKE_WORDS[0]}, {GPT_ASSISTANT_NAME}: {GPT_WAKE_WORDS[0]}, {BING_ASSISTANT_NAME}: {BING_WAKE_WORDS[0]})...")

        wake_word_and_prompt = get_wake_word(False)
        wake_word = wake_word_and_prompt["function"]
        if wake_word == FUNCTION_RESET:
            print_and_play(get_system_text('18'))
            continue

        activation_phrase = get_random_phrase(
            ACTIVATION_PHRASES[assistant_language])
        print_and_play(activation_phrase)

        while True:
            bot_response = None
            function_and_prompt = get_wake_word(True)
            function = function_and_prompt["function"]

            if function == FUNCTION_RESET:
                print_and_play(get_system_text('18'))
                break
            elif function == SYSTEM_TASK:
                continue
            else:
                prompt = function_and_prompt["prompt"]
                if wake_word == BING_ASSISTANT_NAME:
                    if bing_bot:
                        bot_response = await get_bing_response(prompt, bing_bot)
                    else:
                        print_and_play(get_system_text('21'))
                        continue
                elif wake_word == GPT_ASSISTANT_NAME:
                    response = get_chatgpt_response(
                        prompt, assistant_name, messages)
                    if response:
                        bot_response = response["bot_response"]
                        messages = response["messages"]
                elif wake_word == BARD_ASSISTANT_NAME:
                    if bard_bot:
                        bard_thread.join()
                        bot_response = get_bard_response(prompt, bard_bot)
                    else:
                        print_and_play(get_system_text('22'))
                        continue

            if not bot_response:
                break
            else:
                print_and_play(bot_response)
                if not any_word_of_list_in_phrase(["?", "¿"], bot_response):
                    continue_phrase = get_random_phrase(
                        CONTINUE_CHAT_PHRASES[assistant_language])
                    print_and_play(continue_phrase)
                if bing_bot:
                    await reset_binggpt(bing_bot)
if __name__ == "__main__":  # TODO: Rebuild project in multiple files
    asyncio.run(main())
