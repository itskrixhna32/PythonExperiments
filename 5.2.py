#2.	Create a tuple to store n numeric values and find average of all values.
n = int(input("Enter the number of values: "))
values = []
for i in range(n):
    value = float(input("Enter a numeric value: "))
    values.append(value)
values_tuple = tuple(values)
average = sum(values_tuple) / len(values_tuple)
print(f"The average of the values is: {average}")
