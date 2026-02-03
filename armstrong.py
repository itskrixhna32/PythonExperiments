# any number is armstrong or not for any digit number
num = int(input("enter a number: "))
sum = 0
temp = num
n = len(str(num))
while temp>0:
    digit = temp%10
    sum += digit**n
    temp //=10

if num == sum:
    print(num,"is an armstrong number.")
else:
    print(num,"is not an armstrong number.")
    