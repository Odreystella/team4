import random


answer = random.randint(1,100)
guess = int(input('Guess the number(1-100): '))
if guess-answer == 0:
	print('That is correct! The answer was {}'.format(answer))

else:	
	print('Wrong Answer, stupid, The answer was {}.'.format(answer))


