#Generere liste på 10 element, ved å bruke random-funksjon
#Sortere listen fra lavest til høyest, skrive ut listen et element om gangen, lavest til høyest
	#En funksjon som heter Generate list
	#En funksjon som er sort list
	#En funksjon som heter print list

import random

def generateList(length, biggestNumber):
	myList = []
	for number in range(length):
		randomNumber = random.randint(0, biggestNumber)
		myList.append(randomNumber)
	return myList

def printList(myList):
	for number in myList:
		print(number)

#def addNumbers(myList):
	#for number in myList:
		#addNumbers = sum(myList)
	#return addNumbers

def addNumbers(myList):
	listSum = 0
	for number in myList:
		listSum += number
	return listSum

def averageList(myList):
	averageSum = addNumbers(myList) / len(myList)
	return averageSum

def main():
	myList = generateList(10, 50)
	listSum = addNumbers(myList)
	averageSum = averageList(myList)
	print(myList)
	print(listSum)
	print(averageSum)

main()