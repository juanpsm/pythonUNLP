
def dividir (x,y):
	try:
		return x / y
	
	except ZeroDivisionError:
		print ('¡Division por CERO!')
		return 'Indefinido'
	finally:
		print('Ha FINALIZADO la ejecucion del modulo')
		
x = int(input('Ingresa el dividendo: '))
y = int(input('Ingresa el divisor: '))
result = dividir(x,y)
print ('La division es', result)

	
