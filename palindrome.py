# palindrome number or not
num = int(input("enter a number: "))
temp = num
rev = 0
while temp>0:
    digit = temp%10
    rev = rev*10 + digit
    temp //=10

if num == rev:
    print(num,"is a palindrome nuumber.")
else:
    print(num,"is not a palindrome number.")
    