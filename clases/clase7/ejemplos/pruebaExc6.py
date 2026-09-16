dic = {1:'Juan',4:'Pedro',5:'Helena'}
y = 9
try:
	print ('Vamos a entrar a otro bloque TRY')
	
	try:
		for x in range(1,6):
			print (dic[z])
	except (KeyError):
		dic[x] = 'Agregado'
	
	y = y + 1
	print ('El valor de y es:' + str(y))
except(NameError):
	print ('OJO! Se esta usando una variable que no existe')

print ('Se sigue con las siguientes sentencias del programa')

	

