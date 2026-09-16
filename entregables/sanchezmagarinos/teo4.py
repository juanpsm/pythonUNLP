def sumo_parametros(*args):
	print('tupla donde guardo los argumentos:',args)
	return sum(args)
t=(2,2,3)
#print(sumo_parametros(t))  #da error por que no se puede sumar la tupla TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
# lo que hay que hacer es pasar varios argumentos, no una tupla propiamente dicha
print("sumo_parametros(2,2,3) = ",sumo_parametros(2,2,3))
print()

def imprimir_valores (**kwargs):
	for clave,valor in kwargs.items():
		print("el valor de {} es {}".format(clave,valor))
#test=dict([(x,chr(x)) for x in range(0,256)])
#print(test)
#imprimir_valores(test) #TypeError: imprimir_valores() takes 0 positional arguments but 1 was given
imprimir_valores(name='marco',ap='polo')
print()
print()


lista=[1,2,3,4,5,6,7,8,9]
print('Lista: ',lista)
print('\tmap: ',list(map(lambda x:2*x,lista)))
print('\tfilter: ',list(filter(lambda x:x%2==0,lista)))
print()
tupla=(1,2,3,4,5,6,7,8,9)
print('Tupla: ',tupla)
print('\tmap: ',list(map(lambda x:2*x,tupla)))
print('\tfilter: ',list(filter(lambda x:x%2==0,tupla)))
print()
conj={1,2,3,4,5,6,7,8,9}
print('Conjunto: ',conj)
print('\tmap: ',list(map(lambda x:2*x,conj)))
print('\tfilter: ',list(filter(lambda x:x%2==0,conj)))
print()
dicc={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i'}
print('Diccionario: ',dicc)
print('\tmap: ',list(map(lambda x:2*x,dicc)))
print('\tfilter: ',list(filter(lambda x:x%2==0,dicc)))
print()
cad='123456789'
print('Cadena: ',cad)
print('\tmap: ',list(map(lambda x:2*x,cad)))
#print('\tfilter: ',list(filter(lambda x:x%2==0,cad))) da error porque no esta definido % para string
print()

# las funciones reciben cualquier ITERABLE
