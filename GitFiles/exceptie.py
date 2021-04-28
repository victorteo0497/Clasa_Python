#!/usr/bin/python3

try:
	f = open("Sortare_dictionare.py", "r")

	s = f.read()

	print(s)
except 	FileNotFoundError:
	print("Ceva nu este bine. Probabil ca ai gresit numele fisierului")
except IOError:
	print("Problema IO")
except ValueError:
	print("Problema de variabile")
except Exception:
	print("O eroare")	
else:	
	f.close()

print("Multumesc pt utilizare")

def testFunc (d = 0):
	try:
		a = d + 1
	except TypeError:
		print("Ai gresit tipul valorii introduse")
	else:
		return a

print(testFunc(1))

print(testFunc("str"))

print("Salut! Ai terminat!")