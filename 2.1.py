# 1.	Check whether the given number is divisible by 3 and 5 both.
num = int(input("enter the number: "))
if num%3==0 and num%5==0:
    print("The number is divisible by both 3 and 5.")
else:
    print("the number is not divisible by both 3 and 5.")