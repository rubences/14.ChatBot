#-----------------------------------------------------------------------------------------

# Modulos necesarios:
#   NLTK 3.4.1
#
# Para instalar un módulo:
#   Haga clic en el menú File > Settings > Project:nombre_del_proyecto > Project interpreter > botón +
#   Introduzca el nombre del módulo en la zona de búsqueda situada en la parte superior izquierda
#   Elegir la versión en la parte inferior derecha
#   Haga clic en el botón install situado en la parte inferior izquierda
#-----------------------------------------------------------------------------------------




from __future__ import print_function

#Le sous module reflection permet de faire les liens entre les clés et les réponses à apporter
from nltk.chat.util import Chat, reflections


Cles_valeurs = (
        (
            r'Buenos días(.*)',
            (
                "Buenos días, hoy me alegro de hablar contigo",
                "¡Hola! ¿Qué novedades hay hoy?",
            ),
        ),
        (
            r'Necesito (.*)',
            (
                    "¿Por qué necesitas %1?",
                    "¿Te ayudaría de verdad %1?",
                    "¿Estás seguro/a de que necesitas %1?",
            ),
        ),
        (
            r'Por qué no (.*)',
            (
                "¿De verdad crees que no tengo 1 %?",
                "Quizás algún día, acabaré con %1."
                "¿De verdad quieres que haga 1 %?",
            ),
        ),
        (
            r'Porque no puedo (.*)',
            (
                "¿Crees que deberías ser capaz de %1?",
                "Si pudieras %1, ¿qué harías?",
                "No lo sé... ¿por qué no puedes pas %1?",
                "¿Lo has intentado de verdad?",
            ),
        ),
        (
            r'No puedo (.*)',
                (
                "¿Cómo sabes que no puedes %1?",
                "Si pruebas, quizás podrías hacer 1 %."
                "¿Qué te haría falta para tener 1 %?",
            ),
        ),
        (
            r'Soy (.*)',
            (
                "¿Has venido a verme porque eres %1?",
                "¿Cuánto tiempo hace que eres %1?",
                "¿Qué piensas de ser %1?",
                "¿Qué te hacer ser %1?",
                "¿Te gusta ser %1?",
                "¿Por qué me dices que eres 1 %?",
                "¿Por qué piensas que eres 1 %?",
            ),
        ),

        (
            r'Eres (.*)',
            (
                "¿Por qué es importante que yo sea %1?",
                "¿Preferirías que no fuera %1?",
                "Quizás crees que soy %1."
                "Quizás soy %1 -- ¿tú que piensas?",
            ),
        ),
        (
            r'Qué (.*)',
            (
                "¿Por qué haces esta pregunta?",
                "¿En qué te ayudaría una respuesta?",
                "¿Tú que piensas?",
            ),
        ),
        (
            r'Como (.*)',
            (
                "¿Cómo crees?",
                "Quizás puedas responder a tu propia pregunta."
                "¿Qué estás preguntando realmente?",
            ),
        ),
        (
            r'Porque (.*)',
            (
                "¿Es el verdadero motivo?",
                "¿Qué otros motivos se te ocurren?",
                "¿Este motivo se aplica a otra cosa?",
                "Si %1, ¿qué otras cosas deben ser verdad?",
            ),
        ),
        (
            r'(.*) lo siento (.*)',
            (
                "Hay muchas ocasiones en que no es necesario disculparse."
                "¿Qué sientes cuando te disculpas?",
            ),
        ),

        (
            r'Creo que (.*)',
            ("¿Dudas de %1?",
             "¿De verdad lo crees?",
             "¿Pero no estás seguro/a de %1?"),
        ),

        (
            r'Sí',
                 ('Me pareces muy seguro/a.',
                  "Vale, ¿puedes explicarme más?")
        ),
        (
            r'(.*) ordenador(.*)',
            (
                "¿De verdad hablas de mí?",
                "¿Te parece raro hablar con un ordenador?",
                "¿Cómo te sientes con los ordenadores?",
                "¿Te sientes amenazado por los ordenadores?",
            ),
        ),
        (
            r'Es que (.*)',
            (
                "¿Crees que es %1?",
                "Quizás es %1 -- ¿tú qué piensas?",
                "Si fuera %1, ¿tú qué harías?",
                "Podría muy bien ser %1.",
            ),
        ),
        (
            r'Es (.*)',
            (
            "Me pareces muy seguro/a.",
            "Si te dijera que probablemente no es %1, ¿qué sentirías?",
            ),
        ),
        (
            r'Puedes (.*)',
            (
                "¿Qué te hace pensar que no puedo hacer 1 %?",
                "Si pudiera %1, entonces ¿qué?",
                "¿Por qué me preguntas si puedo %1?",
            ),
        ),
        (
            r'Puedo (.*)',
            (
                "Quizás no querías %1.",
                "¿Quieres ser capaz de %1?",
                    "Si pudieras %1, ¿lo harías?",
            ),
        ),
        (
            r'Usted es (.*)',
            (
                "¿Por qué pienas que soy %1?",
                "¿Te gusta pensar que soy %1?",
                "Quizás no querrías que fuera %1.",
                "¿Quizás en realidad hablas de ti?",
                "¿Por qué dices que soy %1?",
                "¿Por qué piensas que soy %1?",
                "¿Hablamos de ti o de mí?",
            ),
        ),

    (
        r'Hasta luego',
        (
            "Gracias por haberme hablado.",
            "Hasta luego."
        ),
    ),
    (
        r'(.*)',
        (
            "Por favor, dime más.",
            "Cambiemos un poco de tema.... Háblame de ti.",
            "¿Puedes decirme más sobre este tema?",
            "¿Por qué dices eso?",
            "Ya veo.",
            "Muy interesante.",
            "Ya veo. ¿Cuéntame sobre eso?",
        ),
    ),
)


#Lanzamiento del programa

eliza_chatbot = Chat(Cles_valeurs, reflections)

print("Programa Eliza\n---------")
print('=' * 72)
print("Buenos días.  ¿Cómo estás?")

eliza_chatbot.converse()
