'''5.	Given a string containing both upper and lower case alphabets. Write a Python program to count the number of occurrences of each alphabet (case insensitive) and display the same.
Sample Input
ABaBCbGc
Sample Output
2A
3B
2C
1G '''
s = input("Enter a string: ")

s = s.upper()   # make it case-insensitive

for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    count = 0
    for c in s:
        if c == ch:
            count += 1
    if count > 0:
        print(str(count) + ch)
