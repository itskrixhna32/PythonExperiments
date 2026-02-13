'''5.	Store details of n movies in a dictionary by taking input from the user. Each movie must store details like name,  year, director name, production cost, collection made (earning) & perform the following :-
a)	print all movie details
b)	display name of movies released before 2015
c)	print movies that made a profit.
d)	print movies directed by a particular director.
'''
n = int(input("Enter the number of movies: "))
movies = {}
for i in range(n):
    name = input("Enter the name of movie {}: ".format(i+1))
    year = int(input("Enter the release year of movie {}: ".format(i+1)))
    director = input("Enter the director name of movie {}: ".format(i+1))
    cost = float(input("Enter the production cost of movie {}: ".format(i+1)))
    earning = float(input("Enter the collection made (earning) of movie {}: ".format(i+1)))
    movies[name] = {"year": year, "director": director, "cost": cost, "earning": earning}
print("Details of all movies:")
for name, details in movies.items():
    print(f"Movie: {name}, Year: {details['year']}, Director: {details['director']}, Cost: {details['cost']}, Earning: {details['earning']}")
print("Movies released before 2015:")
for name, details in movies.items():
    if details['year'] < 2015:
        print(name)
print("Movies that made a profit:")
for name, details in movies.items():
    if details['earning'] > details['cost']:
        print(name)
director_name = input("Enter the director name to filter movies: ")
print(f"Movies directed by {director_name}:")
for name, details in movies.items():
    if details['director'] == director_name:
        print(name)
        