import Modulo1

print ('Este código sirve para mostrar propagacion dinamica')	
elto = input('Ingresa clave para acceder al diccionario: ')
try:
	print ('El valor del elemento : '+ str(elto) + 'es: '+ str(Modulo1.elemento(elto)))
except IOError:
	print ('OJO! Está accediendo a un archivo que no existe. Pruebe de nuevo!')


