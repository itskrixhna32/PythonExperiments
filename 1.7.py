#reverse a number
n = int(input("enter any number: "))
rev = 0
while n>=1:
  last_digit = n%10
  rev = rev*10 + last_digit
  n =n//10
print("reverse of a number: ",rev)