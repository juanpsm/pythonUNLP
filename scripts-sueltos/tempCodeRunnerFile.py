if existe:
	dicc = {"15":[{'time':'asd','temp':'22','hum':'84'},{'time':'asd2','temp':'34','hum':'100'}]}
else:
	dicc = {}
	print('Creado de registro')
of = '15'
temp = '88'
hum = '111'
string_time = time.strftime("%Y/%m/%d - %H:%M:%S", time.gmtime(time.time()))

dicc[of].append({'time':of,'temp':temp,'hum':hum})

print(dicc)