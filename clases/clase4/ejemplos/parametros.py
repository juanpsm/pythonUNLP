
def imprimo_elementos(uno, dos, tres, cuatro):
	'''Imprimo los valores de los dos primeros parámetros'''
	print( '{0}, {1}'.format(uno, dos))
		
def imprimo_elementos2(**argumentos):
	'''Imprimo una tabla nombre-valor'''
	for nombre, valor in argumentos.items():
		print( '{0} = {1}'.format(nombre, valor))		

def imprimo_elementos3(*argumentos):
	'''Imprimo los valores de los argumentos'''
	for valor in argumentos:
		print( valor)	
	
tabla = { "uno": "I", "dos": "II", "tres": "III", "cuatro": "IV"}
tabla_numeros = { "uno": 1, "dos": 2, "tres":3, "cuatro": 4}


print("Invoco a imprimo_elementos2 con  tabla_numeros como parámetro")
imprimo_elementos2(**tabla_numeros)
print("------------------")

print("Invoco a imprimo_elementos2 con los parámetros nombrados")
imprimo_elementos2( uno =1, dos = 2, tres = 3, cuatro = 4)
print("------------------")

print("Invoco a imprimo_elementos con  parámetros nombrados")
imprimo_elementos( uno ="I", dos = "II", tres = "III", cuatro = "IV")

print("------------------")

print("Invoco a imprimo_elementos con  parámetros simples")
imprimo_elementos( "I", "II", "III", "IV")

print("------------------")
print("Invoco a imprimo_elementos3 con  parámetros simples")
imprimo_elementos3( 1,2,3,4)
