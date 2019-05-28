import PySimpleGUI as sg  

sg.ChangeLookAndFeel('LightGreen')


datos_layout = [[ sg.T('Ingrese los datos del jugador:') ],
		  [sg.T('Nombre', size=(15, 1)), sg.In(key='_NOMBRE_',do_not_clear=False) ],      
          [sg.T('Apellido', size=(15, 1)), sg.In(key='_APELLIDO_',do_not_clear=False)],      
          [sg.T('Puntaje', size=(15, 1)), sg.In(key='_PUNTAJE_',do_not_clear=False) ],
          [sg.Button('Agregar'), sg.Exit()]
		]
main_layout = [[sg.Frame('Nuevo jugador', datos_layout)],
			   [sg.Listbox(values=[1,2,3],key='_LIST_', size=(30, 6))],
			   [sg.T('Cantidad de jugadores:'),sg.T('',key='Cant')]
			   ]

    
window = sg.Window('Ejercicio 1 PySimpleGUI',main_layout)

jugadores=[]
while True:
	event, valores = window.Read()
	
	if event is None or event == 'Exit':
		break      
	# ~ if event == 'Agregar':
		# ~ jugadores.append(valores)
		# ~ window.FindElement('Cant').Update(len(jugadores))
		# ~ window.FindElement('_LIST_').Update(values['_APELLIDO_'])
	print(valores)
print(jugadores)


# event, values = window.Read()

# sg.Popup('La GUI devolvió:', event, values)
