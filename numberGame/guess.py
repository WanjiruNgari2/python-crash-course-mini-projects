import random

def guessNumber():
    """ Create a number guessing game
    """

    while True:
        answer = input("Give us any number of your choice not exceeding 20 or press q to quit game: ")
        if answer.lower() == "q":
            print('later Gator!')
            break

        try:
            userAnswer = int(answer)
        except ValueError: # incase user types a str or such
            print("answer must be a number")
            continue

        compchoice = random.choice(range(10))
        if compchoice != userAnswer:
            print(f'Computer Guessed {compchoice} and failed!')
        else:
            print(f"Computer Guessed {compchoice} and passes!")
guessNumber()