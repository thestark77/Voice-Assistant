# Voice-Assistant with chat GPT

Este es un asistente de voz de Python que se activa a comandos de voz predeterminados, sintetiza el audio convirtiéndolo en texto, lo procesa usando la API de ChaGPT o EdgeGPT para usar GPT mediante Bing, posteriormente convierte el texto a voz usando la librería de speech_recognition que utiliza la API de Google y posteriormente se reproduce este audio, de tal manera que el usuario y el asistente puedan interactuar mediante voz, dicha voz está sintetizada usando la librería de AWS Polly, de Amazon, que dota al asistente de una voz femenina bastante pulida y orgánica.

# .env file
GPT_API_KEY="PASTE_IT HERE"
AWS_ACCESS_KEY_ID="PASTE_IT HERE"
AWS_SECRET_ACCESS_KEY="PASTE_IT HERE"

# Commands
pip install -r requirements.txt

py -m pip install EdgeGPT --upgrade
python.exe -m pip install --upgrade pip
pip install git+https://github.com/openai/whisper.git 
pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))    (ON PS administrator)
choco install ffmpeg (Power shell as administrator)
pip install SpeechRecognition
pip install boto3
pip install pydub
pip install openai
pip install ffmpeg-python