#Utilizo una función que genera números aleatorios en un cierto rango
import random
numero_compu = random.randrange(100)

#Inicializo la variable que cuenta la cantidad de oportunidades y comienzo
#con el juego

cont=1
while cont < 11:
	#Pido ingresar el número al usuario
	ingresa_numero = int(input('Ingresa el número que pensó la compu en un rango de 0 a 99. '))
	
	#Evalúo si es le número generado por la computadora
	if ingresa_numero == numero_compu:
		print ('Ganaste! y lo hiciste en', cont, 'intentos!')
		cont = 13
	else:
		print ('No.. ese número no es... Sigue pensando..')
		cont = cont + 1
       
#Consulto si uso todos los intentos..
if cont == 11:
    print ('\n Perdiste :(\n La compu pensó en el número:', numero_compu)
