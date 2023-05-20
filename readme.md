# Voice-Assistant with chat GPT

Este proyecto pretende crear un asistente de voz de Python que se activa a comandos de voz predeterminados, sintetiza el audio convirtiéndolo en texto usando la función "Speech‑to‑Text" de la librería de Google, lo procesa usando a elección del usuario uno de los tres modelos de lenguaje y generación de textos (Google Bard, ChaGPT o Bing+GPT), posteriormente recibe la respuesta del motor seleccionado en formato de texto, lo sintetiza nuevamente a audio usando la librería de AWS Polly, de Amazon, que dota al asistente de una voz femenina bastante pulida y orgánica y posteriormente se reproduce este audio, de tal manera que el usuario y el asistente puedan interactuar mediante voz de una forma ágil, cómoda, entretenida y eficaz. Todo esto mientras un amigable avatar animado en 3D se muestra en pantalla sincronizando su movimiento labial con el texto reproducido por el asistente de voz, usando la tecnología "Audio2Face" de la herramienta Omniverse de Nvidia.

El asistente puede establecer conversaciones con el usuario sobre cualquier tema, y además puede ejecutar tareas como reproducir vídeos en youtube, música en Spotify, buscar en Wikipedia, abrir una página web o hacer una búsqueda en WolframAlpha, de igual manera el asistente es bastante personalizable, pudiendo el usuario cambiar parámetros como el idioma, la voz, la velocidad de habla, el nombre del asistente, entre otras cosas, y si bien el asistente está orientado princpalmente a la interacción con voz, es posible también hacerlo mediante texto mediante un chat.

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
https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#shared-credentials-file
https://us-east-1.console.aws.amazon.com/iamv2/home#/users/details/VoiceA?section=permissions


pipupgrade --verbose --latest --yes
python -m venv venv
source venv/Scripts/activate
python -m pip install -U pip wheel setuptools
pip list
pip install -r requirements.txt 
deactivate
poetry

pip install granslate