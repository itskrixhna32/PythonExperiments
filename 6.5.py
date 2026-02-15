#5.	Write a lambda function to find volume of cone.
# The formula for the volume of a cone is V = (1/3) * π * r^2 * h
import math
volume_of_cone = lambda r, h: (1/3) * math.pi * r**2 * h
# Example usage:
radius = 5
height = 10
volume = volume_of_cone(radius, height)
print(f"The volume of the cone with radius {radius} and height {height} is: {volume:.2f}")
