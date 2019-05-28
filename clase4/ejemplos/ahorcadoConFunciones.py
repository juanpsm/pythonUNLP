# Las imágenes del ahorcado fueron sacadas del ejemplo incluído en: http://inventwithpython.com/invent4thed/chapter9.html

import random
ahorcado = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O]  |
 /|\  |
 / \  |
     ===''']


#Defino conjunto de palabras a trabajar por temas
palabras = {1:['gato', 'perro','pato','elefante','lobo'],
            2:['rojo','azul','verde','amarillo'], 
            3:['milanesa','pure','pizza','salchicha']
            }


def defino_palabra(palabras):
	''' Esta función retorna la palabra a adivinar.'''
	
	#Pido que el jugador elija un tema
	tema = int(input('Elige un tema:\n 1: animales\n 2: colores\n 3: comidas\n '))
	
	#Selecciono la palabra a trabajar
	pal = palabras[tema][random.randrange(len(palabras[tema]))]
	
	return pal
    
   
def muestro_tablero(letras_correctas, cantidad_partes_cuerpo, pal_secreta):
	''' Esta  función muestra el tablero de acuerdo al estado del juego'''
	
	print(ahorcado[cantidad_partes_cuerpo])
	print()
	
	pal_separada = '_' * len(pal_secreta)
	
	for i in range(len(pal_secreta)): # reemplaza los guines por las letras correctas
		if pal_secreta[i] in letras_correctas:
			pal_separada = pal_separada[:i] + pal_secreta[i] + pal_separada[i+1:]
			
	for letra in pal_separada: # muestra la palabra con los espacios que faltan completar
		print(letra, end=' ')

   
   
def jugada():
	''' Obtiene la letra que el jugador ingrese'''
	
	letra = input('Ingresa una letra: ')
	return letra.lower()


	
#Selecciono la palabra a trabajar
pal_secreta = defino_palabra(palabras)

cantidad_partes_cuerpo = 0
letras_correctas = ''

#comienza el juego
sigue = True

while sigue:
	
	muestro_tablero(letras_correctas, cantidad_partes_cuerpo, pal_secreta)
	
	letra = jugada()
	
	# Si hay al menos una aparición de la letra..
	if letra in pal_secreta:
		letras_correctas = letras_correctas + letra
		
		# Chequeamos si ganó
		gane = True
		i = 0
		while gane and i < len(pal_secreta):
			if pal_secreta[i] not in letras_correctas:
				gane = False
			i = i + 1
			
		if gane:
			print('Ganaste')
			muestro_tablero(letras_correctas, cantidad_partes_cuerpo, pal_secreta)
			sigue = False

	else:
		#si se equivocó completo el cuerpo
		cantidad_partes_cuerpo=cantidad_partes_cuerpo + 1
		
		if cantidad_partes_cuerpo == len(ahorcado):
			print ('Perdiste!. La palabra era:', pal_secreta)
			sigue = False
			
		
		
		
			
	
