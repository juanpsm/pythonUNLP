dic = {1:'Juan', 2:'Ana', 5:'Helena'}

try:
	for x in range(1,6):
		print (dic[x])
except (KeyError):
	dic[x] = 'Agregado'
else:
	print ('Se recorrió el diccionario y NO se agregaron valores')
print ("El diccionario al final del proceso es: ", dic)
		


	
