
def vocales(cadena):
	print( list(filter(lambda l: l.lower() in "aeiou", cadena)))



if __name__ == "__main__":
    import sys
    vocales(sys.argv[1])

