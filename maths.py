def printSomething(name):
	print ("Hei", name)

def addNumbers(number1, number2):
	print ("Gratulerer, tallet ditt er ")
	result = number1 + number2
	print (result)

def subtractNumbers(number1, number2, number3):
	print ("Ditt lille tall er ")
	result = number1 - number2 - number3
	print (result)

def averageNumbers(number1, number2, number3, number4, number5):
	print ("Ditt gjennomsnittlige tall er ")
	result = (number1 + number2 + number3 + number4 + number5) / 5
	print (result)

def multiplyNumbers(number1, number2):
	#print ("Ditt multiplikasjonstall er ")
	result = number1 * number2
	return result

def test(streng):

	occuredChars = []
	for char in streng:
		if char in occuredChars:
			return char
		else:
			occuredChars.append(char)

	
	print(a)

def main():
	#addNumbers(2, 4)
	#subtractNumbers(99, 9, 1)
	#averageNumbers(3, 5, 6, 8, 99)
	#result = multiplyNumbers(5, 4)
	#addNumbers(result, 2)
	#subtractNumbers(result, 3, 3)
	res = test("DBCABA")
	print(res)

	resultat = test("ABCDDBCA")
	print(resultat)


main()