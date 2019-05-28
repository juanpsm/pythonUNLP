import PySimpleGUI as sg      

sg.Popup('Mi  primera ventanita', button_color=('black', 'red'))
			   
sg.PopupYesNo('Mi  primera ventanita', button_color=('black', 'green'))

sg.PopupOKCancel('Mi  primera ventanita', button_color=('black', 'grey'))

texto = sg.PopupGetText('Titulo', 'Ingresá algo')      
sg.Popup('Resultados', 'Ingresaste el siguiente texto: ', texto)

