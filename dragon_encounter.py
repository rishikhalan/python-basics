sword = input("(All questions are y/n) You’re walking through a forest and meet a dragon! Do you have a sword? ")
if sword == 'y':
    strength = float(input("What is ur strength level? "))
    if strength > 70:
        print('You defeat the dragon.')
    else:
        print("The dragon defeats you.")
else:
    flee = input("Do you try to flee? ")
    if flee == 'y':
        speed = float(input("What is ur speed? "))
        if speed > 60:
            print('u escape safely')
        else:
            print("The dragon catches you.")
    else:
       print("You get burned by fire. ")
     
