from math import radians, sin, cos, tan

angle=float(input(' Enter a angle in degrees: '))
sine=sin(radians(angle))
cosine=cos(radians(angle))
tangent=tan(radians(angle))

print('The sine value of the angle {} is: {:.2f}'.format(angle, sin))
