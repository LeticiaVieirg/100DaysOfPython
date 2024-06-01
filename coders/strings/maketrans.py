#This function create a table of translate

import string
a=string.ascii_letters
#Rotating the alphabetic a character to the left
b=a[1:]+a[0]

tab=string.maketrans(a,b)
msg=('This text is translating...')

print(string.translate(msg, tab))
