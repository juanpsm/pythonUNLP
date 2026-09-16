from pattern.es import verbs, tag, spelling, lexicon
import string
def clasificar(palabra):
	print( tag(palabra, tokenize=True, encoding='utf-8',tagset = 'UNIVERSAL'))
	print( tag(palabra, tokenize=True, encoding='utf-8'))
	print()


palabra = 'Camino'
print(palabra)
while palabra != 'q':
	if not palabra.lower() in verbs:
		if not palabra.lower() in spelling:
			if (not(palabra.lower() in lexicon) and not(palabra.upper() in lexicon) and not(palabra.capitalize() in lexicon)):
				print('No se encuentra en pattern.es')
			else:
				print('La encontró en lexicon')
				clasificar(palabra)
		else:
			print('La encontró en spelling')
			clasificar(palabra)
	else:
		print('La encontró en verbs')
		clasificar(palabra)
			
	print()
	palabra = input()
	
# ~ c = 0
# ~ for x in verbs:
	# ~ if not x in spelling:
		# ~ if not x in lexicon:
			# ~ print (x, end=', ')
			# ~ c+=1
		
# ~ print(c)
# ~ for x in lexicon:
	# ~ if x != x.lower():
		# ~ if x != x.upper():
			# ~ if x != x.capitalize():
				# ~ print(x,end=', ')
