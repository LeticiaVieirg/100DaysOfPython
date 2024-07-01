from math import hypot

oppCat=float(input('Enter a value of the opposite cathetus: '))
adjCat=float(input('Enter a value of the ajacent cathetus: '))

hypotenuse=hypot(oppCat, adjCat)

print('The value of hypotenuse is {:.2f}'.format(hypotenuse))
