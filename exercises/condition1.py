alienColors = ['yellow', 'green', 'red']

def checkColor():
    while True: 

        color = input("Guess the alien's color or type q to quit:"
        "")
        if color.lower() == 'q':
            print('Bye For Now Player!')
            break
        if color not in alienColors:
                print('color unknown!')
        elif  color.lower() == 'green':
                print("you earned five points!")
        elif color.lower() == 'yellow':
                print('you earned ten points!')
        elif color.lower() == 'red':
                print('you earned fifteen points!')
                break
        else:
                print('Wrong answer!')




checkColor()

