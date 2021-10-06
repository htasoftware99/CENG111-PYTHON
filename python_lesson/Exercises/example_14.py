Salary = int(input("What is your salary?: "))
Child = int(input("How many children do you have?: "))

if Child == 1:
    Salary = (Salary * 0.05) + Salary
    print("New salary is" , Salary)

elif Child == 2:
    Salary = (Salary * 0.10) + Salary
    print("New salary is" , Salary)

elif Child >=3:
    Salary = (Salary * 0.20) + Salary
    print("New salary is" , Salary)