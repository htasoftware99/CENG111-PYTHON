from math import sqrt

a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
c = int(input("Enter c number: "))

delta = (b ** 2) - 4 * a * c
print("Delta: ", delta)

if delta > 0:
    root_1 = (-b -sqrt(delta)) / (2 * a)
    root_2 = (-b +sqrt(delta)) / (2 * a)
    print("There are real two roots")
elif delta == 0:
    DoubleRoot = (-b / 2*a)
    print("There are double roots")
else:
    print("There is no any real root")