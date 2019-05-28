# Basado en el ejemplo incluído en: http://inventwithpython.com/invent4thed/chapter5.html
 
import random
import time

def esperar(tiempo):
	time.sleep(tiempo)
	
def advertencia():
    print('''Estás entrando al bosque encantado. En este bosque hay árboles mágicos.
    ¡Cuidado al tocarlos!
    Algunos pueden hacerte rico o convertirte en piedra.
    Probá tu suerte.''')
    print()

def elegimos_arbol():
    arbol = ''
    while arbol != '1' and arbol != '2':
        print('¿Qué arbol vas a tocar? (1 o 2)')
        arbol = input()

    return arbol

def chequeamos_arbol(arbol_elegido):
    print('Has tocado el arbol {0:1s}'.format(arbol_elegido))
    esperar(1)
    print('Veamos cuál es tu suerte...')
    print()
    esperar(2)

    nuestra_suerte = random.randint(1, 2)

    if arbol_elegido == str(nuestra_suerte):
         print('¡Hoy es tu dia! ¡Ganaste una hoja de oro! ')
    else:
         print('Mmmm creo que hoy no es tu día :( ')

otra_vez = 'si'
while otra_vez == 'si' or otra_vez == 's':
	advertencia()
	arbol = elegimos_arbol()
	chequeamos_arbol(arbol)
	print('Seguimos jugando? (si o no)')
	otra_vez = input()
	
#En realidad salimos del juego cuando presionamos cualquier combnación distinta de si o s


