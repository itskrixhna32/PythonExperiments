#1.	Scan n values in range 0-3 and print the number of times each value has occurred.

n = int(input("enter the number of values: "))
count = [0,0,0,0]
for i in range(n):
    value = int(input("enter a value between 0 and 3: "))
    if 0 <= value <= 3:
        count[value] += 1
    else:
        print("Invalid input. Please enter a value between 0 and 3.")
print("Count of each value:")
for i in range(4):
    print(f"Value {i}: {count[i]} times")
    