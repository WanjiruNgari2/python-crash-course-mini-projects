# will check if a name is already in use:

names = []

def giveName():
    while True:
        yourName = input("Tell us your name or type q to quit: ")

        if yourName.lower() == 'q':
            break


        if yourName.lower() not in names:
            print(f"added {yourName} to the list")
            names.append(yourName.lower())
        else:
                print(f"chooose another name, {yourName} is taken!")

giveName()



