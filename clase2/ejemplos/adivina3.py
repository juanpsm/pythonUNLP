#Utilizo una función que genera números aleatorios en un cierto rango
import random
numero_compu = random.randrange(100)

#Inicializo la variable que cuenta la cantidad de oportunidades y comienzo
#con el juego
cont = 1
while cont < 11:
	#Pido ingresar el número al usuario
	ingresa_numero = int(input('Ingresa el número que pensó la compu en un rango de 0 a 99. '))
	
	#Evalúo si es le número generado por la computadora
	if ingresa_numero == numero_compu:
		print ('Ganaste! y lo hiciste en', cont, 'intentos!')
		cont = 13
	#Pregunto si el número está en un rango de 10
	elif ingresa_numero - numero_compu > -10  and ingresa_numero - numero_compu < 10:
		print ('No es ese número. Estás cerca. Sigue pensando..')
	#Si no está cerca...
	# se informa si el número pensado por la computadora es más chico o..
	elif ingresa_numero > numero_compu:
		print ('No es ese número. No estás cerca, el número es mas chico .Sigue pensando..')		
	# es más grande...
	else:
		print ('No es ese número. No estás cerca, el número es mas grande .Sigue pensando..')
	cont = cont + 1
       
#Consulto si uso todos los intentos..
if cont == 11:
    print ('\n Perdiste :(\n La compu pensó en el número:', numero_compu)
