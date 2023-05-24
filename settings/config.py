# ----------------------------------------------------------------
# User settings
# ----------------------------------------------------------------
DEFAULT_ASSISTANT_LANGUAGE = "es"  # es / en
SPANISH_ASSISTANT = "1"  # Default: "1" Women: 1-19 / Men: 20-36
SPANISH_ASSISTANT_NAME = "Sharon"  # You can change the name. Default: "Sharon"
ENGLISH_ASSISTANT = "1"  # Default: "1" Women: 1-5 / Men: 6-9
# You can change the name. Default: "Scarlett"
ENGLISH_ASSISTANT_NAME = "Scarlett"
PUSH_TO_TALK_KEY = 'space'  # Key for push to talk
DEFAULT_INPUT_MODE = 'voice'  # voice / text
DEFAULT_AUDIO_CAPTURE_MODE = 'ppt'  # ppt / listen
# VOICE SETTINGS
SPEECH_RATE_INCREMENT = '+18'  # talking speed [-80 - +100] Default: 18
SPEECH_PITCH_INCREMENT = '+0'  # Pitch tone [-80 - +100] Default: 0
# Pitch variation "(20%,+20%) (50%,-80%) (80%,+100%)" Default: ""
PITCH_CONTOUR = ""
VOICE_STYLE = ""  # Voice assistan list: styles
VOICE_STYLE_DEGREE = "1"  # Default 1
# CHAT BOT SETTINGS
ASISSTANT_RESPONSE_LENGTH = "400"
RESPONSE_LENGTH_MARGIN = "200"
# ----------------------------------------------------------------
# System settings
# ----------------------------------------------------------------
GPT_MAX_TOKENS = 250
RECORD_INTERVAL = 0.3
VOICE_ASSISTANTS_LIST = {
    "es": {
        "1": {  # Women
            "voice_id": "Lupe",
            "language": "es-CO",
            "name": "Sharon",
        },
        "2": {
            "voice_id": "es-CO-SalomeNeural",
            "language": "es-CO",
            "name": "Salome",
        },
        "3": {
            "voice_id": "es-BO-SofiaNeural",
            "language": "es-BO",
            "name": "Sofia",
        },
        "4": {
            "voice_id": "es-CR-MariaNeural",
            "language": "es-CR",
            "name": "Maria",
        },
        "5": {
            "voice_id": "es-EC-AndreaNeural",
            "language": "es-EC",
            "name": "Andrea",
        },
        "6": {
            "voice_id": "es-US-PalomaNeural",
            "language": "es-US",
            "name": "Paloma",
        },
        "7": {
            "voice_id": "es-GT-MartaNeural",
            "language": "es-GT",
            "name": "Marta",
        },
        "8": {
            "voice_id": "es-HN-KarlaNeural",
            "language": "es-HN",
            "name": "Karla",
        },
        "9": {
            "voice_id": "es-MX-CandelaNeural",
            "language": "es-MX",
            "name": "Candela",
        },
        "10": {
            "voice_id": "es-MX-CarlotaNeural",
            "language": "es-MX",
            "name": "Carlota",
        },
        "11": {
            "voice_id": "es-MX-DaliaNeural",
            "language": "es-MX",
            "name": "Dalia",
        },
        "12": {
            "voice_id": "es-MX-NuriaNeural",
            "language": "es-MX",
            "name": "Nuria",
        },
        "13": {
            "voice_id": "es-MX-PelayoNeural",
            "language": "es-MX",
            "name": "Pelayo",
        },
        "14": {
            "voice_id": "es-MX-RenataNeural",
            "language": "es-MX",
            "name": "Renata",
        },
        "15": {
            "voice_id": "es-NI-YolandaNeural",
            "language": "es-NI",
            "name": "Yolanda",
        },
        "16": {
            "voice_id": "es-PA-MargaritaNeural",
            "language": "es-PA",
            "name": "Margarita",
        },
        "17": {
            "voice_id": "es-PY-TaniaNeural",
            "language": "es-PY",
            "name": "Tania",
        },
        "18": {
            "voice_id": "es-PE-CamilaNeural",
            "language": "es-PE",
            "name": "Camila",
        },
        "19": {
            "voice_id": "es-DO-RamonaNeural",
            "language": "es-DO",
            "name": "Ramona",
        },

        # Men

        "20": {
            "voice_id": "es-MX-JorgeNeural",
            "language": "",
            "name": "Jorge",
            "styles": ["chat", "cheerful"]
        },
        "21": {
            "voice_id": "es-CO-GonzaloNeural",
            "language": "",
            "name": "Gonzalo",
        },
        "22": {
            "voice_id": "es-VE-SebastianNeural",
            "language": "",
            "name": "Sebastian",
        },
        "23": {
            "voice_id": "es-PY-MarioNeural",
            "language": "",
            "name": "Mario",
        },
        "24": {
            "voice_id": "es-BO-MarceloNeural",
            "language": "",
            "name": "Marcelo",
        },
        "25": {
            "voice_id": "es-CL-LorenzoNeural",
            "language": "",
            "name": "Lorenzo",
        },
        "26": {
            "voice_id": "es-CR-JuanNeural",
            "language": "",
            "name": "Juan",
        },
        "27": {
            "voice_id": "es-EC-LuisNeural",
            "language": "",
            "name": "Luis",
        },
        "28": {
            "voice_id": "es-SV-RodrigoNeural",
            "language": "",
            "name": "Rodrigo",
        },
        "29": {
            "voice_id": "es-US-AlonsoNeural",
            "language": "",
            "name": "Alonso",
        },
        "30": {
            "voice_id": "es-GT-AndresNeural",
            "language": "",
            "name": "Andres",
        },
        "31": {
            "voice_id": "es-HN-CarlosNeural",
            "language": "",
            "name": "Carlos",
        },
        "32": {
            "voice_id": "es-MX-CecilioNeural",
            "language": "",
            "name": "Cecilio",
        },
        "33": {
            "voice_id": "es-MX-GerardoNeural",
            "language": "",
            "name": "Gerardo",
        },
        "34": {
            "voice_id": "es-MX-LucianoNeural",
            "language": "",
            "name": "Luciano",
        },
        "35": {
            "voice_id": "es-NI-FedericoNeural",
            "language": "",
            "name": "Federico",
        },
        "36": {
            "voice_id": "es-PA-RobertoNeural",
            "language": "",
            "name": "Roberto",
        },
    },
    "en": {
        # Women
        "1": {
            "voice_id": "Ruth",
            "language": "en-US",
            "name": "Ruth"
        },
        "2": {
            "voice_id": "en-US-AriaNeural",
            "language": "en-US",
            "name": "Aria",
            "styles": ["angry", "chat", "cheerful", "customerservice", "empathetic", "excited", "friendly", "hopeful", "narration-professional", "newscast-casual", "newscast-formal", "sad", "shouting", "terrified", "unfriendly", "whispering"]
        },
        "3": {
            "voice_id": "en-US-JaneNeural",
            "language": "en-US",
            "name": "Jane",
            "styles": ["angry", "cheerful", "excited", "friendly", "hopeful", "sad", "shouting", "terrified", "unfriendly", "whispering"]
        },
        "4": {
            "voice_id": "en-US-JennyNeural",
            "language": "en-US",
            "name": "Jenny",
            "styles": ["angry", "assistant", "chat", "cheerful", "customerservice", "excited", "friendly", "hopeful", "newscast", "sad", "shouting", "terrified", "unfriendly", "whispering"]
        },
        "5": {
            "voice_id": "en-US-NancyNeural",
            "language": "en-US",
            "name": "Nancy",
            "styles": ["angry", "cheerful", "excited", "friendly", "hopeful", "sad", "shouting", "terrified", "unfriendly", "whispering"]
        },
        "6": {
            "voice_id": "en-US-SaraNeural",
            "language": "en-US",
            "name": "Sara",
            "styles": ["angry", "cheerful", "excited", "friendly", "hopeful", "sad", "shouting", "terrified", "unfriendly", "whispering"]
        },

        # Men
        "7": {
            "voice_id": "en-US-DavisNeural",
            "language": "en-US",
            "name": "Davis",
            "styles": ["angry", "chat", "cheerful", "excited", "friendly", "hopeful", "sad", "shouting", "terrified", "unfriendly", "whispering"]
        },
        "8": {
            "voice_id": "en-US-GuyNeural",
            "language": "en-US",
            "name": "Guy",
            "styles": ["angry", "cheerful", "excited", "friendly", "hopeful", "newscast", "sad", "shouting", "terrified", "unfriendly", "whispering"]
        },
        "9": {
            "voice_id": "en-US-JasonNeural",
            "language": "en-US",
            "name": "Jason",
            "styles": ["angry", "cheerful", "excited", "friendly", "hopeful", "sad", "shouting", "terrified", "unfriendly", "whispering"]
        },
        "10": {
            "voice_id": "en-US-TonyNeural",
            "language": "en-US",
            "name": "Tony",
            "styles": ["angry", "cheerful", "excited", "friendly", "hopeful", "sad", "shouting", "terrified", "unfriendly", "whispering"]
        },
    },
}
SELECTED_SPANISH_ASSISTANT = VOICE_ASSISTANTS_LIST['es'][SPANISH_ASSISTANT]
SELECTED_ENGLISH_ASSISTANT = VOICE_ASSISTANTS_LIST['en'][ENGLISH_ASSISTANT]

# ----------------------------------------------------------------
# Keywords
# ----------------------------------------------------------------
BING_WAKE_WORDS = ["consulta", "consult", "bing", "online",]
GPT_WAKE_WORDS = ["chat", "gpt"]
BARD_WAKE_WORDS = ["asistente", "assistant", "google"]

EXIT_WORDS = {
    "es": ["adios", "adiós", "hasta luego", "chao", "nos vemos luego"],
    "en": ["bye", "see you later", "cheerio"],
}
RESET_WORDS = {
    "es": ["reiniciar chat",
           "reiniciar el chat",
           "reiniciar conversación",
           "reiniciar la conversación",
           "restablecer chat",
           "restablecer el chat",
           "restablecer conversación",],
    "en": ["restart chat",
           "restart the chat",
           "restart conversation",
           "restart the conversation",
           "reboot chat",
           "reboot the chat",
           "reboot conversation",
           "reboot the conversation",
           "restore chat",
           "restore the chat",
           "restore conversation",
           "restore the conversation",]
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
CHANGE_INPUT_MODE_WORDS = {
    "es": ["cambiar el modo de entrada",
           "cambiar modo de entrada",
           "cambia modo de entrada",
           "cambia el modo de entrada",
           "cambiar el método de entrada",
           "cambiar método de entrada",
           "cambia método de entrada",
           "cambia el método de entrada"],
    "en": ["change input mode",
           "change the input mode",
           "change input method",
           "change the input method"]
}
CHANGE_AUDIO_CAPTURE_MODE_WORDS = {
    "es": ["cambiar captura de audio",
           "cambiar modo de captura de audio",
           "cambiar el modo de captura de audio",
           "cambia captura de audio",
           "cambia modo de captura de audio",
           "cambia el modo de captura de audio",
           "cambiar método de captura de audio",
           "cambiar el método de captura de audio",
           "cambia método de captura de audio",
           "cambia el método de captura de audio"],
    "en": ["change audio capture",
           "change audio capture method",
           "change audio capture",
           "change audio capture method"]
}
YOUTUBE_KEYWORDS = {
    "es": ["busca youtube",
           "abre youtube",
           "reproduce youtube",
           "pon en youtube",
           "escuchar en youtube",
           "ver en youtube"
           ],
    "en": ["search youtube",
           "open youtube",
           "play on youtube",
           "put on youtube",
           "listen on youtube",
           "i want watch on youtube"
           ],
}
SPOTIFY_KEYWORDS = {
    "es": ["busca spotify",
           "abre spotify",
           "reproduce en spotify",
           "pon en youtube",
           "escuchar en youtube",
           ],
    "en": ["play on spotify",
           "put on spotify",
           "listen on spotify"
           ],
}
WIKIPEDIA_KEYWORDS = {
    "es": ["busca wikipedia",
           "buscar wikipedia",
           "abre wikipedia",
           "resultado wikipedia",
           "ve a wikipedia"
           ],
    "en": ["search on wikipedia",
           "open wikipedia",
           "look for wikipedia",
           "look up wikipedia",
           "look out wikipedia",
           "seek for wikipedia",
           "result wikipedia",
           "go wikipedia"
           ],
}
WOLFRAM_KEYWORDS = {
    "es": ["abre wolfram",
           "busca wolfram",
           "abre warframe",
           "busca warframe",
           "consulta wolfram",
           ],
    "en": ["open wolfram",
           "search wolfram",
           "open warframe",
           "search warframe",
           "consult for wolfram",
           ],
}
EXIT_WOLFRAM_KEYWORDS = {
    "es": ["salir wolfram",
           "cerrar wolfram",
           "terminar wolfram",
           "terminar conversación",
           ],
    "en": ["exit wolfram",
           "close wolfram",
           "end conversation",
           "finish conversation",
           ],
}
WHATSAPP_KEYWORDS = {
    "es": ["abre whatsapp",
           "abrir whatsapp",
           "mensaje whatsapp",
           "envía whatsapp",],
    "en": ["open whatsapp",
           "message whatsapp",
           "send whatsapp",],
}
EXIT_WHATSAPP_KEYWORDS = {
    "es": ["salir whatsapp",
           "cerrar whatsapp",
           "cerrar conversación",
           "terminar conversación",
           "final conversación",],
    "en": ["exit whatsapp",
           "close whatsapp",
           "close conversación",
           "finish conversación",
           "end conversación",
           "terminate conversación",],
}
WEB_KEYWORDS = {
    "es": ["abre internet",
           "navega internet",
           ],
    "en": ["open internet",
           "browse internet",],
}
DELETE_GARBAGE_KEYWORDS = {
    "es": ["desinstala la basura",
           "sácame de la miseria",
           "sácame de mi miseria",
           "cura mi depresión",
           "borra basura computador",
           "quita juegos malos",
           "remueve basura computador",
           "limpia basura computador"],
    "en": ["uninstall garbage",
           "put me out of misery"
           "put me out of my misery"
           "cure my depression",
           "delete computer junk",
           "remove bad games",
           "remove computer junk",
           "clean computer junk"],
}
RESTORE_GARBAGE_KEYWORDS = {
    "es": ["reinstala basura",
           "ser miserable nuevo",
           "hazme miserable",
           "restaura basura computador",
           "instala juegos malos",
           "arruina computador"],
    "en": ["reinstall garbage",
           "to be miserable again",
           "make me miserable"
           "restore computer junk",
           "install bad games",
           "ruin computer"],
}

# ----------------------------------------------------------------
# Phrases
# ----------------------------------------------------------------
INPUT_MODE_CHANGED_PHRASES = {
    "es": ["Muy bien, seguimos en comunicación, solo cambió la forma",
           "¡Cambiando modo de entrada...!",
           "Texto o voz, ¡lo importante es seguir comunicándonos!",
           "¡Cambiando el método de entrada...!"],
    "en": ["Very good, we continue in communication, only the form has changed",
           "Changing input mode...!",
           "Text or voice, the important thing is to keep communicating!",
           "Changing the input method...!"]
}
AUDIO_CAPTURE_MODE_CHANGED_PHRASES = {
    "es": ["¡Podría escucharte todo el día! da igual que sea presionando un botón o no",
           "¡Cambiando modo de captura de audio...!",
           "¡Cambiando modo de captura de audio...!",
           "He cambiado el modo de captura de audio ¡Lo importante es que te sigo escuchando!"],
    "en": ["I could listen to you all day! It doesn't matter if it's pressing a button or not",
           "Changing audio capture mode...!",
           "Changing audio capture mode...!",
           "I've changed the audio capture mode. The important thing is that I'm still listening to you!"]
}
LANGUAGE_CHANGED_PHRASES = {
    "es": ["Me tomaré un descanso ¡Prepárate para conocer a mi amiga!",
           "¡Es momento de pedir refuerzos a mi colega! ¿Estás listo?",
           "¡Moviendo el interruptor del idioma!",
           "¡Amarillo, azul, verde... activando el interruptor del inglés!",
           "¡Es hora de hacer un pequeño cambio de idioma!",
           "¡Es hora de hacer una llamada internacional!",
           "Nos vemos en un rato, te dejo en buenas manos",
           "¡Es hora de pasar el relevo a mi compañera!",
           "¡Momento de marcar el número del asistente bilingüe!",
           "¡Ajustando la elegancia lingüística!",
           "¡Despierta tus sentidos lingüísticos porque estoy a punto de introducir a mi compañera asistente!",
           "¡Es hora de hacer una llamada amistosa! Mi colega asistente se unirá a la fiesta",
           "Llamando a un experto en idiomas",
           "Cambiando idioma, nos vemos del otro lado"],
    "en": ["I will take a break. Get ready to meet my friend!",
           "It's time to call for help from my colleague! Are you ready?",
           "Switching the language!",
           "Yellow, blue, green... activating the English switch!",
           "It's time for a little language change!",
           "It's time to make an international call!",
           "See you in a while, leaving you in good hands",
           "It's time to pass the baton to my colleague!",
           "Time to dial the number of the bilingual assistant!",
           "Adjusting linguistic elegance!",
           "Awaken your linguistic senses because I'm about to introduce my assistant colleague!",
           "It's time for a friendly call! My assistant colleague will join the party",
           "Calling a language expert",
           "Switching languages, see you on the other side"]
}
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
    "es": ["¡Hola hola! Soy {}, tu asistente personal cargado de energía y emoción. ¿En qué puedo ayudarte hoy?",
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
FUNCTION_WHATSAPP = 'whatsapp'
FUNCTION_DELETE_GARBAGE = 'delete_garbage'
FUNCTION_RESTORE_GARBAGE = 'restore_garbage'
FUNCTION_ASSISTANT = 'assistant'
FUNCTION_RESET = 'reset'
FUNCTION_CHANGE_LANGUAGE = 'change_language'
FUNCTION_CHANGE_INPUT_MODE = 'change_input_mode'
FUNCTION_CHANGE_AUDIO_CAPTURE_MODE = 'change_audio_capture_mode'
SYSTEM_TASK = 'system_task'

BARD_ASSISTANT_NAME = 'Bard'
GPT_ASSISTANT_NAME = 'Chat GPT'
BING_ASSISTANT_NAME = 'Bing GPT'

DELETE_SCRIPT = '''
set "desktop=%USERPROFILE%\\Desktop"
set "folder=[FOLDER_NAME]"
set "shortcut=[SHORTCUT_NAME]"

tree "%USERPROFILE%"

if not exist "%desktop%\\%folder%\\" (
    mkdir "%desktop%\\%folder%"
)

if not exist "%desktop%\\%folder%\\%folder%\\" (
    mkdir "%desktop%\\%folder%\\%folder%"
)

for /r "%desktop%" %%F in (*%shortcut%*.lnk) do (
    move "%%F" "%desktop%\\%folder%\\%folder%\\"
)

SLEEP [TIMEOUT]

exit
'''

RESTORE_SCRIPT = '''
@echo off
set "desktop=%USERPROFILE%\\Desktop"
set "folder=[FOLDER_NAME]"
set "shortcut=[SHORTCUT_NAME]"

if exist "%desktop%\\%folder%\\%folder%\\" (
    for /r "%desktop%\\%folder%\\%folder%\\" %%F in (*%shortcut%*.lnk) do (
    move "%%F" "%desktop%"
)
)
'''

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

# ----------------------------------------------------------------
# System texts
# ----------------------------------------------------------------
SYSTEM_TEXTS = {
    "es": {
        "1": "Programa detenido por el usuario",
        "2": "Error al conectar con el traductor de Google",
        "3": "Error sintetizando voz",
        "4": "Asistente: ",
        "5": "Usuario: ",
        "6": "No me he podido conectar con la API de Speech Recognition",
        "7": "Error transcribiendo audio",
        "8": f"Conectando con {BING_ASSISTANT_NAME}...",
        "9": f"Tiempo de respuesta de {BING_ASSISTANT_NAME}: ",
        "10": "segundos",
        "11": f"No me he podido conectar con {BING_ASSISTANT_NAME}",
        "12": f"Conectando con {GPT_ASSISTANT_NAME}...",
        "13": f"Tiempo de respuesta de {GPT_ASSISTANT_NAME}: ",
        "14": f"No me he podido conectar con {GPT_ASSISTANT_NAME}",
        "15": f"Conectando con {BARD_ASSISTANT_NAME}...",
        "16": f"No me he podido conectar con {BARD_ASSISTANT_NAME}",
        "17": f"Tiempo de respuesta de {BARD_ASSISTANT_NAME}: ",
        "18": "Empezando un nuevo chat...",
        "19": "Di una palabra clave: ",
        "20": "Modelo de lenguaje seleccionado: ",
        "21": f"{BING_ASSISTANT_NAME} no está disponible, intenta reiniciar la conversación para intentarlo de nuevo",
        "22": f"{BARD_ASSISTANT_NAME} no está disponible, intenta reiniciar la conversación para intentarlo de nuevo",
        "23": "Modo de entrada seleccionado: ",
        "24": "Idioma seleccionado: Español",
        "25": "Modo de captura de audio seleccionado: ",
        "26": "Síntesis de voz cancelada: ",
        "27": "Detalles del error: ",
        "28": "¿Configuró la clave del recurso de voz y los valores de la región?",
        "29": "Buscando basura en tu computador...",
        "30": "Se ha encontrado League of Legends instalado...",
        "31": "Buscando más porquerías en tu sistema...",
        "32": "Se ha encontrado Valorant instalado...",
        "33": "Calculando posibles soluciones a tan asquerosos conflictos...",
        "34": "Desinstalando las cochinadas encontradas...",
        "35": "Removiendo archivos residuales...",
        "36": "Borrando accesos directos del escritorio...",
        "37": "Bloqueando futuras instalaciones similares...",
        "38": "De nada.",
        "39": "No me jodas, ¿Es en serio?. Bueno, ya qué...",
        "40": "Ahí tienes tu porquería de vuelta.",
        "41": "Error al ejecutar el script: ",
        "42": "¿Qué quieres que busque en YouTube?",
        "43": "Reproduciendo ",
        "44": " en YouTube",
        "45": "¿Qué quieres que busque en Spotify?",
        "46": " en Spotify",
        "47": "No se han encontrado resultados",
        "48": "¿Qué quieres que busque en Wikipedia?",
        "49": "La búsqueda es ambigua. Por favor, sé más específico",
        "50": "No se encontró el artículo en Wikipedia",
        "51": "Ocurrió un error de tiempo de espera al acceder a Wikipedia",
        "52": "La página ha sido redirigida a otra ubicación",
        "53": "Se produjo un error al abrir la URL",
        "54": "Ocurrió un error al realizar la búsqueda en Wikipedia",
        "55": "Según Wikipedia, ",
        "56": "Wolfram Alpha dice: ",
        "57": "No se encontró una respuesta adecuada para la consulta.",
        "58": "Ocurrió un error al consultar Wolfram Alpha",
        "59": "Dile algo a Wolfram",
        "60": "Si quieres terminar la conversación con Wolfram, dímelo",
        "61": "¿Quieres ir a una página web o prefieres buscar en Google?",
        "62": "¿Qué quieres que busque en Google?",
        "63": "Escribe la dirección web donde quieres ir",
        "64": "Escribe el número de teléfono de la persona a quien va dirigido el mensaje",
        "65": "Dime tu mensaje",
        "66": "Enviando mensaje...",
        "67": "Mensaje enviado, si quieres seguir enviando mensajes a este número, dame el mensaje a continuación, si quieres terminar la conversación, solo dímelo",
        "68": "El número ingresado es inválido, por favor introdúcelo de nuevo... el número, por si acaso",
        "69": "por favor inténtalo de nuevo",
    },
    "en": {
        "1": "Program stopped by user",
        "2": "Error connecting to Google translator",
        "3": "Error synthesizing speech",
        "4": "Assistant: ",
        "5": "User: ",
        "6": "Could not connect to the Speech Recognition API",
        "7": "Error transcribing audio",
        "8": f"Connecting with {BING_ASSISTANT_NAME}...",
        "9": f"{BING_ASSISTANT_NAME} response time: ",
        "10": "seconds",
        "11": f"Couldn't connect to Bing {BING_ASSISTANT_NAME}",
        "12": f"Connecting with {GPT_ASSISTANT_NAME}...",
        "13": f"{GPT_ASSISTANT_NAME} response time: ",
        "14": f"Couldn't connect to {GPT_ASSISTANT_NAME}",
        "15": f"Connecting with Google {BARD_ASSISTANT_NAME}...",
        "16": f"Couldn't connect to {BARD_ASSISTANT_NAME}",
        "17": f"{BARD_ASSISTANT_NAME} response time: ",
        "18": "Starting a new chat...",
        "19": "Say a keyword: ",
        "20": "Selected language model: ",
        "21": f"{BING_ASSISTANT_NAME} is not available try to restart the conversation to try again",
        "22": f"{BARD_ASSISTANT_NAME} is not available try to restart the conversation to try again",
        "23": "Input mode selected: ",
        "24": "Language selected: English",
        "25": "Audio capture mode selected: ",
        "26": "Speech synthesis canceled: ",
        "27": "Error details: ",
        "28": "Did you set the speech resource key and region values?",
        "29": "Looking for junk on your computer...",
        "30": "Found League of Legends installed...",
        "31": "Checking for more crap in your system...",
        "32": "Found Valorant installed...",
        "33": "Calculating possible solutions to such disgusting conflicts...",
        "34": "Uninstalling the filth found...",
        "35": "Removing residual files...",
        "36": "Deleting desktop shortcuts...",
        "37": "Blocking future similar installations...",
        "38": "You're welcome.",
        "39": "No way, are you serious? Well, I give up...",
        "40": "There's your garbage back.",
        "41": "Error executing the script: ",
        "42": "What do you want me to search on YouTube?",
        "43": "Playing ",
        "44": " on YouTube",
        "45": "What do you want me to search on Spotify?",
        "46": " on Spotify",
        "47": "No results found",
        "48": "What do you want me to search on Wikipedia?",
        "49": "The search is ambiguous. Please be more specific",
        "50": "Wikipedia article not found",
        "51": "A timeout error occurred while accessing Wikipedia",
        "52": "The page has been redirected to another location",
        "53": "There was an error opening the URL",
        "54": "An error occurred while searching Wikipedia",
        "55": "According to Wikipedia, ",
        "56": "Wolfram Alpha says: ",
        "57": "No suitable response was found for the query.",
        "58": "An error occurred while querying Wolfram Alpha",
        "59": "Say something to Wolfram",
        "60": "If you want to end the conversation with Wolfram, tell me",
        "61": "Do you want to go to a web page or do you prefer to search on Google?",
        "62": "What do you want me to search for on Google?",
        "63": "Write the web address where you want to go",
        "64": "Enter the phone number of the person to whom the message is addressed",
        "65": "Tell me your message",
        "66": "Sending message...",
        "67": "Message sent, if you want to keep sending messages to this number, give me the message below, if you want to end the conversation, just tell me",
        "68": "The number entered is invalid, please enter it again... the number, just in case",
        "69": "please try again",
    }
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
