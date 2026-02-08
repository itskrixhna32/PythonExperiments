#convert height in cm to feet and inches
h = int(input("enter height in cm: "))
feet = h//30.4
inches = (h%30.4)/2.54
print("Height in feet: ",feet)
print("Height in inches: ",inches)