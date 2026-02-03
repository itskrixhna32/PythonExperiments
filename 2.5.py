#5.	Check whether the quadratic equation has real roots or imaginary roots. Display the roots
import math
a = int(input("enter the value of a: "))
b = int(input("enter the value of b: "))
c = int(input("enter the value of c: " ))
d = b**2 - 4*a*c
if d>0:
    root1 = (-b + math.sqrt(d))/(2*a)
    root2 = (-b - math.sqrt(d))/(2*a)
    print("the roots are real and different.")
    print("the roots are: ",root1,"and",root2)
elif d==0:
    root = -b/(2*a)
    print("the roots are real and same.")
    print("the root is : ",root)
else:
    realpart = -b/(2*a)
    imagpart = math.sqrt(-d)/(2*a)
    print("the roots are imaginary. ")
    print("the roots are: ",realpart,"+",imagpart,"i and ",realpart,"-",imagpart,"i")
    