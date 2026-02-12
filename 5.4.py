'''4.	Create a dictionary of n persons where key is name and value is city. 
a) Display all names
b) Display all city names
c) Display student name and city of all students.
d) Count number of students in each city.
'''
n = int(input("Enter the number of persons: "))
persons = {}
for i in range(n):
    name = input("Enter the name of person {}: ".format(i+1))
    city = input("Enter the city of person {}: ".format(i+1))
    persons[name] = city
print("Names of all persons:")
for name in persons.keys(): print(name)
print("City names of all persons:") 
for city in persons.values(): print(city) 
print("Name and city of all persons:") 
for name, city in persons.items(): print(f"{name} lives in {city}") 
city_count = {} 
for city in persons.values():
    if city in city_count: 
        city_count[city] += 1
    else: 
        city_count[city] = 1
print("Number of persons in each city:") 
for city, count in city_count.items(): print(f"{city}: {count} persons")
