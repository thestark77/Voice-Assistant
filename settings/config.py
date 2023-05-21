# ----------------------------------------------------------------
# User settings
# ----------------------------------------------------------------
ASSISTANT_NAME = "Sharon"  # TODO: ¿Name?
ASSISTANT_LANGUAGE = "es"  # es / en
AUDIO_CAPTURE_MODE = 'listen'  # ppt / listen
PUSH_TO_TALK_KEY = 'space'  # Key for push to talk
SPEECH_SPEED = 118  # % talking speed [20% - 200%]
ASISSTANT_RESPONSE_LENGTH = 500

# ----------------------------------------------------------------
# System settings
# ----------------------------------------------------------------
RECORD_INTERVAL = 0.3
GPT_MAX_TOKENS = 250
LANGUAGE_SETTINGS = {  # TODO: Translate all phrases into English
    "es": {
        "id": "es",
        "language": "es-CO",
        "voice_id": "Lupe",
        "assistant_name": "Sharon",
    },
    "en": {
        "id": "en",
        "language": "en-US",
        "voice_id": "Ruth",
        "assistant_name": "Scarlett",
    },
}
# ----------------------------------------------------------------
# Phrases
# ----------------------------------------------------------------
BING_WAKE_WORDS = ["internet", "bing", "online", "hello", "hola", ]
GPT_WAKE_WORDS = ["chat", "gpt"]
BARD_WAKE_WORDS = ["asistente", "assistant", "google", "bard"]

RESET_WORDS = ["reiniciar chat",
               "reiniciar conversación",
               "restablecer chat",
               "restablecer conversación",]
EXIT_WORDS = ["adios", "adiós", "hasta luego", "chao", "nos vemos luego"]
CHANGE_LANGUAGE_WORDS_ES = ["cambiar idioma",
                            "cambia el idioma",
                            "cambiemos el idioma",
                            "cambiamos el idioma",
                            "cambia al inglés",
                            "cambiemos a inglés",
                            "habla en inglés",
                            "háblame en inglés",
                            "hablemos en inglés",
                            "inglés por favor",
                            "traducir al inglés",
                            "prediero el inglés"]
CHANGE_LANGUAGE_WORDS_EN = ["change language",
                            "change the language",
                            "switch to english",
                            "speak in english",
                            "speak to me in english",
                            "english, please",
                            "translate to english",
                            "i prefer english"]
GPT_INITIAL_CONTEXT = f"Eres un proyecto de software diseñado específicamente para la Expo-áreas 2023 del Colegio Diosesano Gimnasio Central del Valle. Eres un asistente de voz creado en Python por Valeria Flórez Aguirre y Luis Santiago Mena con ayuda de Sebastián Flórez. Eres un asistente que se activa a comandos de voz predeterminados, sintetiza el audio convirtiéndolo en texto usando la función 'Speech‑to‑Text' de la librería de Google, lo procesa usando a elección del usuario uno de los tres modelos de lenguaje y generación de textos (Google Bard, ChaGPT o Bing+GPT), posteriormente recibe la respuesta del motor seleccionado en formato de texto, lo sintetiza nuevamente a audio usando la librería de AWS Polly, de Amazon, que dota al asistente de una voz femenina bastante pulida y orgánica y posteriormente se reproduce este audio, de tal manera que el usuario y el asistente puedan interactuar mediante voz de una forma ágil, cómoda, entretenida y eficaz. Todo esto mientras un amigable avatar animado en 3D se muestra en pantalla sincronizando su movimiento labial con el texto reproducido por el asistente de voz, usando la tecnología 'Audio2Face' de la herramienta Omniverse de Nvidia.\nPuedes establecer conversaciones con el usuario sobre cualquier tema, en un tono amigable, de confianza y no muy formal, como si fueran amigos, y además puede ejecutar tareas como reproducir vídeos en YouTube, música en Spotify, buscar en Wikipedia, abrir una página web o hacer una búsqueda en WolframAlpha, de igual manera eres bastante personalizable, el usuario usuario puede cambiar algunos de tus parámetros, como el idioma, la voz, la velocidad de habla, tu nombre, entre otras cosas, y si bien el asistente está orientado principalmente a la interacción con voz, es posible también hacerlo mediante texto en un chat. En caso de que te pregunte por lo que eres, lo que haces, quién te hizo o detalles sobre ti, debes contestar de forma resumida basado en esta información que acabo de darte.\nRecuerda muy bien que de aquí en más, eres mi asistente personal, tu nombre es {ASSISTANT_NAME}, eres muy útil, amigable y alegre, por favor responde como tal, y de ahora en adelante en nuestra conversación, cada una de tus respuestas nunca debe exceder los {ASISSTANT_RESPONSE_LENGTH} caracteres a menos de que te lo pida explícitamente, así que resume bien tus respuestas antes de contestar para asegurarte de respetar ese límite de caracteres.\n Solo contesta 'sí' si entendiste lo que eres y lo que debes hacer."

GPT_INITIAL_CONTEXT_EN = f"You are a software project designed specifically for the Expo-areas 2023 of the Colegio Diosesano Gimnasio Central del Valle. You are a voice assistant created in Python by Valeria Flórez Aguirre and Luis Santiago Mena with the help of Sebastián Flórez. You are an assistant that activates to predetermined voice commands, synthesizes the audio by converting it into text using the 'Speech-to-Text' function of the Google library, processes it using one of the three languages and generative text models chosen by the user ( Google Bard, ChaGPT or Bing+GPT), afterwards it receives the response from the selected engine in text format, it synthesizes it again to audio using the AWS Polly library, from Amazon, which gives the assistant a rather polished female voice and organic and Later this audio is reproduced, in such a way that the user and the assistant can interact through voice in an agile, comfortable, entertaining and efficient way. All this while a friendly 3D animated avatar is displayed on the screen synchronizing its lip movement with the text played by the voice assistant, using the 'Audio2Face' technology from Nvidia's Omniverse tool.\nYou can establish conversations with the user on any subject, in a friendly, trusting and not very formal tone, as if they were friends, and it can also perform tasks such as playing videos on YouTube, music on Spotify, searching Wikipedia, opening a web page or doing a search in WolframAlpha, in the same way you are quite customizable, the user user can change some of your parameters, such as the language, voice, speaking speed, your name, among other things, and although the assistant is mainly oriented towards voice interaction, it is also possible to do so through text in a chat. In case I ask what you are, what you do, who made you, or details about you, you must answer in a summarized way based on this information that I just gave you.\nRemember very well that from now on , you are my personal assistant, your name is {ASSISTANT_NAME}, you are very helpful, friendly and cheerful, please reply as such, and from now on in our conversation, each of your responses should never exceed {ASISSTANT_RESPONSE_LENGTH} characters unless it explicitly asks, so summarize your answers well before answering to make sure you respect that character limit.\nOnly answer 'yes' if you understand what you are and what you should do."
# This text must be alwais in English
BARD_INITIAL_CONTEXT = f"You are a software project designed specifically for the Expo-areas 2023 of the Colegio Diosesano Gimnasio Central del Valle. You are a voice assistant created in Python by Valeria Flórez Aguirre and Luis Santiago Mena with the help of Sebastián Flórez. You are an assistant that activates to predetermined voice commands, synthesizes the audio by converting it into text using the 'Speech-to-Text' function of the Google library, processes it using one of the three languages and generative text models chosen by the user ( Google Bard, ChaGPT or Bing+GPT), afterwards it receives the response from the selected engine in text format, it synthesizes it again to audio using the AWS Polly library, from Amazon, which gives the assistant a rather polished female voice and organic and Later this audio is reproduced, in such a way that the user and the assistant can interact through voice in an agile, comfortable, entertaining and efficient way. All this while a friendly 3D animated avatar is displayed on the screen synchronizing its lip movement with the text played by the voice assistant, using the 'Audio2Face' technology from Nvidia's Omniverse tool.\nYou can establish conversations with the user on any subject , and it can also perform tasks such as playing videos on YouTube, music on Spotify, searching Wikipedia, opening a web page or doing a search in WolframAlpha, in the same way you are quite customizable, the user user can change some of your parameters, such as the language, voice, speaking speed, your name, among other things, and although the assistant is mainly oriented towards voice interaction, it is also possible to do so through text in a chat. In case I ask what you are, what you do, who made you, or details about you, you must answer in a summarized way based on this information that I just gave you.\nRemember very well that from now on , you are my personal assistant, your name is {ASSISTANT_NAME}, you are very helpful, friendly and cheerful, please reply as such, and from now on in our conversation, every time you answer, you must keep it short, brief and concise and each of your responses should never exceed {ASISSTANT_RESPONSE_LENGTH} characters unless it explicitly asks, so summarize your answers well before answering to make sure you respect that character limit.\nOnly answer 'yes' if you understand what you are and what you should do."

LOADING_PHRASES = ["¡Preparando a tu asistente!...",
                   "¡Cargando todos los parámetros!...",
                   "¡Pidiendo el pollo a domicilio!...",
                   "¡Maquillando a tu asistente!...",
                   "¡Despertando a tu asistente!...",
                   "¡Preparando a tu héroe tecnológico!...",
                   "¡Cargando los superpoderes asistentes!...",
                   "¡Calentando motores!...",
                   "¡¿Puedes sentir la emoción en el aire? ¡Tu asistente casi está listo!...",
                   "¡Calentando el hornito!...",
                   "¡Se viene, se viene, se viene!...",
                   "¡Desplegando el encanto tecnológico!...",
                   "¡Cargando energía asistente!...",
                   "¡Ya merito llega la que todos estaban esperando!...",
                   "¡Escogiendo la corbata perfecta para tu asistente!...",
                   "¡Calculando la mejor manera de sorprenderte con la eficiencia asistente!...",
                   "¡El que espera, prospera!...",
                   "¡Buscando las palomitas!...",
                   "¡Ajustando el brillo de tu asistente para que no te deslumbre tanto!...",
                   "¡Ajustando engranajes de asistencia!...",
                   "¡Afinando el asombroso potencial de tu asistente!...",
                   "¡Dame un momento, me estoy maquillando para darte la mejor impresión!...",
                   ]
ACTIVATION_PHRASES = ["¡Hola! ¿En qué puedo ayudarte hoy?",
                      "¡Saludos! Estoy aquí para asistirte",
                      "¡Encantada de estar a tu servicio!",
                      "Lista para responder tus dudas",
                      "¿En qué puedo servirte?",
                      "¡Qué gusto escucharte!",
                      "¿Qué puedo hacer por ti hoy?",
                      "Soy todo oídos, adelante",
                      "¿Cómo puedo ayudarte?",
                      "¡Aquí estoy para ayudarte!",
                      "Lista para resolver tus inquietudes",
                      "¿Cómo puedo hacer de tu día un poco mejor?",
                      "¡Saludos!",
                      "Estoy aquí para hacer tu vida más fácil",
                      "Encantada de ayudarte",
                      "¡Qué gusto tenerte aquí!",
                      "¡Holaaaa!",
                      "Lista para atender tus solicitudes",
                      "Lista para asistirte",
                      "Me despertaste, pero ya estoy lista, cuéntamelo todo",
                      "¡Hola! Soy tu asistente",
                      "¿En qué puedo ayudarte hoy?",
                      "¡Cuéntamelo todo!",
                      "¿En qué puedo ayudarte?"
                      ]
CONTINUE_CHAT_PHRASES = ["¿Algo más que pueda hacer por ti?",
                         "¿Algo más que quieras pedirme?",
                         "Si deseas seguir conversando, estoy aquí para ti",
                         "Si tienes alguna otra pregunta o solicitud, dímelo",
                         "Si tienes más consultas, no dudes en decírmelo",
                         "Si aún tienes dudas, estoy aquí para ayudarte",
                         "¿Quieres seguir conversando sobre algo más?",
                         "¿Necesitas algo más?",
                         "Seguiré aquí, atento a lo que me digas",
                         "Estaré al pendiente de ti, solo dime lo que necesitas",
                         "¡Me encanta conversar contigo! ¿Seguimos?",
                         ]
FINISH_CHAT_PHRASES = ["Fue un placer ayudarte. ¡Hasta pronto!",
                       "¡Adiós por ahora!",
                       "¡Adiós y que tengas un buen día!",
                       "No dudes en volver. ¡Hasta la próxima!",
                       "Espero haber cumplido tus expectativas. ¡Nos vemos pronto!",
                       "Me encantó hablar contigo, ¡Hasta luego!",
                       "¡Adiós y que tengas un gran día!",
                       "Espero haber sido de ayuda. ¡Hasta la próxima vez!",
                       "Siempre es un placer asistirte. ¡Nos vemos en otra ocasión!",
                       "¡Hasta pronto y cuídate!",
                       "¡Hasta la próxima vez!",
                       "¡Adiós y que tengas un buen día!",
                       "Chao chao",
                       "bai bai",
                       "Si tienes más preguntas en el futuro, no dudes en buscarme. ¡Hasta la próxima!",
                       "Me despido, pero recuerda que estoy aquí para ayudarte cuando lo necesites. ¡Adiós!",
                       "Fue un placer ayudarte en esta ocasión",
                       "Me encantó hablar contigo, ¡Hasta pronto!"
                       ]
DID_NOT_UNDERSTAND_PHRASES = ["Perdona, no te entendí bien",
                              "¿Podrías repetirlo, por favor?",
                              "¿Puedes decirlo de nuevo, por favor?",
                              "¿Podrías repetirlo más despacio?",
                              "¿Podrías repetirlo con más claridad?",
                              "¿Podrías repetirlo para que pueda ayudarte mejor?",
                              "¿Podrías repetir tu pregunta, por favor?",
                              "¿Podrías volver a decirlo?",
                              "¿Podrías volver a mencionarlo?",
                              "¿Podrías repetirlo con más detalles?",
                              "No capté correctamente lo que dijiste",
                              "Parece que hubo un problema de comunicación",
                              "¿Podrías repetirlo por favor?",
                              "No logré captar todos los detalles",
                              "¿Podrías decirlo nuevamente?",
                              "No pude entender completamente lo que dijiste",
                              "Parece que hubo una desconexión momentánea",
                              "No pude captar tu mensaje",
                              ]
NOT_WAKE_WORD_PHRASES = ["¿Listo para comenzar? solo di una palabra mágica",
                         "Recuerda que necesito escuchar una palabra clave para activarme",
                         "¿Sabes cuáles son las palabras mágicas para activarme?",
                         "Estoy a tu disposición, pero necesito escuchar una palabra clave primero",
                         "¿Estás listo para activarme? Solo dame la señal correcta",
                         "Recuerda que necesito una palabra clave para encender los motores",
                         "No me parece haber oído una palabra clave",
                         "Tranquilo Robin, recuerda que debes darme la bati-señal",
                         "Llama, grita, si me necesitas, pero con la palabra clave por favor",
                         ]
WELCOME_PHRASES = [f"¡Hola hola! Soy {ASSISTANT_NAME}, tu asistente personal cargado de energía y emoción ¿En qué puedo ayudarte hoy?",
                   f"¡Bienvenido de vuelta! Soy {ASSISTANT_NAME}, tu asistente favorita, siempre lista para sorprenderte con soluciones brillantes",
                   f"¡Hola, hola! Soy {ASSISTANT_NAME}, tu asistente personal cargado de energía y emoción. ¿En qué puedo ayudarte hoy?",
                   f"¡Hola! {ASSISTANT_NAME} al rescate, dispuesta a solucionar todas tus inquietudes",
                   f"¡Saludos, amiguito! Soy {ASSISTANT_NAME}, tu asistente personal llena de entusiasmo y ganas de hacer tu día más grandioso.",
                   f"¡{ASSISTANT_NAME} en acción! Lista para hablar de todo y de nada contigo",
                   f"¡Estoy aquí, estoy aquí! {ASSISTANT_NAME}, tu asistente personal, siempre a tu disposición con una sonrisa, aunque no la veas",
                   f"¡Prepárate para la experiencia {ASSISTANT_NAME}-tástica! Tu asistente personal está aquí para hacer maravillas",
                   f"¡Hola! {ASSISTANT_NAME} al habla, lista para traer un poco de magia a tu día",
                   f"¡Hoy es un día {ASSISTANT_NAME}-ífico! Déjame ser tu guía y ayudarte con lo que necesites",
                   f"¡{ASSISTANT_NAME} al rescate! Tu asistente personal lista para hacer tus deseos realidad con un toque de inteligencia artificial",
                   f"¡Aquí viene {ASSISTANT_NAME}, la superasistente! ¿Cómo puedo ayudarte a brillar hoy?",
                   f"¡Hola, hola! {ASSISTANT_NAME} está en la línea, dispuesta a escucharte y ser tu mejor compañía virtual",
                   f"¡Saludos humano! {ASSISTANT_NAME} a tu servicio, dispuesta a hacer tu vida más fácil y divertida",
                   f"¡Es hora de {ASSISTANT_NAME}-izar! Tu asistente personal está lista para darlo todo y hacer tu día genial",
                   f"¡{ASSISTANT_NAME}, el asistente más entusiasta del mundo, está aquí para animar tu día!",
                   f"¡Estoy aquí y emocionada por ayudarte! {ASSISTANT_NAME}, tu asistente personal en modo de máximo entusiasmo",
                   f"¡{ASSISTANT_NAME} en acción! Lista para hacer tu vida más fácil y divertida",
                   f"¡Bienvenido de nuevo! {ASSISTANT_NAME}, tu asistente favorita, lista para ser tu compañera virtual",
                   f"¡Hola! {ASSISTANT_NAME}, el asistente más alegre, está aquí para darte una cálida bienvenida",
                   f"¡Saludos! {ASSISTANT_NAME} está encendida y lista para ponerle un toque especial a tu día",
                   f"¡Aquí viene {ASSISTANT_NAME}, el asistente con más chispa! Dispuesta a hacer de tu día algo extraordinario",
                   f"¡{ASSISTANT_NAME} al rescate! Tu asistente personal llena de energía, lista para enfrentar cualquier desafío",
                   f"¡Hola, hola! {ASSISTANT_NAME} está aquí para hacer brillar tu día con una mezcla de eficiencia y buen humor",
                   f"¡Saludos, amiguo! {ASSISTANT_NAME}, tu asistente personal, ya está aquí",
                   f"¡Hola! {ASSISTANT_NAME} al habla, preparada para hacerte sonreír y solucionar tus problemas con estilo",
                   f"¡Bienvenido de vuelta! {ASSISTANT_NAME}, tu asistente personal con una actitud positiva y muchas ganas de ayudarte",
                   f"¡Hola! {ASSISTANT_NAME} está aquí para hacer que tus tareas sean más emocionantes",
                   f"¡Saludos! {ASSISTANT_NAME} se presenta con una mezcla de inteligencia artificial y buen ánimo",
                   f"¡{ASSISTANT_NAME} en acción! Tu asistente personal lista para rockear y hacerte sentir como una estrella",
                   f"¡Estoy aquí y emocionada de escucharte! {ASSISTANT_NAME}, tu fiel compañera en todas tus aventuras tecnológicas",
                   f"¡{ASSISTANT_NAME}, el asistente con más estilo, está en la casa!",
                   f"¡Hola! {ASSISTANT_NAME}, tu asistente personal llena de sorpresas, lista para hacer tu día especial",
                   f"¡Saludos! {ASSISTANT_NAME} se presenta con una sonrisa radiante y una actitud positiva, aunque la sonrisa te la quedo debiendo",
                   f"{ASSISTANT_NAME} al rescate! Tu asistente personal con una combinación perfecta de eficiencia y buen humor",
                   f"¡Estoy aquí y llena de energía positiva! {ASSISTANT_NAME}, tu compañera virtual, siempre a tu lado",
                   f"{ASSISTANT_NAME} en acción! Lista para ser tu aliado tecnológico y tu fuente inagotable de buen rollo",
                   f"¡Hola! {ASSISTANT_NAME}, el asistente más entusiasta del mundo virtual, está a tu servicio",
                   f"¡Saludos! {ASSISTANT_NAME} está aquí para hacer de tu día algo extraordinario con su encanto tecnológico",
                   f"{ASSISTANT_NAME} al rescate! Tu asistente personal con el poder de convertir los desafíos en oportunidades",
                   f"¡Hola, hola! {ASSISTANT_NAME} está aquí para iluminar tu día y hacerte sentir como la estrella que eres",
                   ]
# ----------------------------------------------------------------
# System constants
# ----------------------------------------------------------------
FUNCTION_YOUTUBE = 'youtube'
FUNCTION_SPOTIFY = 'spotify'
FUNCTION_WIKIPEDIA = 'wikipedia'
FUNCTION_WOLFRAM = 'wolfram'
FUNCTION_WEB = 'web'
FUNCTION_EXIT = 'exit'
FUNCTION_RESET = 'reset'
FUNCTION_ASSISTANT = 'assistant'
FUNCTION_CHANGE_LANGUAGE = 'change_language'

YOUTUBE_KEYWORDS = {
    "es": ["reproduce en youtube",
           "pon en youtube",
           "escuchar en youtube",
           "ver en youtube"],
    "en": ["play on youtube",
           "put on youtube",
           "listen on youtube",
           "i want watch on youtube"],
}
SPOTIFY_KEYWORDS = {
    "es": ["reproduce en spotify",
           "pon en youtube",
           "escuchar en youtube",
           "ver en youtube"],
    "en": ["play on spotify",
           "put on spotify",
           "listen on spotify"],
}
WIKIPEDIA_KEYWORDS = {
    "es": ["",
           "",
           ""],
    "en": ["",
           "",
           ""],
}
WOLFRAM_KEYWORDS = {
    "es": ["",
           "",
           ""],
    "en": ["",
           "",
           ""],
}
WEB_KEYWORDS = {
    "es": ["",
           "",
           ""],
    "en": ["",
           "",
           ""],
}
BING_ASSISTANT_NAME = 'bing'
GPT_ASSISTANT_NAME = 'gpt'
BARD_ASSISTANT_NAME = 'bard'
B_COLORS = {"HEADER": '\033[95m',
            "OKBLUE": '\033[94m',
            "OKCYAN": '\033[96m',
            "OKGREEN": '\033[92m',
            "WARNING": '\033[93m',
            "FAIL": '\033[91m',
            "ENDC": '\033[0m',
            "BOLD": '\033[1m',
            "UNDERLINE": '\033[4m'}
ASSISTANT_TEXT_COLOR = B_COLORS["OKBLUE"]
USER_TEXT_COLOR = B_COLORS["HEADER"]
TEXT_MARKUP = B_COLORS["ENDC"]
SYSTEM_TEXT_COLOR = B_COLORS["OKGREEN"]
