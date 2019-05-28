import PySimpleGUI as sg      

sg.ChangeLookAndFeel('Dark')      

# layout = [[sg.Listbox(values=('Item 1', 'Item 2', 'Item 3'), background_color='yellow', size=(20,3)),      
		  # [sg.Input('Last input')], 
		  #[sg.ColorChooserButton("  Elegi color")],  
		  # [sg.OK()]]      


layout = [[sg.Input('Ingresa algo')], 
		  [sg.Listbox(values=('Item 1', 'Item 2', 'Item 3'))],   
		  [sg.OK()]] 
		   	
event, values = sg.Window('Elementos básicos').Layout(layout).Read()  

sg.Popup(event, values, line_width=200)      
