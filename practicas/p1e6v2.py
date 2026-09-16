
#la idea era hacer lomismo pero limpiar el conuntodecomas ypuntos previamente

def cuentacar(s):  #cuenta cualquier caracter hay que limpiar la cadena antes
	c = 0
	for L in s:
		c+=1
	return c

frase = 'Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar un montón de archivos con fotos de una manera compleja. Tal vez quieras escribir alguna pequeña base de datos personalizada, o una aplicación especializada con interfaz gráfica, o UN juego simple.'
lista = frase.upper().replace(',','').replace('.','').replace('?','').split(' ')

conj = set(lista)
dicc={}
maxim=0
for palabra in conj:
	
	print(palabra)
	c = cuentacar(palabra)
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
  
print('palabras con12 letras. ',dicc[12])
