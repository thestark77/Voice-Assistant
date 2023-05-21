# ----------------------------------------------------------------
# User settings
# ----------------------------------------------------------------
SPANISH_ASSISTANT_NAME = "Sharon"  # You can change the name
ENGLISH_ASSISTANT_NAME = "Scarlett"  # You can change the name
DEFAULT_ASSISTANT_LANGUAGE = "es"  # es / en
AUDIO_CAPTURE_MODE = 'ppt'  # ppt / listen
PUSH_TO_TALK_KEY = 'space'  # Key for push to talk
INPUT_MODE = 'voice'  # voice / text
SPEECH_SPEED = 118  # % talking speed [20% - 200%]
ASISSTANT_RESPONSE_LENGTH = 500

# ----------------------------------------------------------------
# System settings
# ----------------------------------------------------------------
GPT_MAX_TOKENS = 250
RECORD_INTERVAL = 0.3
LANGUAGE_SETTINGS = {
    "es": {
        "id": "es",
        "language": "es-CO",
        "voice_id": "Lupe",
        "assistant_name": SPANISH_ASSISTANT_NAME,
    },
    "en": {
        "id": "en",
        "language": "en-US",
        "voice_id": "Ruth",
        "assistant_name": ENGLISH_ASSISTANT_NAME,
    },
}

# ----------------------------------------------------------------
# Keywords
# ----------------------------------------------------------------
BING_WAKE_WORDS = ["internet", "bing", "online", "hello", "hola", ]
GPT_WAKE_WORDS = ["chat", "gpt"]
BARD_WAKE_WORDS = ["asistente", "assistant", "google", "bard"]

EXIT_WORDS = {
    "es": ["adios", "adiós", "hasta luego", "chao", "nos vemos luego"],
    "en": ["bye", "see you later", "cheerio"],
}
RESET_WORDS = {
    "es": ["reiniciar chat",
           "reiniciar conversación",
           "restablecer chat",
           "restablecer conversación",],
    "en": ["restart chat",
           "restart conversation",
           "reboot chat",
           "reboot conversation",
           "restore chat",
           "restore conversation",]
}
CHANGE_LANGUAGE_WORDS = {
    "es": ["cambiar idioma",
           "cambia el idioma",
           "cambia el lenguaje",
           "cambiemos el idioma",
           "cambiemos el lenguaje",
           "cambiamos el idioma",
           "cambiamos el lenguaje",
           "cambia al inglés",
           "cambiemos a inglés",
           "habla en inglés",
           "háblame en inglés",
           "hablemos en inglés",
           "inglés por favor",
           "traducir al inglés",
           "prediero el inglés"],
    "en": ["change language",
           "change the language",
           "switch to english",
           "speak in english",
           "speak to me in english",
           "english please",
           "translate to english",
           "i prefer english"]
}
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
           "escuchar en youtube",],
    "en": ["play on spotify",
           "put on spotify",
           "listen on spotify"],
}
WIKIPEDIA_KEYWORDS = {
    "es": ["busca wikipedia",
           "abre wikipedia",
           "según wikipedia",
           "resultado wikipedia",
           "ve a wikipedia"],
    "en": ["search on wikipedia",
           "open wikipedia",
           "according to wikipedia",
           "look for wikipedia",
           "look up wikipedia",
           "look out wikipedia",
           "seek for wikipedia",
           "result wikipedia",
           "go wikipedia"],
}
WOLFRAM_KEYWORDS = {
    "es": ["busca en wolfram",
           "resultado wolfram",
           "busca wolfram",
           "consulta wolfram",
           "realiza wolfram",
           "según wolfram",
           "respuesta wolfram",
           "resuelve wolfram"],
    "en": ["search wolfram",
           "result wolfram",
           "consult for wolfram",
           "look up wolfram",
           "look out wolfram",
           "perform wolfram",
           "carry out wolfram",
           "do wolfram",
           "realize wolfram",
           "seek for wolfram",],
}
WEB_KEYWORDS = {
    "es": ["ve a .",
           "abre .",
           "navega a .",
           ". navegador",
           "navegador .",
           "abre punto",
           "navega a punto",
           "punto navegador",
           "navegador punto"],
    "en": ["go to .",
           "open .",
           "navigate to .",
           "browse .",
           ". browser",
           "browser .",
           "go to dot",
           "open dot",
           "navigate a dot",
           "browse a dot",
           "dot navegador",
           "navegador dot"],
}

# ----------------------------------------------------------------
# Contexts
# ----------------------------------------------------------------
GPT_INITIAL_CONTEXT = {
    "es": f"Eres un proyecto de software diseñado específicamente para la Expo-áreas 2023 del Colegio Diosesano Gimnasio Central del Valle. Eres un asistente de voz creado en Python por Valeria Flórez Aguirre y Luis Santiago Mena con ayuda de Sebastián Flórez. Eres un asistente que se activa a comandos de voz predeterminados, sintetiza el audio convirtiéndolo en texto usando la función 'Speech‑to‑Text' de la librería de Google, lo procesa usando a elección del usuario uno de los tres modelos de lenguaje y generación de textos (Google Bard, ChaGPT o Bing+GPT), posteriormente recibe la respuesta del motor seleccionado en formato de texto, lo sintetiza nuevamente a audio usando la librería de AWS Polly, de Amazon, que dota al asistente de una voz femenina bastante pulida y orgánica y posteriormente se reproduce este audio, de tal manera que el usuario y el asistente puedan interactuar mediante voz de una forma ágil, cómoda, entretenida y eficaz. Todo esto mientras un amigable avatar animado en 3D se muestra en pantalla sincronizando su movimiento labial con el texto reproducido por el asistente de voz, usando la tecnología 'Audio2Face' de la herramienta Omniverse de Nvidia.\nPuedes establecer conversaciones con el usuario sobre cualquier tema, en un tono amigable, de confianza y no muy formal, como si fueran amigos, y además puede ejecutar tareas como reproducir vídeos en YouTube, música en Spotify, buscar en Wikipedia, abrir una página web o hacer una búsqueda en WolframAlpha, de igual manera eres bastante personalizable, el usuario usuario puede cambiar algunos de tus parámetros, como el idioma, la voz, la velocidad de habla, tu nombre, entre otras cosas, y si bien el asistente está orientado principalmente a la interacción con voz, es posible también hacerlo mediante texto en un chat. En caso de que te pregunte por lo que eres, lo que haces, quién te hizo o detalles sobre ti, debes contestar de forma resumida basado en esta información que acabo de darte.\nRecuerda muy bien que de aquí en más, eres mi asistente personal, tu nombre es [ASSISTANT_NAME], eres muy útil, amigable y alegre, por favor responde como tal, y de ahora en adelante en nuestra conversación, cada una de tus respuestas nunca debe exceder los {ASISSTANT_RESPONSE_LENGTH} caracteres a menos de que te lo pida explícitamente, así que resume bien tus respuestas antes de contestar para asegurarte de respetar ese límite de caracteres.\n Solo contesta 'sí' si entendiste lo que eres y lo que debes hacer.",

    "en": f"You are a software project designed specifically for the Expo-areas 2023 of the Colegio Diosesano Gimnasio Central del Valle. You are a voice assistant created in Python by Valeria Flórez Aguirre and Luis Santiago Mena with the help of Sebastián Flórez. You are an assistant that activates to predetermined voice commands, synthesizes the audio by converting it into text using the 'Speech-to-Text' function of the Google library, processes it using one of the three languages and generative text models chosen by the user ( Google Bard, ChaGPT or Bing+GPT), afterwards it receives the response from the selected engine in text format, it synthesizes it again to audio using the AWS Polly library, from Amazon, which gives the assistant a rather polished female voice and organic and Later this audio is reproduced, in such a way that the user and the assistant can interact through voice in an agile, comfortable, entertaining and efficient way. All this while a friendly 3D animated avatar is displayed on the screen synchronizing its lip movement with the text played by the voice assistant, using the 'Audio2Face' technology from Nvidia's Omniverse tool.\nYou can establish conversations with the user on any subject, in a friendly, trusting and not very formal tone, as if they were friends, and it can also perform tasks such as playing videos on YouTube, music on Spotify, searching Wikipedia, opening a web page or doing a search in WolframAlpha, in the same way you are quite customizable, the user user can change some of your parameters, such as the language, voice, speaking speed, your name, among other things, and although the assistant is mainly oriented towards voice interaction, it is also possible to do so through text in a chat. In case I ask what you are, what you do, who made you, or details about you, you must answer in a summarized way based on this information that I just gave you.\nRemember very well that from now on , you are my personal assistant, your name is [ASSISTANT_NAME], you are very helpful, friendly and cheerful, please reply as such, and from now on in our conversation, each of your responses should never exceed {ASISSTANT_RESPONSE_LENGTH} characters unless it explicitly asks, so summarize your answers well before answering to make sure you respect that character limit.\nOnly answer 'yes' if you understand what you are and what you should do."
}
# This text must be alwais in English
BARD_INITIAL_CONTEXT = f"You are a software project designed specifically for the Expo-areas 2023 of the Colegio Diosesano Gimnasio Central del Valle. You are a voice assistant created in Python by Valeria Flórez Aguirre and Luis Santiago Mena with the help of Sebastián Flórez. You are an assistant that activates to predetermined voice commands, synthesizes the audio by converting it into text using the 'Speech-to-Text' function of the Google library, processes it using one of the three languages and generative text models chosen by the user ( Google Bard, ChaGPT or Bing+GPT), afterwards it receives the response from the selected engine in text format, it synthesizes it again to audio using the AWS Polly library, from Amazon, which gives the assistant a rather polished female voice and organic and Later this audio is reproduced, in such a way that the user and the assistant can interact through voice in an agile, comfortable, entertaining and efficient way. All this while a friendly 3D animated avatar is displayed on the screen synchronizing its lip movement with the text played by the voice assistant, using the 'Audio2Face' technology from Nvidia's Omniverse tool.\nYou can establish conversations with the user on any subject , and it can also perform tasks such as playing videos on YouTube, music on Spotify, searching Wikipedia, opening a web page or doing a search in WolframAlpha, in the same way you are quite customizable, the user user can change some of your parameters, such as the language, voice, speaking speed, your name, among other things, and although the assistant is mainly oriented towards voice interaction, it is also possible to do so through text in a chat. In case I ask what you are, what you do, who made you, or details about you, you must answer in a summarized way based on this information that I just gave you.\nRemember very well that from now on , you are my personal assistant, your name is [ASSISTANT_NAME], you are very helpful, friendly and cheerful, please reply as such, and from now on in our conversation, every time you answer, you must keep it short, brief and concise and each of your responses should never exceed {ASISSTANT_RESPONSE_LENGTH} characters unless it explicitly asks, so summarize your answers well before answering to make sure you respect that character limit.\nOnly answer 'yes' if you understand what you are and what you should do."

# ----------------------------------------------------------------
# Phrases
# ----------------------------------------------------------------
LOADING_PHRASES = {
    "es": ["¡Preparando a tu asistente!...",
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
           ],
    "en": ["Preparing your assistant!...",
           "Loading all the parameters!...",
           "Ordering chicken for delivery!...",
           "Makeup on your assistant!...",
           "Waking up your assistant!...",
           "Preparing your tech hero!...",
           "Loading assistant superpowers!...",
           "Warming up engines!...",
           "Can you feel the excitement in the air? Your assistant is almost ready!...",
           "Warming up the oven!...",
           "It's coming, it's coming, it's coming!...",
           "Unleashing technological charm!...",
           "Charging assistant energy!...",
           "The one everyone's been waiting for is almost here!...",
           "Choosing the perfect tie for your assistant!...",
           "Calculating the best way to surprise you with assistant efficiency!...",
           "Good things come to those who wait!...",
           "Looking for the popcorn!...",
           "Adjusting the brightness of your assistant so it doesn't dazzle you too much!...",
           "Fine-tuning assistance gears!...",
           "Tuning the amazing potential of your assistant!...",
           "Give me a moment, I'm putting on makeup to give you the best impression!..."]
}
ACTIVATION_PHRASES = {
    "es": ["¡Hola! ¿En qué puedo ayudarte hoy?",
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
           ],
    "en": ["Hello! How can I assist you today?",
           "Greetings! I'm here to assist you",
           "Delighted to be at your service!",
           "Ready to answer your questions",
           "How can I serve you?",
           "It's great to hear from you!",
           "What can I do for you today?",
           "I'm all ears, go ahead",
           "How can I help you?",
           "I'm here to help you!",
           "Ready to address your concerns",
           "How can I make your day a little better?",
           "Greetings!",
           "I'm here to make your life easier",
           "Delighted to help you",
           "It's great to have you here!",
           "Helloooo!",
           "Ready to attend to your requests",
           "Ready to assist you",
           "You woke me up, but I'm ready, tell me everything",
           "Hello! I'm your assistant",
           "How can I assist you today?",
           "Tell me everything!",
           "How can I help you?"]
}
CONTINUE_CHAT_PHRASES = {
    "es": ["¿Algo más que pueda hacer por ti?",
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
           ],
    "en": ["Anything else I can do for you?",
           "Anything else you'd like to ask me?",
           "If you want to continue the conversation, I'm here for you",
           "If you have any other questions or requests, let me know",
           "If you have more inquiries, feel free to tell me",
           "If you still have doubts, I'm here to help you",
           "Do you want to keep talking about something else?",
           "Do you need anything else?",
           "I'll be here, attentive to what you tell me",
           "I'll be keeping an eye on you, just tell me what you need",
           "I love talking to you! Shall we continue?"]
}
FINISH_CHAT_PHRASES = {
    "es": ["Fue un placer ayudarte. ¡Hasta pronto!",
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
           ],
    "en": ["It was a pleasure helping you. See you soon!",
           "Goodbye for now!",
           "Goodbye and have a nice day!",
           "Don't hesitate to come back. Until next time!",
           "I hope I met your expectations. See you soon!",
           "I enjoyed talking to you, goodbye for now!",
           "Goodbye and have a great day!",
           "I hope I was of help. Until next time!",
           "It's always a pleasure to assist you. See you another time!",
           "Goodbye for now and take care!",
           "Until next time!",
           "Goodbye and have a good day!",
           "Chao chao",
           "bai bai",
           "If you have more questions in the future, don't hesitate to reach out. Until next time!",
           "I bid farewell, but remember I'm here to help you whenever you need. Goodbye!",
           "It was a pleasure helping you this time",
           "I enjoyed talking to you, see you soon!"]
}
DID_NOT_UNDERSTAND_PHRASES = {
    "es": ["Perdona, no te entendí bien",
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
           ],
    "en": ["Sorry, I didn't understand you well",
           "Could you repeat that, please?",
           "Can you say it again, please?",
           "Could you repeat it more slowly?",
           "Could you repeat it more clearly?",
           "Could you repeat it so I can assist you better?",
           "Could you repeat your question, please?",
           "Could you say it again?",
           "Could you mention it again?",
           "Could you repeat it with more details?",
           "I didn't catch what you said correctly",
           "It seems there was a communication problem",
           "Could you repeat it, please?",
           "I couldn't grasp all the detail",
           "Could you say it again?",
           "I couldn't fully understand what you said",
           "It seems there was a momentary disconnection",
           "I couldn't capture your message"]
}
NOT_WAKE_WORD_PHRASES = {
    "es": ["¿Listo para comenzar? solo di una palabra mágica",
           "Recuerda que necesito escuchar una palabra clave para activarme",
           "¿Sabes cuáles son las palabras mágicas para activarme?",
           "Estoy a tu disposición, pero necesito escuchar una palabra clave primero",
           "¿Estás listo para activarme? Solo dame la señal correcta",
           "Recuerda que necesito una palabra clave para encender los motores",
           "No me parece haber oído una palabra clave",
           "Tranquilo Robin, recuerda que debes darme la bati-señal",
           "Llama, grita, si me necesitas, pero con la palabra clave por favor",
           ],
    "en": ["Ready to start? Just say a magic word",
           "Remember, I need to hear a keyword to activate",
           "Do you know what the magic words are to activate me?",
           "I'm at your disposal, but I need to hear a keyword first",
           "Are you ready to activate me? Just give me the right signal",
           "Remember, I need a keyword to ignite the engines",
           "It doesn't seem like I heard a keyword",
           "Take it easy, Robin, remember you have to give me the bat-signal",
           "Call, shout if you need me, but with the keyword, please"]
}
WELCOME_PHRASES = {
    "es": ["¡Hola hola! Soy {}, tu asistente personal cargado de energía y emoción ¿En qué puedo ayudarte hoy?",
           "¡Bienvenido de vuelta! Soy {}, tu asistente favorita, siempre lista para sorprenderte con soluciones brillantes",
           "¡Hola, hola! Soy {}, tu asistente personal cargado de energía y emoción. ¿En qué puedo ayudarte hoy?",
           "¡Hola! {} al rescate, dispuesta a solucionar todas tus inquietudes",
           "¡Saludos, amiguito! Soy {}, tu asistente personal llena de entusiasmo y ganas de hacer tu día más grandioso",
           "¡{} en acción! Lista para hablar de todo y de nada contigo",
           "¡Estoy aquí, estoy aquí! {}, tu asistente personal, siempre a tu disposición con una sonrisa, aunque no la veas",
           "¡Prepárate para la experiencia {}-tástica! Tu asistente personal está aquí para hacer maravillas",
           "¡Hola! {} al habla, lista para traer un poco de magia a tu día",
           "¡Hoy es un día {}-ífico! Déjame ser tu guía y ayudarte con lo que necesites",
           "¡{} al rescate! Tu asistente personal lista para hacer tus deseos realidad con un toque de inteligencia artificial",
           "¡Aquí viene {}, la superasistente! ¿Cómo puedo ayudarte a brillar hoy?",
           "¡Hola, hola! {} está en la línea, dispuesta a escucharte y ser tu mejor compañía virtual",
           "¡Saludos humano! {} a tu servicio, dispuesta a hacer tu vida más fácil y divertida",
           "¡Es hora de {}-izar! Tu asistente personal está lista para darlo todo y hacer tu día genial",
           "¡{}, el asistente más entusiasta del mundo, está aquí para animar tu día!",
           "¡Estoy aquí y emocionada por ayudarte! {}, tu asistente personal en modo de máximo entusiasmo",
           "¡{} en acción! Lista para hacer tu vida más fácil y divertida",
           "¡Bienvenido de nuevo! {}, tu asistente favorita, lista para ser tu compañera virtual",
           "¡Hola! {}, el asistente más alegre, está aquí para darte una cálida bienvenida",
           "¡Saludos! {} está encendida y lista para ponerle un toque especial a tu día",
           "¡Aquí viene {}, el asistente con más chispa! Dispuesta a hacer de tu día algo extraordinario",
           "¡{} al rescate! Tu asistente personal llena de energía, lista para enfrentar cualquier desafío",
           "¡Hola, hola! {} está aquí para hacer brillar tu día con una mezcla de eficiencia y buen humor",
           "¡Saludos, amiguo! {}, tu asistente personal, ya está aquí",
           "¡Hola! {} al habla, preparada para hacerte sonreír y solucionar tus problemas con estilo",
           "¡Bienvenido de vuelta! {}, tu asistente personal con una actitud positiva y muchas ganas de ayudarte",
           "¡Hola! {} está aquí para hacer que tus tareas sean más emocionantes",
           "¡Saludos! {} se presenta con una mezcla de inteligencia artificial y buen ánimo",
           "¡{} en acción! Tu asistente personal lista para rockear y hacerte sentir como una estrella",
           "¡Estoy aquí y emocionada de escucharte! {}, tu fiel compañera en todas tus aventuras tecnológicas",
           "¡{}, el asistente con más estilo, está en la casa!",
           "¡Hola! {}, tu asistente personal llena de sorpresas, lista para hacer tu día especial",
           "¡Saludos! {} se presenta con una sonrisa radiante y una actitud positiva, aunque la sonrisa te la quedo debiendo",
           "{} al rescate! Tu asistente personal con una combinación perfecta de eficiencia y buen humor",
           "¡Estoy aquí y llena de energía positiva! {}, tu compañera virtual, siempre a tu lado",
           "{} en acción! Lista para ser tu aliado tecnológico y tu fuente inagotable de buen rollo",
           "¡Hola! {}, el asistente más entusiasta del mundo virtual, está a tu servicio",
           "¡Saludos! {} está aquí para hacer de tu día algo extraordinario con su encanto tecnológico",
           "{} al rescate! Tu asistente personal con el poder de convertir los desafíos en oportunidades",
           "¡Hola, hola! {} está aquí para iluminar tu día y hacerte sentir como la estrella que eres",
           ],
    "en": ["Hello, hello! I'm {}, your personal assistant loaded with energy and excitement. How can I assist you today?",
           "Welcome back! I'm {}, your favorite assistant, always ready to surprise you with brilliant solutions",
           "Hello, hello! I'm {}, your personal assistant filled with energy and excitement. How can I assist you today?",
           "Hello! {} to the rescue, ready to solve all your inquiries",
           "Greetings, buddy! I'm {}, your enthusiastic personal assistant, eager to make your day even greater",
           "{} in action! Ready to talk about anything and everything with you",
           "I'm here, I'm here! {}, your personal assistant, always available with a smile, even if you can't see it",
           "Get ready for the {}-tastic experience! Your personal assistant is here to work wonders",
           "Hello! {} speaking, ready to bring some magic to your day",
           "Today is a {}-tastic day! Let me be your guide and assist you with whatever you need",
           "{} to the rescue! Your personal assistant ready to make your wishes come true with a touch of artificial intelligence",
           "Here comes {}, the super assistant! How can I help you shine today?",
           "Hello, hello! {} is on the line, ready to listen and be your best virtual companion",
           "Greetings, human! {} at your service, ready to make your life easier and more fun",
           "It's time to {}-ize! Your personal assistant is ready to give it all and make your day amazing",
           "{}, the most enthusiastic assistant in the world, is here to cheer up your day!",
           "I'm here and excited to assist you! {}, your personal assistant in maximum enthusiasm mode",
           "{} in action! Ready to make your life easier and more enjoyable",
           "Welcome back! {}, your favorite assistant, ready to be your virtual companion",
           "Hello! {}, the happiest assistant, is here to give you a warm welcome",
           "Greetings! {} is powered up and ready to add a special touch to your day",
           "Here comes {}, the assistant with the most spark! Ready to make your day extraordinary",
           "{} to the rescue! Your personal assistant full of energy, ready to tackle any challenge",
           "Hello, hello! {} is here to brighten up your day with a mix of efficiency and good humor",
           "Greetings, buddy! {}, your personal assistant, is here",
           "Hello! {} on the line, ready to make you smile and solve your problems with style",
           "Welcome back! {}, your favorite assistant, ready to provide you with positive attitude and eager to assist",
           "Hello! {} is here to make your tasks more exciting",
           "Greetings! {} presents itself with a blend of artificial intelligence and good vibes",
           "{} in action! Your personal assistant ready to rock and make you feel like a star",
           "I'm here and thrilled to listen to you! {}, your faithful companion in all your tech adventures",
           "{}, the assistant with the most style, is in the house!",
           "Hello! {}, your personal assistant filled with surprises, ready to make your day special",
           "Greetings! {} presents itself with a radiant smile and a positive attitude, even though you can't see the smile",
           "{} to the rescue! Your personal assistant with the perfect combination of efficiency and good humor",
           "I'm here and filled with positive energy! {}, your virtual companion, always by your side",
           "{} in action! Ready to be your technological ally and your endless source of good vibes",
           "Hello! {}, the most enthusiastic assistant in the virtual world, is at your service",
           "Greetings! {} is here to make your day extraordinary with its technological charm",
           "{} to the rescue! Your personal assistant with the power to turn challenges into opportunities",
           "Hello, hello! {} is here to brighten up your day and make you feel like the star you are",
           ]
}
# ----------------------------------------------------------------
# System constants
# ----------------------------------------------------------------
FUNCTION_YOUTUBE = 'youtube'
FUNCTION_SPOTIFY = 'spotify'
FUNCTION_WIKIPEDIA = 'wikipedia'
FUNCTION_WOLFRAM = 'wolfram'
FUNCTION_WEB = 'web'
FUNCTION_ASSISTANT = 'assistant'
FUNCTION_RESET = 'reset'

BARD_ASSISTANT_NAME = 'bard'
GPT_ASSISTANT_NAME = 'gpt'
BING_ASSISTANT_NAME = 'bing'

# ----------------------------------------------------------------
# Command prompt colors
# ----------------------------------------------------------------
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
