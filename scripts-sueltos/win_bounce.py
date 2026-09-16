# -*- coding: utf-8 -*-
import PySimpleGUI as sg
import random
import math
import time

def dibujar():
	tam = 50
	layout = [[sg.Button('GO!')]]
	window = sg.Window('Cascada',size = (tam,tam)).Layout(layout)

	while True:				 # Event Loop
		event, val = window.Read()
		#print(event, val)

		if event is None or event == 'Cerrar':
			break
		if event == 'GO!':
			# ~ window.SetAlpha(0.5)
			x_max,y_max = window.GetScreenDimensions()
			for rep in range(1):
				margen = tam
				x_0, y_0 =  random.randrange(x_max-margen), random.randrange(y_max-margen)
				# ~ x_0, y_0 = 555,450
				v_x = random.randrange(1,10)
				v_y = random.randrange(1,10)
				# ~ v_x, v_y = 10,10

				t = 0
				rebote = 0
				x,y=x_0,y_0
				
				while rebote < 80:
					x = x + v_x
					y = y + v_y
					
					rand_col = ['#'+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
									for i in range(4)]
					# ~ sg.PopupNoButtons('WIN',
							# ~ button_color = (rand_col[0],rand_col[1]),					# Color of buttons (text_color, background_color)
							# ~ background_color = rand_col[2],				# Color of background
							# ~ text_color = rand_col[3], 					# Color of text
							# ~ auto_close = True,					# If True window will automatically close
							# ~ auto_close_duration = 5,			# Number of seconds for autoclose
							# ~ non_blocking = True,					# If True returns immediately
							# ~ line_width = 15,						# Width of lines in characters
							# ~ font = None,							# Font to use for characters
							# ~ no_titlebar = False,					# If True no titlebar will be shown
							# ~ grab_anywhere = False,					# If True can move window by grabbing anywhere
							# ~ keep_on_top = True,					# If True window will be on top of other windows
							# ~ location = (x,y)					# (x,y) coordinates to show the window
						# ~ )
					window.Move(x,y)
					window.Refresh()
					
					if x < 0:
						v_x = -1*v_x
					elif y < 0: 
						v_y = -1*v_y
					elif x > x_max-margen:
						v_x = -1*v_x
					elif y > y_max-margen:
						v_y = -1*v_y
					t+=1
			# ~ sg.Popup('GANASTE', keep_on_top=True)
			# ~ window.Reappear()  

if __name__ == "__main__":
	dibujar()
