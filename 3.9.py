'''9.	Print the table for a given number: 
             5 * 1 = 5
             5 * 2 = 10………..
'''
num = int(input("enter a number to print its table: "))
for i in range(1,11):
    print(f"{num} * {i} = {num*i}")
    