print('\n Condicionales ternarios \n')
condition = True
x = 1 if condition else 0
print (x)

print('\n Underscore Placeholders \n')
x = 1_000_000
y = 1000000
print ('x==y ?',x==y)

print('\n Enumerate \n')
names = ['lala', 'lele', 'lolo', 'lulu']
for index, name in enumerate(names):
	print (index, name)

print('\n Zip \n')
#devuelve una tupla de los valores con igual indice de listas 
namex = ['lalax', 'lelex', 'lolox', 'lulux']
namey = ['lalay', 'leley', 'loloy', 'luluy']
namez = ['lalaz', 'lelez', 'loloz', 'luluz', 'papirulo']

for x,y,z in zip(namex,namey,namez):
	print(f' primero {x}  segundo {y} y tercero {z}')

for value in zip(namex,namey,namez):
	print(value) # imprime la tupla
#ojo zip corta cuando se termina la lista mas corta

print('Unpacking \n')

a, b = (1, 2)
print('a = ',a,'b = ',b)

# necesitamos el mismo numero de items de ambos lados
# con * ponemos todo en c excepto el ultimo que va a d
a, b, *c, d = (1,2,3,4,5)
print('a = ',a,'b = ',b,'c = ',c,' d = ',d)

print('\n IGNORE VARIABLE (convención) \n')

a, _ = (1, 2)
print(a, ' ', _) #anda como vaiable pero es convencion que esa var no la vamo a usar

print('\n Getpass \n')
from getpass import getpass
#uname = input('Username: ')
password= '0'#getpass('Password: ')
pw = ''
for x in password:
	pw += '*'
print (pw)

print('\n PRINT \n')
a = 5
print("a =", a, sep='00000', end='\n\n\n', flush = True)
print("a =", a, sep='0', end='')

print('''
python -m es para correr modulos
corre todo lo que pones despues de la m como si estuviera en el path
python -m password.py va sin el .py porque necesita el nombre del modulo solamente
''')

print('\n HELP \n')

import random
#con esto se muestra toda la documentacion
#help(random)
from datetime import datetime
print('\n dir(datetime): \n')
print(dir(datetime)) #list of valid attributes and methods for the object
print('\n datetime.today :',datetime.today)#asi vemos que es un METODO, neceita parentesis
print('\n datetime.today() :',datetime.today())
