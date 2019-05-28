def cuentaLetra(s): #funcion para contar letras de las palabras y ademas marcarlas para sacarle la coma o el punto
	c = 0
	for L in s:
		if ((L != ',') and (L != '.')):
			c+=1
		else:
			c=-1
	return c

frase = 'Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar un montón de archivos con fotos de una manera compleja. Tal vez quieras escribir alguna pequeña base de datos personalizada, o una aplicación especializada con interfaz gráfica, o UN juego simple.'
lista = frase.lower().split(' ')

conj = set(lista) #de esta forma elimino automaticamente todos los repetidos
dicc={}
maxim=0

for palabra in conj:
	
	print(palabra)
	c = cuentaLetra(palabra)
	if c == -1 : # hay que sacar el ultimo char de la cadena y volver a contar
		conj.remove(palabra)
		palabra = palabra[:-1]  #para eso la saco del conj, la modifico y la vuelvo a agregar
		conj.add(palabra)
		c = cuentaLetra(palabra)
	print(c)
	if (c > maxim): #el maximosolo es para imprimir el diccionario en orden al final
		maxim = c
	if c in dicc:  #si ya existe la clave, le anexo la nueva palabra
		dicc[c].append(palabra)
	else:  #no existe asi que lo creo con una lista que tenga esa palabra
		dicc[c] = [palabra]
	print(dicc[c])
	print('-----------')
	

print('Dicc: ',dicc)
print()
print('Max: ',maxim)

for i in range(maxim+1):  #para imprimirmas lindo
  print(i, ' elementos --> ', dicc.get(i))



