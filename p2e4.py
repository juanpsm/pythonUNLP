import os
import time

def tamaño(arch):
	T=os.path.getsize(arch)
	B=' B '
	if T>1024:
		T=round(T/1024,2)
		B=' KB'
		if T>1024:
			T=round(T/1024,2)
			B=' MB'
			if T>1024:
				T=round(T/1024,2)
				B=' GB'
				if T>1024:
					T=round(T/1024,2)
					B=' TB'
	return str(T)+B+' '

def fecha(arch):
	return time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(float((os.path.getatime(x)))))
#for x in os.listdir('.'): #genera una lista con los "path" de la carpeta '.' (actual)
#    print(x)
#    print(os.path.getsize(x)) #tamaño en bytes
#    print(os.path.getatime(x)) #tiempo desde ultimo acceso (Unix epoch)

print('Contenido de "{}"'.format(os.path.abspath('.')))
formato_col='{:<20}|{:>13}|{:>30}'
print('-'*65)
print(formato_col.format('Nombre de archivo','tamaño ','fecha último acceso'))
print('-'*65)
#print(os.listdir('.'))
for x in sorted(os.listdir('.')): #ordeno por nombre.¿¿ como cambio key????
	#print(time.localtime(float(os.path.getatime(x)))) #convierto a float y luego a tiempo local (no anda sin float)
	#time.strftime("%a, %d %b %Y %H:%M:%S",time.localtime()) #formateo localtime
	#T=round(os.path.getsize(x)/1024,2)  #tam en kb
	print(formato_col.format(x,tamaño(x),fecha(x)))
