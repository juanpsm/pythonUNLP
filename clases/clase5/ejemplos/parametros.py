#!/usr/bin/env python
# -*- coding: utf-8 -*-


def imprimo_elementos(uno, dos, tres, cuatro):
	'''Imprimo una tabla nombre-valor'''
	print( '{0}, {1}'.format(uno, dos))
		
def imprimo_elementos2(**argumentos):
	'''Imprimo una tabla nombre-valor'''
	for nombre, valor in argumentos.items():
		print( '{0} = {1}'.format(nombre, valor))		

def imprimo_elementos3(*argumentos):
	'''Imprimo una tabla nombre-valor'''
	for valor in argumentos:
		print( valor)	
	
tabla = { "uno": "I", "dos": "II", "tres": "III", "cuatro": "IV"}
tabla_numeros = { "uno": 1, "dos": 2, "tres":3, "cuatro": 4}


print("Envíola tabla como parámetro")
imprimo_elementos2(**tabla_numeros)
print("------------------")
print("Envío la lista de parámetros nombrados")
imprimo_elementos2( uno =1, dos = 2, tres = 3, cuatro = 4)

print("Envío de parámetros simples")
imprimo_elementos( uno ="I", dos = "II", tres = "III", cuatro = "IV")
print("------------------")
print("Accedo a los parámetros como una tupla")
imprimo_elementos3( 1,2,3,4)
