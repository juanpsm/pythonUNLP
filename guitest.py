#para instalar usar:
#python -m pip install --upgrade pip setuptools wheel PySimpleGUI

import PySimpleGUI as sg      

layout = [[sg.Text('My one-shot window.')],      
                 [sg.InputText()],      
                 [sg.Submit(), sg.Cancel()]]      

window = sg.Window('Window Title').Layout(layout)    

event, values = window.Read()    
window.Close()

text_input = values[0]    
print(text_input)
