import traceback
def debug(__x):
	'''Devuelve el nombre_var = valor_var, type: tipo_var'''
	print (traceback.extract_stack(limit=2)[0][3][6:][:-1],"=",__x,', type:',type(__x))

a=[5]; b={3}
debug(a)
debug (b)
for i in range(0,20,3):
	debug(i)
