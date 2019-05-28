#Utilizo una función que genera números aleatorios en un cierto rango
import random
numero_compu = random.randrange(100)

#Pido ingresar el número al usuario
ingresa_numero = int (input('Ingresa el número que pensó la compu en un rango de 0 a 99. '))

#Evalúo si es le número generado por la computadora
if ingresa_numero == numero_compu:
    print ('Ganaste!')
else:
    print ('Perdiste la compu pensó en el número:', numero_compu, 'intenta nuevamente')
