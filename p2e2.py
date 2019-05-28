# coding=utf-8
import random
import traceback
def debug(__x):
	print (traceback.extract_stack(limit=2)[0][3][6:][:-1],"=",__x,', type:',type(__x))
	

def suma():
	rango=5
	x=random.randrange(rango)
	y=random.randrange(rango)
	print('Procedimiento Suma:')
	if  int(input('{} + {} = '.format(x,y)))== x+y:
		print('Correcto!')
	else:
		print('Mal...')
	print()
	
	
def acentos():
	print('Procedimiento Acento:')
	palabras = [('grave',['molesto','boleto']), ('aguda',['ratón','camión']),('esdrújula',['murciélago','brújula'])]
	tupla_aleatoria = random.choice(palabras)
	#print('tupla_aleatoria ',tupla_aleatoria)
	palabra_aleatoria = random.choice(tupla_aleatoria[1])  #elijo random de la lista de palabras que es el segundo elemente (1) de la tupla
	#print('palabra_aleatoria ',palabra_aleatoria)
	#print('tipo palabra_aleatoria ',type(palabra_aleatoria))

	#palabra_aleatoria  = random.choice(random.choice(palabras)[1]) #sirve pero pierdo la "llave" de la tupla
	
	respuesta = int(input('Indique la acentuación de "{}" \n1. {}, 2. {}, 3. {}: '.format(palabra_aleatoria,palabras[0][0],palabras[1][0],palabras[2][0])).lower()) #el lower quedo de cuando no tenia opciones
	#print('tipo respuesta ',type(respuesta))
	#debug(tupla_aleatoria[0])
	if palabras[respuesta-1][0] == tupla_aleatoria[0]:  #la "key" es el primer elemento de la tupla
		print('Correcto!')
	else:
		print('Mal...')
	print()

colores = ['azul','amarillo','rojo','blanco','negro']
coordenadas = [(2,3),(5,6),(8,8),(10,2),(-5,-8)]
con_repeticion = {t:random.choice(colores) for t in coordenadas}
sinrep={}
conj_col=set(colores) #no es necesario, pero por si ya estaban repetidos los colores en la lista
for t in coordenadas:
	sinrep[t] = random.choice(tuple(conj_col))  #no se puede usar el metodo directamente sobre un conjunto, hay que copiarlo a una tupla.
	conj_col.remove(sinrep[t])    #habria que ver como hacerlo en una linea porque necesito ir guardando el conjunto reducido

criterio1 = colores[:2]
criterio2 = colores[-2:]
criterio3 = colores[2:-2] #al pedo
print('colores = ',colores)
print()
print('Si la coord:\n esta en {}, sumo \n esta en {}, acentos \n y si no ({}), no hago nada'.format(criterio1,criterio2,criterio3))
print()
for t in coordenadas:
	if sinrep[t] in criterio1:
		print('Coord. {} -> {}'.format(t,sinrep[t]))
		suma()
	elif sinrep[t] in criterio2:
		print('Coord. {} -> {}'.format(t,sinrep[t]))
		acentos()
