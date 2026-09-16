# -*- coding: utf-8 -*-
import PySimpleGUI as sg
import random
import math
import time

def dibujar():

	layout = [[sg.Button('GO!')]]
	window = sg.Window('Cascada').Layout(layout)

	while True:				 # Event Loop
		event, val = window.Read()
		#print(event, val)

		if event is None or event == 'Cerrar':
			break
		
		window.SetAlpha(0.5)
		x_max,y_max = window.GetScreenDimensions()
		
		# ~ def spiral(t):
			# ~ t = (t-200)
			# ~ a = 10
			# ~ b = 0.035
			# ~ x = a * math.exp(b*t) / math.cos(t)
			# ~ y = a * math.exp(b*t) / math.sin(t)
			# ~ return x, y

		for rep in range(5):
			margen = 150
			x_0, y_0 =  random.randrange(x_max-margen-50), random.randrange(y_max-margen-50)
			# ~ x_0, y_0 = 555,450
			sign = random.choice([-1,1])
			v_x = sign*random.randrange(1,50)
			
			v_y = -1*random.randrange(1,80)
			# ~ v_x, v_y = 10,10


			g = 5
			t = 0
			rebote = 0
			x,y=x_0,y_0
			
			while rebote < 3 and t < 500:
				x = x + v_x
				v_y = v_y + g
				y = y + v_y
				
				rand_col = ['#'+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
								for i in range(4)]
				# ~ print(rand_col)## ['#C7980A', '#F4651F', '#82D8A7', '#CC3A05', '#575E76', '#156943', '#0BD055', '#ACD338']
				sg.PopupNoButtons('WIN',
						button_color = (rand_col[0],rand_col[1]),					# Color of buttons (text_color, background_color)
						background_color = rand_col[2],				# Color of background
						text_color = rand_col[3], 					# Color of text
						# ~ button_type = 'POPUP_BUTTONS_NO_BUTTONS',
						auto_close = True,					# If True window will automatically close
						auto_close_duration = 5,			# Number of seconds for autoclose
						non_blocking = True,					# If True returns immediately
						# ~ icon = DEFAULT_WINDOW_ICON,				# Icon to use on the taskbar
						line_width = 15,						# Width of lines in characters
						font = 'Fixedsys ',							# Font to use for characters
						no_titlebar = False,					# If True no titlebar will be shown
						grab_anywhere = False,					# If True can move window by grabbing anywhere
						keep_on_top = True,					# If True window will be on top of other windows
						location = (x,y)					# (x,y) coordinates to show the window
					)
				
				if x < 0:
					v_x = -1*v_x
				elif y < 0: 
					v_y = -1*v_y
				elif x > x_max-margen:
					v_x = -1*v_x
				elif y > y_max-margen:
					rebote +=1
					v_y = -1*v_y
				t+=0.5

			# ~ def cascade(a, b, t):
			# ~ x = t - b
			# ~ y = a * (t - b)**2
			# ~ print(a, b, x, y)
			# ~ return x,y
		# ~ for rep in range(5):
			# ~ x_0 = random.randrange(x_max)
			# ~ y_0 = random.randrange(y_max)
			# ~ sign = random.choice([-1,1]) ## derecha o izq
			# ~ a = 0.001 + 0.05 * random.random() # factor cuadrático
			# ~ b = random.randrange(10,100) ## corrimiento
			# ~ t = 0.01  ## slider
			# ~ print(x_0,y_0,':',t)
			# ~ x = 0
			# ~ y = 0
			# ~ while x >= 0 and y >= 0 and x < x_max and y < y_max:
								
				
				# ~ delta_x, delta_y = cascade(a,b,t)
				
				# ~ x = x_0 + delta_x * sign
				# ~ y = y_0 + delta_y
				# ~ t += 10
				# ~ print('--> x ',x,'y ',y,'t ',t)
				# ~ rand_col = ['#'+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
								# ~ for i in range(4)]
				# ~ print(rand_col)## ['#C7980A', '#F4651F', '#82D8A7', '#CC3A05', '#575E76', '#156943', '#0BD055', '#ACD338']
				# ~ sg.Popup('WIN',
						# ~ button_color = (rand_col[0],rand_col[1]),					# Color of buttons (text_color, background_color)
						# ~ background_color = rand_col[2],				# Color of background
						# ~ text_color = rand_col[3], 					# Color of text
						# ~ button_type = 'POPUP_BUTTONS_NO_BUTTONS',
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
				
				



if __name__ == "__main__":
	dibujar()
