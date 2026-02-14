#1.	Write a Python function to find the maximum and minimum numbers from a sequence of numbers.  (Note: Do not use built-in functions.)
def find_max_min(numbers):
    if not numbers:
        return None, None
    max_num = numbers[0]
    min_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return max_num, min_num

# Example usage:
numbers = [3, 5, 2, 8, 1, 9, 4]
max_val, min_val = find_max_min(numbers)
print("Maximum number:", max_val)
print("Minimum number:", min_val)