P = float(input("enter the principle amount: "))
R = float(input("enter the rate of interest: "))
T = float(input("enter the time: "))
SI = (P*R*T)/100
CI = P*((1+R/100)**T)
print("SIMPLE INTEREST = ",SI)
print("COMPOUND INTEREST = ",CI)