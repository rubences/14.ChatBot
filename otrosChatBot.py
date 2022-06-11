#-----------------------------------------------------------------------------------------

# 
# Modulos necesarios:
#   NLTK 3.4.1
#
# Para instalar un módulo:
#   Haga clic en el menú File > Settings > Project:nombre_del_proyecto > Project interpreter > botón +
#   Introduzca el nombre del módulo en la zona de búsqueda situada en la parte superior izquierda
#   Elegir la versión en la parte inferior derecha
#   Haga clic en el botón install situado en la parte inferior izquierda
#-----------------------------------------------------------------------------------------
#
#  Código procedente de la documentación del módulo NLTK:
#          https://www.nltk.org/_modules/nltk/chat.html
#  
#-----------------------------------------------------------------------------------------


from __future__ import print_function

from nltk.chat.util import Chat
from nltk.chat.eliza import eliza_chat
from nltk.chat.iesha import iesha_chat
from nltk.chat.rude import rude_chat
from nltk.chat.suntsu import suntsu_chat
from nltk.chat.zen import zen_chat

bots = [
    (eliza_chat, 'Eliza (Psiquiatra)'),
    (iesha_chat, 'Iesha (Adolescente drogadicto)'),
    (rude_chat, 'Rude (ChatBot incorrecto)'),
    (suntsu_chat, 'Suntsu (Proverbios chinos)'),
    (zen_chat, 'Zen (Perlas de sabiduría)'),
]


def chatbots():
    import sys

    print('¿Qué chatBot quiere probar?')
    botcount = len(bots)
    for i in range(botcount):
        print('  %d: %s' % (i + 1, bots[i][1]))
    while True:
        print('\nElija su chatBot 1-%d: ' % botcount, end=' ')
        choice = sys.stdin.readline().strip()
        if choice.isdigit() and (int(choice) - 1) in range(botcount):
            break
        else:
            print('   Error: Este chatBot no existe')

    chatbot = bots[int(choice) - 1][0]
    chatbot()

chatbots()