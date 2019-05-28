import random

colores = ['azul','amarillo','rojo','blanco','negro']
coordenadas = [(2,3),(5,6),(8,8),(10,2),(-5,-8)]
#print(len(colores))
#indice = random.randrange(len(colores))
#print(colores[indice])  #puedo hacerlo de una
print('Color al azar: ',colores[random.randrange(len(colores))])
print('Color al azar (método): ',random.choice(colores))

con_repeticion = {t:colores[random.randrange(len(colores))] for t in coordenadas}

print('Con Repeticion: ',con_repeticion)
print()

sinrep={}
conj_col=set(colores) #no es necesario, pero por si ya estaban repetidos los colores en la lista
for t in coordenadas:
	sinrep[t] = random.choice(tuple(conj_col))  #no se puede usar el metodo directamente sobre un conjunto, hay que copiarlo a una tupla.
	conj_col.remove(sinrep[t])    #habria que ver como hacerlo en una linea porque necesito ir guardando el conjunto reducido

print('Sin Repeticion: ',sinrep)	
print()	


#sin_repeticion = {t:colores[random.randrange(len(colores))] for t in coordenadas}
#print('Sin Repeticion',sin_repeticion)
