#frase = input('Ingrese la frase :')
frase = 'Split the string at the first occurrence of sep, and return a 3-tuple containing the part before the separator, the separator itself, and the part after the separator. If the separator is not found, return a 3-tuple containing the string itself, followed by two empty strings.'
#cadena = input('ingrese el string :')
cadena = 'string'
frase_alpha=frase.replace(',','').replace('.','').replace('?','')
print('frase_alpha = {}'.format(frase_alpha))
lista = frase_alpha.split(' ')
print('lista = {}'.format(lista))
c = 0
for e in lista:
	if e.casefold() == cadena.casefold():
		c=c+1
print('Se encontro "{}" {} veces'.format(cadena,c))


	

