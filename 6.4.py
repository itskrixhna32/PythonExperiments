#4.	Write a recursive function to print Fibonacci series upto n terms.
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series
# Example usage:
terms = 10
fib_series = fibonacci(terms)
print(f"Fibonacci series up to {terms} terms: {fib_series}")
