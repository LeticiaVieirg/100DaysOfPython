import math
import random 

lower=int(input('enter a lower bound: '))
upper=int(input('enter a upper bound: '))

x=random.randint(lower, upper)
print('\nYou have only ', round(math.log(upper - lower + 1,2)),
'chances to guess the integer! \n')

count=0
while count<math.log(upper-lower+1,2):
	count+=1

	guess=int(input('Guess a number:'))

	if x==guess:
		print('Congratulation! You did it in ', count, ' try')
		break
	elif x>guess:
		print('You guessed to small!')
	elif x<guess:
		print('You guessed too high!')

if count>=math.log(upper-lower+1,2):
	print('\nThe number is %d' %x)
