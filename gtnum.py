import random
print('this is guess the number game.')
snum=random.randint(1, 100)
a=0
while a<=10:
    g = int(input('give me ur guess: '))
    a = a+1
    if g == snum:
        print('You got it!')
        break
    elif g<snum:
        print('higher')
    elif g>snum:
        print('lower')
if a > 10:
    ('You failed it was',snum)