import random 


answer = random.randint(1, 100)
chance = int(input('Choose level(10-easy 1-hell): '))

while chance > 0:

    guess = int(input('Guess the number(1~100): '))
    if guess-answer==0:
        print('Correct!')
        break
    elif guess < answer:
        hint = 'up!'
    elif guess > answer:
        hint = 'Down!'
    chance -= 1
    print('{} You have {} life(s)'.format(hint, chance))

    if chance == 0:
        print('YOu now dead! The answer was {}.'.format(answer))



