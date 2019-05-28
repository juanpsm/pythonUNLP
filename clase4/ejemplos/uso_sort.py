#
#  uso_sort.py
#  

def uso_sort(cadena):
	
	lista = cadena.split()
	
	print("Teniendo en cuenta mayúsculas y minúsculas")
	lista.sort()
	print(lista)
	
	lista.sort(key=str.lower)
	print("Sin tener en cuenta mayúsculas y minúsculas")
	print(lista)

def uso_sorted(cadena):
	
	print(sorted(cadena.split(), key=str.lower))


def uso_sorted1():
	usuarios_juego = [
		('Juan', 'Nivel1', 15),
		('Maria', 'Nivel1', 12),
		('Jose', 'Nivel2', 1020),
		('Ana', 'Nivel2', 1020),
	]
	return sorted(usuarios_juego)
	#return sorted(usuarios_juego, key=lambda usuario: usuario[0])

#uso_sort("Hoy puede ser un gran día. ")
#uso_sorted("Hoy puede ser un gran dia")
print(uso_sorted1())

