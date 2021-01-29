import random


answer = random.randint(1,101)
chance = 3

while chance > 0:

    guess =  int(input('Guess the number(1~100): '))
    if guess-answer==0:
        print('Correct!')
        break
    elif guess<answer:
        hint = 'up!'
    elif guess>answer:
        hint = 'Down!'
    chance -=1
print('{} You have {} life(s)'.format(hint, chance))

