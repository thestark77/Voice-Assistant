# Constants ----------------------------------------------------------------
INITIAL_CONTEXT = "Eres un asistente muy útil"
SPEECH_SPEED = 118
BING_WAKE_WORDS = ["hola", "bing"]
GPT_WAKE_WORDS = ["chat", "chad", "asistente"]
RESET_WORDS = ["reiniciar", "restablecer", "reactivar",]
EXIT_WORDS = ["adios", "adiós", "hasta luego", "chao", "nos vemos"]
AUDIO_CAPTURE_MODES = {"listen": '\033[95m',
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
ACTIVATION_PHRASES = ["¡Hola! ¿En qué puedo ayudarte hoy?",
                      "¡Saludos! Estoy aquí para asistirte",
                      "¡Encantada de estar a tu servicio!",
                      "Lista para responder dudas",
                      "¿En qué puedo servirte?",
                      "¡Qué gusto escucharte!",
                      "¿Qué puedo hacer por ti hoy?",
                      "Soy todo oídos",
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
