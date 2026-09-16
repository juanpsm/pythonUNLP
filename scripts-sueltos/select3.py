#para instalar usar:
#python -m pip install --upgrade pip setuptools wheel PySimpleGUI

import PySimpleGUI as sg
MAX = 8
lista1 = [22,55,66,55,44,55,88,7,4]
lista2 = [22,55,66,55,44,55,88,7,4]
lista3 = [22,55,66,55,44,55,88,7,4]
def_1 = 3
print(list(range(11, 17)))
layout = [
			[sg.Text('My one-shot window.')],	  
			[sg.InputText()],
			[sg.Combo( list( range( 0, 1 + min( MAX, len(lista1) ))), key = '_CANT_1_',
				 default_value = 0, size =(2,1),enable_events=True),
			 sg.Combo( list( range( 0, 1 + min( MAX, len(lista1) ))), key = '_CANT_2_',
				 default_value = 0, size =(2,1),enable_events=True),
			 sg.Combo( list( range( 0, 1 + min( MAX, len(lista1) ))), key = '_CANT_3_',
				 default_value = 0, size =(2,1),enable_events=True)
			],	  
			[sg.Submit(), sg.Cancel()]
		 ]
		 
window = sg.Window('Window Title').Layout(layout)	



while True:
	
	event, values = window.Read()	
	lista_cant = ['_CANT_1_','_CANT_2_','_CANT_3_']
	if event in lista_cant:
		if event == '_CANT_1_':
			lista_cant = ['_CANT_2_','_CANT_3_']
			print(lista_cant)
			for x in lista_cant:
				suma = MAX - int(values[event])
				window.Element(x).Update(values = list( range( 0, 1 + MAX - int(values[event]) ) ) )
		
		if event == '_CANT_2_':
			lista_cant = ['_CANT_3_']
			print(lista_cant)
			print(1 + MAX - int(values[event]) - int(values['_CANT_1_']))
			window.Element('_CANT_3_').Update(values = list( range( 0, 1 + MAX - int(values[event]) - int(values['_CANT_1_']) ) ) )
		elif event == '_CANT_3_':
			lista_cant = []
			print(lista_cant)
	print('MAX',MAX)
	print('Total = ',int(values['_CANT_1_'])+int(values['_CANT_2_'])+int(values['_CANT_3_']))
window.Close()

	
