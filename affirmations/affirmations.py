import random

AFFIRMATIONS = [
    "You are enough.",
    "You are capable of achieving great things.",   
    "You are worthy of love and respect.",
    "You have the power to create positive change in your life.",
    "Even if you are not ready for the day, it cannot always be night.",
    "you cannot spell 'awesome' without 'me'.",
    "Remember to stay hydrated and take care of yourself.", 
    "I know who I am and I am enough.",
]

def get_random_affirmation():
    """Returns a random affirmation from the list.""" # three double quotes for docstring to explain the function
    if not AFFIRMATIONS:
        return "No affirmations available."
    return (random.choice(AFFIRMATIONS))



def userAddedAffirmation():
    name = input("what is your name?: ")
    affirmation = input("what's the affirmation of today?: ")
    print(f"Hello {name}, {affirmation}")
    return affirmation


def add_affirmation(affirmation):
    """add affirmations from the user to the random affirmations list"""
    AFFIRMATIONS.append(affirmation)
    print(f"added affirmation: {affirmation}") 



# create a loop of affirmations until user types stop
def stopAffirmation():
    while True:
        reply = input("Type STOP at the end to exit or anything else to continue: ").strip()
        if "stop" in reply.lower():
            print("BYE FOR NOW!")
            break
        print(get_random_affirmation())

userQuotes = userAddedAffirmation()
add_affirmation(userQuotes)
stopAffirmation()


    