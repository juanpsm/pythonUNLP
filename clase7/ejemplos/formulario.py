import PySimpleGUI as sg

diseño = [ 
			[sg.Text('Ingresa tus datos')],
			[sg.Text('Nombre'), sg.InputText(),sg.Text('Nombre'), sg.InputText() ],			    
            [sg.Text('Tipo Doc'), sg.Listbox(values=('DNI','LE', 'PAS'), size=(30, 1)), sg.Text('Número'), sg.InputText()], 
            [sg.Text('fecha de Nac'), sg.InputText(),sg.Text('Nacionalidad'), sg.InputText() ],	      
            [ sg.Submit(), sg.Cancel()]
         ]

window = sg.Window('Datos Personales').Layout(diseño)
window.Read()

