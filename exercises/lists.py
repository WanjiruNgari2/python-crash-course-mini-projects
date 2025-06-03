destinations = ['Italy', 'Ethiopia', 'Turkey', 'Greece', 'Mauritius', 'Kenya']
myFoods = ['pizza', 'chicken', 'pie', 'rice', 'roti', 'spaghetti']
yourFoods = myFoods[:] #adding the semicolon ensure The variables arent replacing each other

print(f"original: {destinations} ")

destinations.sort()
print(f"Sorted destinations: {destinations}")

destinations.sort(reverse=True)
print(f"reverse sort destinations: {destinations}")

destinations.reverse()
print(f"reversed destinations: {destinations}")

print(f"my fav foods are: {myFoods}")
print(f"your fav foods are: {yourFoods}")
myFoods.append('ugali')
print(f"my new favs are: {myFoods}")
yourFoods.append('fish')
print(f"my new favs are: {yourFoods}")

print(f"all include: {destinations}")
print(f"The first two include: {destinations[0:2]}")
print(f"The last two include: {destinations[-2:]}")
print(f"The middle to last include: {destinations[3:]}")


def chooseDest():
    for destination in destinations:
        choice = input('Where would you love to visit today?: ').title()
        print(f"You chose {choice} and not {destination[:]}") # the : ensures to loop thru the list and stop afterwards

chooseDest()


