# Voice-Assistant with chat GPT

Este proyecto pretende crear un asistente que se activa a comandos de voz predeterminados, sintetiza el audio convirtiéndolo en texto usando la función 'Speech‑to‑Text' de la librería de Google y Azure Cognitive Services, lo procesa usando a elección del usuario uno de los tres modelos de lenguaje y generación de textos (Google Bard, ChaGPT o Bing+GPT), posteriormente recibe la respuesta del motor seleccionado en formato de texto, lo sintetiza nuevamente a audio usando la librería de AWS Polly, de Amazon, y Azure, de Microsoft dota al asistente de una voz femenina bastante pulida y orgánica y posteriormente se reproduce este audio, de tal manera que el usuario y el asistente puedan interactuar mediante voz de una forma ágil, cómoda, entretenida y eficaz. 

El asistente puede establecer conversaciones con el usuario sobre cualquier tema, tanto en inglés como en español, y además puede ejecutar tareas como reproducir vídeos en YouTube, música en Spotify, buscar en Wikipedia, abrir una página web, hacer una búsqueda en Googlé o en WolframAlpha, enviar mensajes por WhatsApp.

De igual manera el asistente es bastante personalizable, pudiendo el usuario cambiar parámetros como el idioma, la voz, la velocidad de habla, la entonación y la variación en la entonación, el nombre del asistente, el modo de captura de audio, el método de entrada, los diálogos, las teclas de en interacción, entre muchas otras cosas, y si bien el asistente está orientado principalmente a la interacción con voz, es posible también hacerlo mediante texto en un chat.

# Errores conocidos
1. Si inicias el asistente o terminas una charla y te demoras varios minutos en volver a hablarle y consultar con uno de los bots, es posible que dé un error de conexión.
Solución temporal: intentar hablarle de nuevo o reiniciar la conversación, bien sea por teclado o por input
2. Cuando cambias en modo de entrada de voz a texto, la consola se llena de espacios o caracteres, por lo que antes de enviarle el primer mensaje por input de texto.
Solución temporal: esto no afecta el funcionamiento del programa, sin embargo, puede reiniciar el chat o detener el programa, cambiar el parámetro DEFAULT_INPUT_MODE a 'text', guardar los cambios e iniciar nuevemente el programa.
3. A veces al iniciar el programa ouede ser que Bing GPT no esté disponible, este bot tiene una conexión muy mala.
Solución temporal: reiniciar el chat, detener el programa y volverlo a iniciar o ignorar el error y evitar usar Bing GPT como asistente

# Project set up
# 0. Set up env variables:
GPT_API_KEY="platform.openai.com/account/api-keys"
AWS_ACCESS_KEY_ID="us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/users/details/VoiceA?section=security_credentials"
AWS_SECRET_ACCESS_KEY="us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/users/details/VoiceA?section=security_credentials"
BARD_TOKEN="bard.google.com/" F12 → Application → Cookies → __Secure-1PSID
AZURE_SPEECH_API_KEY="portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/SpeechServices"
AZURE_SPEECH_REGION="portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/SpeechServices"
SPOTIFY_ID_CLIENT="developer.spotify.com/dashboard" Project name → Settings
SPOTIFY_CLIENT_SECRET="developer.spotify.com/dashboard" Project name → Settings
WOLFRAM_API_KEY="developer.wolframalpha.com/portal/myapps/"
# 1. Install Visual C++:
https://learn.microsoft.com/es-es/cpp/windows/latest-supported-vc-redist?view=msvc-170 (For Azure Cognitive Services)
# 2. Install Python:
https://www.python.org/downloads/
# 3. Install Chocolatey amd ffmpeg (Power shell as administrator)
1. Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
2. choco install ffmpeg
# 4. Set up venv
python -m venv venv
source venv/Scripts/activate
# 5. Install Python libraries:
python -m pip install --upgrade pip
python -m pip install -U pip wheel setuptools
pip install -r requirements.txt 
# 5. Run program
py main.py

 # Dev prompts
pipupgrade --verbose --latest --yes
pip list --outdated
deactivate
pip freeze > requirements.txt
poetry

# Usefull links
AWS Polly docs: boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#shared-credentials-file
Azure Cognitive Services docs: learn.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support?tabs=tts#voice-styles-and-roles
Azure voice gallery: speech.microsoft.com/portal/6c3ec7f356ae4cb1834fae1b565eb573/voicegallery
Azure speech studio: speech.microsoft.com/portal/6c3ec7f356ae4cb1834fae1b565eb573/audiocontentcreation/file?voiceId=77225261-11e8-4f00-92c5-ebd3cea15fa9&languageCode=es-BO