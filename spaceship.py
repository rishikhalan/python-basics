shield = input("You are the captain of a spaceship, and an alien ship approaches. Is your shield up? (All q's are y/n) ")
if shield == 'y':
    laser = input('Is your laser charged? ')
    if laser == 'y':
        print("You attack first and win.")
    else:
        print("Alien attacks and damages you")
        flee = input('Do you try to flee? ')
        if flee == 'y':
            speed = int(input("What is your speed? "))
            if speed > 80:
                print('You escape!')
            else:
                print('You’re caught.')
        else:
            print("'Instantly defeated you are', says Yoda, whilst coming out of the ship. ")
else:
    flee = input('Do you try to flee? ')
    if flee == 'y':
        speed = int(input("What is your speed? "))
        if speed > 80:
            print('You escape!')
        else:
            print('You’re caught.')
    else:
        print("'Instantly defeated you are', says Yoda, whilst coming out of the ship. ")