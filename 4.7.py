'''7.	Create 2 sets s1 and s2 of n fruits each by taking input from user and find:
a)	Fruits which are in both sets s1 and s2
b)	Fruits only in s1 but not in s2
c)	Count of all fruits from s1 and s2 '''

n = int(input("Enter number of fruits: "))

s1 = set()
s2 = set()

print("Enter fruits for set s1:")
for i in range(n):
    s1.add(input())

print("Enter fruits for set s2:")
for i in range(n):
    s2.add(input())

print("Fruits in both s1 and s2:", s1 & s2)

print("Fruits only in s1:", s1 - s2)

print("Total count of fruits:", len(s1 | s2))
