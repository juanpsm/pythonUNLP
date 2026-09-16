#
#  uso_sort.py
#  

def uso_sorted1():
	usuarios_juego = [
		('Juan', 'Nivel1', 15),
		('Maria', 'Nivel1', 12),
		('Jose', 'Nivel2', 1020),
		('Ana', 'Nivel2', 1020),
	]

	return sorted(usuarios_juego, key=lambda usuario: usuario[0])

print(uso_sorted1())

