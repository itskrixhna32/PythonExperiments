#7.	Count and print all numbers divisible by 5 or 7 between 1 to 100
n = int(input("enter the value of n: "))
count = 0
for i in range(1,n+1):
    if i%5==0 or i%7==0:
        print(i,end=' ')
        count+=1
print("\nTotal numbers divisible by 5 or 7 between 1 to 100 are:",count)
