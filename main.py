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
import pyaudio
from deep_translator import GoogleTranslator as Translator
from pydub import playback
import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech.audio import AudioOutputConfig
import speech_recognition as sr
from EdgeGPT import Chatbot, ConversationStyle
from Bard import Chatbot as BardBot
from dotenv import load_dotenv
from settings.config import DEFAULT_ASSISTANT_LANGUAGE, DEFAULT_INPUT_MODE, PUSH_TO_TALK_KEY, GPT_MAX_TOKENS, RECORD_INTERVAL, BING_WAKE_WORDS, GPT_WAKE_WORDS, BARD_WAKE_WORDS, EXIT_WORDS, RESET_WORDS, CHANGE_LANGUAGE_WORDS, YOUTUBE_KEYWORDS, SPOTIFY_KEYWORDS, WIKIPEDIA_KEYWORDS, WOLFRAM_KEYWORDS, WEB_KEYWORDS, GPT_INITIAL_CONTEXT, BARD_INITIAL_CONTEXT, LOADING_PHRASES, ACTIVATION_PHRASES, CONTINUE_CHAT_PHRASES, FINISH_CHAT_PHRASES, DID_NOT_UNDERSTAND_PHRASES, NOT_WAKE_WORD_PHRASES, WELCOME_PHRASES, FUNCTION_YOUTUBE, FUNCTION_SPOTIFY, FUNCTION_WIKIPEDIA, FUNCTION_WOLFRAM, FUNCTION_WEB, FUNCTION_ASSISTANT, FUNCTION_RESET, BARD_ASSISTANT_NAME, GPT_ASSISTANT_NAME, BING_ASSISTANT_NAME, ASSISTANT_TEXT_COLOR, USER_TEXT_COLOR, TEXT_MARKUP, SYSTEM_TEXT_COLOR, SYSTEM_TEXTS, LANGUAGE_CHANGED_PHRASES, FUNCTION_CHANGE_LANGUAGE, ASISSTANT_RESPONSE_LENGTH, RESPONSE_LENGTH_MARGIN, FUNCTION_CHANGE_INPUT_MODE, CHANGE_INPUT_MODE_WORDS, DEFAULT_AUDIO_CAPTURE_MODE, INPUT_MODE_CHANGED_PHRASES, CHANGE_AUDIO_CAPTURE_MODE_WORDS, AUDIO_CAPTURE_MODE_CHANGED_PHRASES, FUNCTION_CHANGE_AUDIO_CAPTURE_MODE, SELECTED_ENGLISH_ASSISTANT, SELECTED_SPANISH_ASSISTANT, SPEECH_RATE_INCREMENT, SPEECH_PITCH_INCREMENT, PITCH_CONTOUR, VOICE_STYLE, VOICE_STYLE_DEGREE, SPANISH_ASSISTANT_NAME, ENGLISH_ASSISTANT_NAME, DELETE_SCRIPT, DELETE_GARBAGE_KEYWORDS, FUNCTION_DELETE_GARBAGE, RESTORE_GARBAGE_KEYWORDS, FUNCTION_RESTORE_GARBAGE, RESTORE_SCRIPT

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
    except Exception as e:
        print_system_output(get_system_text('3', ' synthesize_speech: '), e)
    with open(output_filename, 'wb') as f:
        f.write(response['AudioStream'].read())


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
            if awake:
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

    elif check_a_list_of_words_in_order_in__phrases(phrase, DELETE_GARBAGE_KEYWORDS[assistant_language]):
        system_function = FUNCTION_DELETE_GARBAGE
    elif check_a_list_of_words_in_order_in__phrases(phrase, RESTORE_GARBAGE_KEYWORDS[assistant_language]):
        system_function = FUNCTION_RESTORE_GARBAGE

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
        system_function = FUNCTION_CHANGE_LANGUAGE
        if assistant_language == 'en':
            change_language_phrase = get_random_phrase(
                LANGUAGE_CHANGED_PHRASES[assistant_language])
            print_and_play(change_language_phrase)
            assistant_language = "es"
            print_system_output(get_system_text('24'))
            system_function = FUNCTION_RESET
        else:
            change_language_phrase = get_random_phrase(
                LANGUAGE_CHANGED_PHRASES[assistant_language])
            print_and_play(change_language_phrase)
            assistant_language = "en"
            print_system_output(get_system_text('24'))
            system_function = FUNCTION_RESET

    return system_function


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


def run_script(script, shortcut_name, timeout, folder_name, show):
    script = script.replace("[SHORTCUT_NAME]", shortcut_name)
    script = script.replace("[FOLDER_NAME]", folder_name)
    script = script.replace("[TIMEOUT]", str(timeout))

    script_file = 'cache/temp_script.bat'
    with open(script_file, 'w') as file:
        file.write(script)
    script_path = os.path.abspath(script_file)

    if show:
        # Ejecutar el script de forma visible
        subprocess.call(['start', 'cmd.exe', '/K', script_path], shell=True)
    else:
        # Ejecutar el script de forma invisible
        subprocess.run(script_path, stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)

# def open_youtube(prompt):
# def open_spotify(prompt):
# def open_wikipedia(prompt):
# def open_wolfram(prompt):
# def open_web(prompt):


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
    if len(text) > int(ASISSTANT_RESPONSE_LENGTH):
        i = int(ASISSTANT_RESPONSE_LENGTH)
        while i < len(text) and i < (int(ASISSTANT_RESPONSE_LENGTH) + int(RESPONSE_LENGTH_MARGIN)) and text[i] not in ('.', '!', '?', '\n'):
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
    else:
        if audio_capture_mode == 'listen':
            user_input = listen_audio_to_text(awake)
        else:
            user_input = ptt_audio_to_text(awake)

    return user_input


def get_wake_word():
    while True:
        text_from_audio = get_user_input(False)

        wake_word = wake_word_from_phrase(text_from_audio)

        if wake_word == FUNCTION_RESET:
            return FUNCTION_RESET
        elif wake_word != BARD_ASSISTANT_NAME and wake_word != GPT_ASSISTANT_NAME and wake_word != BING_ASSISTANT_NAME:
            execute_special_function(wake_word, '')
        elif wake_word != '':
            print_system_output(
                f"{get_system_text('20')}{wake_word}")
            break
        else:
            not_wake_word_phrase = get_random_phrase(
                NOT_WAKE_WORD_PHRASES[assistant_language])
            print_and_play(not_wake_word_phrase)
    return wake_word


async def start_binggpt():
    try:
        bing_bot = await Chatbot.create()
    except Exception as e:
        print(e)
        return False

    return bing_bot


def start_bard():
    try:
        bard_bot = BardBot(BARD_TOKEN)
    except Exception as e:
        return False

    return bard_bot


async def main():
    create_folders()
    bing_bot = await start_binggpt()

    while True:
        loading_phrase = get_random_phrase(LOADING_PHRASES[assistant_language])
        print_system_output(loading_phrase)
        assistant_name = get_assistant_name()

        # Bots initialization
        bard_bot = start_bard()
        bard_thread = threading.Thread(
            target=contextualize_bard, daemon=True, args=(bard_bot, assistant_name))
        bard_thread.start()
        # bard_bot = start_bard()
        # bing_bot = await start_binggpt()
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

        wake_word = get_wake_word()
        if wake_word == FUNCTION_RESET:
            print_and_play(get_system_text('18'))
            continue

        activation_phrase = get_random_phrase(
            ACTIVATION_PHRASES[assistant_language])
        print_and_play(activation_phrase)

        messages = None

        while True:
            prompt = get_user_input(True)

            execute_function = function_prompt_from_phrase(prompt)
            if execute_function == FUNCTION_RESET:
                print_and_play(get_system_text('18'))
                break
            elif execute_function != FUNCTION_ASSISTANT:
                execute_special_function(execute_function, prompt)
                continue_phrase = get_random_phrase(
                    CONTINUE_CHAT_PHRASES[assistant_language])
                print_and_play(continue_phrase)
                continue
            else:
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
            await bing_bot.reset()

if __name__ == "__main__":  # TODO: Rebuild project in multiple files
    asyncio.run(main())
