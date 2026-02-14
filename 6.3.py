#3.	Write a Python function to print 1 to n using recursion. (Note: Do not use loops.)
def print_numbers(n):
    if n <= 0:
        return
    print_numbers(n - 1)
    print(n)
# Example usage:
number = 5
print(f"Numbers from 1 to {number}:")
print_numbers(number)
