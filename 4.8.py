'''8.	Take two sets and apply various set operations on them :
S1 = {Red ,yellow, orange , blue }
S2 = {violet, blue , purple} '''

S1 = {"Red", "yellow", "orange", "blue"}
S2 = {"violet", "blue", "purple"}

print("Union of S1 and S2:", S1 | S2)
print("Intersection of S1 and S2:", S1 & S2)
print("Difference of S1 and S2 (S1 - S2):", S1 - S2)
print("Difference of S2 and S1 (S2 - S1):", S2 - S1)
print("Symmetric Difference of S1 and S2:", S1 ^ S2)
