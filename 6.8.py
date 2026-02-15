#8.	Write a program to check whether all the values in a dictionary are same or not using lambda function.
my_dict = {'a': 1, 'b': 1, 'c': 1}
all_values_same = lambda d: len(set(d.values())) == 1
if all_values_same(my_dict):
    print("All values in the dictionary are the same.")
else:
    print("Not all values in the dictionary are the same.")
    