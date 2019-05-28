import random

#Preparo el juego

#Defino conjunto de palabras a trabajar por temas
palabras = {1:['gato', 'perro','pato','elefante','lobo'], 2:['rojo','azul','verde','amarillo'], 3:['milanesa','pure','pizza','salchicha']}

#Defino estructura del ahoracado
ahorcado = [' O ', '/|\\','/ \\']

#Comienza el proceso del juego
#Pido que el jugador elija un tema
tema = int(input('Elige un tema:\n 1: animales\n 2: colores\n 3: comidas\n '))

#Selecciono la palabra a trabajar
pal = palabras[tema][random.randrange(len(palabras[tema]))]


#armo la estructura de la palabra sobre la cuál se irá armando con las letras 
#que se ingresen. Comienza con tantas rayas como letras tiene la palabra a adivinar
pal_separada = []
for y in pal:
	pal_separada.append(['_ '])

#Muestro por pantalla tantas rayas como letras tenga la palabra a adivinar
print ('- '*len(pal))

#inicializo variables que permiten saber si se ganó o perdió
cantidad_letras_adivinadas = 0
cantidad_partes_cuerpo = 0

#comienza la interacción con el jugador
sigue = True
while sigue:
	#introducción de letras por parte del jugador
	letra = input('Ingresa una letra: ').lower()
	# Si hay al menos una aparición de la letra..
	if letra in pal:
		
		#Guardo las posiciones donde se encuentra		
		for pos in range(len (pal)):
			
			if pal[pos] == letra:
				pal_separada[pos] = letra				
				cantidad_letras_adivinadas = cantidad_letras_adivinadas + 1
			
		#armo la palabra a mostrar al jugador con su letra elegida
		pal_imprime = ''
		for y in pal_separada:
			pal_imprime = pal_imprime + y[0]
		print (pal_imprime)
		#averiguo si terminó o debe continuar
		if cantidad_letras_adivinadas == len(pal):
			print ('Ganaste')
			sigue = False
		
	else:
		#si se equivocó completo el cuerpo
		cantidad_partes_cuerpo=cantidad_partes_cuerpo + 1
		for x in range(cantidad_partes_cuerpo):
			print (ahorcado[x])
		if cantidad_partes_cuerpo == 3:
			print ('Perdiste!. La palabra era:', pal)
			sigue = False
			
		
		
		
			
	
