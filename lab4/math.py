#1
pi=22/7
degree = 15
radian = degree*(pi/180)
print("Radian:", radian)


#2
h = 5
b1 = 5
b2 = 6
A = (b1 + b2) * h / 2
print("Area:", float(A))


#3
import math
def area(n, s):
    area = (1 / 4) * n * s**2 / math.tan(math.pi / n)
    return area
n = 4
s = float(25)
result = area(n, s)
print(f"The area of the polygon is: {result}")


#4

l = 5
h = 6
area = l * h
print(f"The area of the parellelogram is:", float(area))