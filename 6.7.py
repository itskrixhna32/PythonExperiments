'''7.	Write functions to explain mentioned concepts:
a.	Keyword argument
b.	Default argument
c.	Variable length argument
'''
# a. Keyword argument
def greet(name, message):
    print(f"{message}, {name}!")
greet(name="Alice", message="Hello")
# b. Default argument
def greet(name, message="Hello"):
    print(f"{message}, {name}!")
greet("Bob")
# c. Variable length argument
def sum_numbers(*args):
    return sum(args)
print("Sum of numbers:", sum_numbers(1, 2, 3, 4, 5))
