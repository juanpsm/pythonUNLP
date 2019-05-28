import PySimpleGUI as sg
#Armo el diseño de la interface
diseño = [ 
			[sg.Text('Ingresa tus datos')],
			[sg.Text('Nombre'), sg.InputText(),sg.Text('Nombre'), sg.InputText() ],			    
            [sg.Text('Tipo Doc'), sg.Listbox(values=('DNI','LE', 'PAS'), size=(30, 1)), sg.Text('Número'), sg.InputText()], 
            [sg.Text('fecha de Nac'), sg.InputText(),sg.Text('Nacionalidad'), sg.InputText() ],	      
            [ sg.Submit(), sg.Cancel()]
         ]
#La aplico a la ventana y la muestro
window = sg.Window('Datos Personales').Layout(diseño)
#Inicializo una tupla con los datos recibidos: botón apretado y datos ingresados
(boton_cliqueado, datos_ingresados) = window.Read()

print (boton_cliqueado, datos_ingresados)

