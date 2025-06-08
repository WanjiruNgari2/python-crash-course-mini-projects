def simpleCalculator():
    while True:
        choice = input("what's your operator of choice? (+/*) or type q to quit game: ")
        
        if choice.lower() == 'q':
            print("Goodbye!")
            break
        
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '+':
            total = num1+ num2
            print("result: ", total)
        elif choice == '*':
            product = num1 * num2
            print("Result:", product)
        elif choice == '/':
            try:
                division = num1 / num2
                print("Result:", division)
            except ZeroDivisionError: # expects this error if user inputs 0
                print('cannot divide by 0, try another number')

        else:
            print("invalid operator")

simpleCalculator()   