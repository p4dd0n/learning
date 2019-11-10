import random

#def players():
#	#player = input("Enter number of players: ")
#		if player == 1
#			return



def rollDice():
	diceList = []
	for number in range(5):
		diceValue = random.randint(1, 6)
		diceList.append(diceValue)
		print("Dice", number + 1, ":", diceValue)

	return diceList

def keepDice():
	player = input("Please select which dices to save, by writing the dice number (1 2 3 etc), press enter when done selecting dices: ")
	for dice in player:
		if dice == " ":
			pass
		else:
			print(dice)
		

def yatzeeTable():
	print("|Players|", player)

if __name__ == "__main__":
	diceList = rollDice()
	keepDice()
	
