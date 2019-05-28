import PySimpleGUI as sg
#Armando una columna

columna_1 =  [ 
			[sg.Text('Nombre'), sg.InputText()],
			[sg.Text('Apellido'), sg.InputText() ]
			]
columna_2 = [
			[sg.Text('Tipo Doc'), sg.Listbox(values=('DNI','LE', 'PAS'), size=(30, 1))],
			[sg.Text('Número'), sg.InputText()],
			[sg.Text('Nacionalidad'), sg.InputText()]
			
			]
#Armo el diseño de la interface
diseño = [ 
			[sg.Text('Ingresa tus datos')],
			[sg.Column(columna_1), sg.Column(columna_2)],
			[ sg.Submit(), sg.Cancel()]		
         ]
#La aplico a la ventana y la muestro
window = sg.Window('Datos Personales').Layout(diseño)
#Inicializo una tupla con los datos recibidos: botón apretado y datos ingresados
(boton_cliqueado, datos_ingresados) = window.Read()

print (boton_cliqueado, datos_ingresados)

