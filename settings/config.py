# Constants ----------------------------------------------------------------
ASSISTANT_NAME = "Sharon"  # TODO:
INITIAL_CONTEXT = "Eres un asistente muy útil"
SPEECH_SPEED = 118
RESET_WORDS = ["reiniciar", "restablecer", "reactivar",]
EXIT_WORDS = ["adios", "adiós", "hasta luego", "chao", "nos vemos"]
FUNCTION_YOUTUBE = 'youtube'
FUNCTION_SPOTIFY = 'spotify'
FUNCTION_WIKIPEDIA = 'wikipedia'
FUNCTION_WOLFRAM = 'wolfram'
FUNCTION_WEB = 'web'
FUNCTION_EXIT = 'exit'
FUNCTION_RESET = 'reset'
FUNCTION_ASSISTANT = 'assistant'
BING_WAKE_WORDS = ["hola", "bing"]
GPT_WAKE_WORDS = ["chat", "chad"]
BARD_WAKE_WORDS = ["google", "bard", "asistente"]
BING_ASSISTANT_NAME = 'bing'
GPT_ASSISTANT_NAME = 'gpt'
BARD_ASSISTANT_NAME = 'bard'
BARD_SPECIFICATIONS = ". " + "responde de "
AUDIO_CAPTURE_MODES = {"listen": 'listen',
                       "ptt": 'push_to_talk'}
AUDIO_CAPTURE_MODE = AUDIO_CAPTURE_MODES["ptt"]
PUSH_TO_TALK_KEY = 'space'
RECORD_INTERVAL = 0.3
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
BARD_CONTEXT = "You are my personal assistant, you are very useful, as such, please respond in a very short, brief, concise, summarized paragraph and without further details to everything I tell you or ask from this moment on in the conversation."
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
                         "Tranquilo Robin, recuerda que debes dame la bati-señal",
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
                   f"¡{ASSISTANT_NAME} en acción! Listo/a para hacer tu vida más fácil y divertida",
                   f"¡Bienvenido de nuevo! {ASSISTANT_NAME}, tu asistente favorita, lista para ser tu compañera virtual",
                   f"¡Hola! {ASSISTANT_NAME}, el asistente más alegre, está aquí para darte una cálida bienvenida",
                   f"¡Saludos! {ASSISTANT_NAME} está encendida y lista para ponerle un toque especial a tu día",
                   f"¡Aquí viene {ASSISTANT_NAME}, el asistente con más chispa! Dispuesta a hacer de tu día algo extraordinario",
                   f"¡{ASSISTANT_NAME} al rescate! Tu asistente personal llena de energía, lista para enfrentar cualquier desafío",
                   f"¡Hola, hola! {ASSISTANT_NAME} está aquí para hacer brillar tu día con una mezcla de eficiencia y buen humor",
                   f"¡Saludos, amiguo! {ASSISTANT_NAME}, tu asistente personal, ya está aquí",
                   f"¡Hola! {ASSISTANT_NAME} al habla, preparado/a para hacerte sonreír y solucionar tus problemas con estilo",
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
                   f"{ASSISTANT_NAME} en acción! Listo/a para ser tu aliado tecnológico y tu fuente inagotable de buen rollo",
                   f"¡Hola! {ASSISTANT_NAME}, el asistente más entusiasta del mundo virtual, está a tu servicio",
                   f"¡Saludos! {ASSISTANT_NAME} está aquí para hacer de tu día algo extraordinario con su encanto tecnológico",
                   f"{ASSISTANT_NAME} al rescate! Tu asistente personal con el poder de convertir los desafíos en oportunidades",
                   f"¡Hola, hola! {ASSISTANT_NAME} está aquí para iluminar tu día y hacerte sentir como la estrella que eres",
                   ]
