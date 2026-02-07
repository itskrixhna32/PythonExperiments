'''4.	WAP to enter a string and a substring. You have to print the number of times that the substring occurs in the given string. 
String traversal will take place from left to right, not from right to left.'''

string = input("Enter a string: ")
substring = input("Enter a substring: ")
count = 0
for i in range(len(string)-len(substring)+1):
    if string[i:i+len(substring)] == substring:
        count += 1

print("The substring occurs", count, "times in the given string.")
