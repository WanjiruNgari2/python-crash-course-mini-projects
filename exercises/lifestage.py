def checkAge():
    while True:
        age = input("How old are you? (or type 'q' to quit): ")
        if age.lower() == 'q':
            print("Goodbye!")
            break

        try:
            age = int(age)
            if age < 2:
                print("You are a baby!")
            elif age < 4:
                print("You are a toddler")
            elif age < 13:
                print("You are a kid")
            elif age < 20:
                print("You are a teenager")
            elif age < 65:
                print("You are an adult")
            elif age >= 65:
                print("You are an elder!")
        except ValueError:
            print('age must be a number!')
            continue


checkAge()
