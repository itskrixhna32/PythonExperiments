#6.	Write a lambda function which gives tuple of max and min from a list.
max_min_tuple = lambda lst: (max(lst), min(lst))
# Example usage:
numbers = [3, 1, 4, 1, 5, 9]
result = max_min_tuple(numbers)
print(f"The maximum and minimum values in the list are: {result}")
