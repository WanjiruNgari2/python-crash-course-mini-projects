import random

choices = ['Rock', 'Paper', 'Scissors']

def theGame():
    while True:
        userChoice = input("please type your choice: ").capitalize()
    
        if userChoice == "Quit":
            print("Thanks for playing!")
            break

    
        compChoice = random.choice(choices)


        if userChoice not in choices:
            print("Invalid choice! Please choose Rock, Paper, or Scissors.")
            continue 
    

        print(f"\nYou chose: {userChoice}")
        print(f"Computer chose: {compChoice}\n")


        if userChoice == compChoice:
            print("It's a tie!")
        elif (userChoice == 'Rock' and compChoice == 'Paper'):
            print("Rock crushes paper, You Win!!")
        elif (userChoice == 'Paper' and compChoice == 'Rock'):
            print("Rock crushes paper, You Lose!!")
        elif (userChoice == 'Scissors' and compChoice == 'Paper'):
            print("Scissors cut paper, You Win!!")
        elif (userChoice == 'Paper' and compChoice == 'Scissors'):
            print("Scissors cut paper, You Lose!!")
        elif (userChoice == 'Rock' and compChoice == 'Scissors'):
            print("Rock crushes Scissors, You win!!")
        elif (userChoice == 'Scissors' and compChoice == 'Rock'):
            print("Rock crushes Scissors, You Lose!!")

theGame()