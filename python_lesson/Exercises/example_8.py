x = int(input("Enter a number: "))

factorial  = 1

if x < 0:
   print("Do not enter a negative number")
elif x == 0:
   print("0! = 1")
else:
   for i in range(1,x + 1):
       factorial = factorial*i
   print(str(x) + ' sayısının faktöriyeli = ' + str(factorial))