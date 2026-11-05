import random
print('This is the rock paper scissors game.')
ua =input('Choose rock paper or scissors: ').lower()
cc = random.choice(['rock', 'paper', 'scissors'])
if cc == ua:
    print('Its a tie!')
elif (cc == 'paper' and ua == 'scissors') or (ua == 'rock' and cc == 'scissors') or (ua == 'paper' and cc == 'rock') :
    print('You win!')
else:
    print('Computer wins!')