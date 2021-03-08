import math
import cmath
print('Calculator example.')
q = math.pi
print(q)
a = eval(input('Enter a(greater than 0): '))
b = eval(input('Enter b: '))
c = eval(input('Enter c: '))

d = (b**2) - 4*a*c

if d > 0:
    root1 = (-b + d)/(2*a)
    root2 = (-b - d)/(2*a)
elif d ==0:
    root1 = root2 = (-b)/(2*a)
else:
    root1 = (-b -cmath.sqrt(d))/(2*a)
    root2 = (-b + cmath.sqrt(d))/(2*a)

print('First root is', root1, 'and second root is', root2)
