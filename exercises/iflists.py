users = []

def welcomeUser():
    while True:
        choice = input('Tell me your role or type q to quit: ').strip()
        if choice.lower() == 'q':
            print("Aw! come again someday.")
            break

        role = choice.lower()
        if role not in users:
            users.append(role)
            print(f"Hello {choice}, You wanna sign up?")
        else:
            print(f"Hello {choice}, How can I help you today?")

welcomeUser()



