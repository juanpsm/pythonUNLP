x = 222222
def uno():
	x = 10
	def otra():
		x = 999
		def dos():
			global x
			print(x)
			x += 1
		dos()
	otra()
	print(x)
uno()
