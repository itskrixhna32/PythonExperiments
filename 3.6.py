#6.	Write a program to print sum of digits.
num = int(input("enter a number: "))
sum = 0
while num>0:
    digit = num%10
    sum+=digit
    num = num//10
print("the sum of digits is:",sum)
