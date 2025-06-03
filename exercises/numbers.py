# count numbers to 20, add them, show even and odd numbers
numbers = []

def countNumbers():
    for n in range(0, 20):
        numbers.append(n)
        print(numbers)

countNumbers()

def evenNumbers():
    for n in range(0, 20, 2):
        print(n)

evenNumbers()

def oddNumbers():
    for n in range(0, 20, 3):
        print(n)

oddNumbers()


def addNumbers():
    total = 0
    for n in range(0, 20):
        total += n
    print(total)

addNumbers()

def cubedNumbers():
    for n in range(20):
        print(n ** 3)

cubedNumbers()
