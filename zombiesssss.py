safehouse = input("There is a zombie apocalypse, are you in the safe house(y/n)? ")


if safehouse == 'y':
    food = input("Do you have food(y/n)? ")
    if food == 'y':
        weapons = input("Do you have weapons(y/n)? ")
        if weapons == 'y':
            print("You survive the night safely.")
        else:
            print("You are safe but vulnerable.")
    else:
        print("You starve.")
else:
    car = input('Do you have a car(y/n)? ')
    if car == 'y':
        fuel = float(input("What is your fuel percentage? "))
        if fuel >= 50:
            print("You escape the city.")
        else:
            print("Zombies get you!")
    else:
        print("Zombies get you!")
        