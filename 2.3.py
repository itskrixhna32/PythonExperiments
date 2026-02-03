#3.	Find the greatest among the two numbers. If numbers are equal than print “numbers are equal”
num1 = int(input("enter the first number: "))
num2 = int(input("enter tthe second number: "))
if num1>num2:
    print("the greatest number is:",num1)
elif num2>num1:
    print("the greatest number is:",num2)
else:
    print("the numbers are equal")