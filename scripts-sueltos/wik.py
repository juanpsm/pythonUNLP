from pattern.es import lexicon, spelling,tag
# ~ from pattern.en import tokenize

def clasificar(palabra):
	print( tag(palabra, tokenize=True, encoding='utf-8',tagset = 'UNIVERSAL'))
	print( tag(palabra, tokenize=True, encoding='utf-8'))






# ~ print(dir(pattern.es))


 # ~ != tag(x, tokenize=True, encoding='utf-8',tagset = 'UNIVERSAL')[0][1]:


# ~ lista = list(pattern.es.lexicon.keys())
# ~ mas_largo = max(lista, key=len)
# ~ print(mas_largo,' - ', len(mas_largo))

# ~ from collections import Counter
# ~ c = Counter(lexicon.values())

# ~ print(c)

# ~ c= 0
# ~ for x in lexicon:
	# ~ if x in spelling:
		# ~ c+=1
		# ~ print(x, end=', ')

# ~ print('Total =',len(spelling)+len(lexicon))

# ~ print('Repetidos =',c)

palabra = 'azucar.'

if not palabra in spelling:
	if not palabra in lexicon:
		print('no se encuentra en pattern.es')
	else:
		print('lexicon')
		clasificar(palabra)
else:
	print('spelling')
	clasificar(palabra)
