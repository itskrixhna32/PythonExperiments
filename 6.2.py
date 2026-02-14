#2.	write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number
def sum_of_cubes(n):
    if n <= 0:
        return 0
    total = 0
    for i in range(1, n):
        total += i ** 3
    return total
# Example usage:
number = 5
result = sum_of_cubes(number)
print(f"The sum of cubes of positive integers smaller than {number} is: {result}")