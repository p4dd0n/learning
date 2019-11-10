import random

def userChoice():
    user = input("Please choose rock, paper or scissor. Enter exit to quit: ")
    while (user != "rock" and user != "paper" and user != "scissor" and user != "exit"):
        user = input("Invalid input. Please choose rock, paper or scissor. Enter exit to quit: ")
    return user

def computerChoice():
    computer = random.randint(1, 3)
    if computer == 1:
        return "rock"
    elif computer == 2:
        return "paper"
    elif computer == 3:
        return "scissor"

def findWinner(user, computer):
    print("User:    ", user)
    print("Computer:    ", computer)
    if user == computer:
        print("Draw")

    if user == "rock":
        if computer == "paper":
            print("Computer wins")
        else:
            print("Player wins")

    if user == "paper":
        if computer == "scissor":
            print("Computer wins")
        else:
            print("Player wins")

    if user == "scissor":
        if computer == "rock":
            print("Computer wins")
        else:
            print("Player wins")

if __name__ == "__main__":
    user = userChoice()
    while user != "exit":
        computer = computerChoice()
        findWinner(user, computer)
        user = userChoice()