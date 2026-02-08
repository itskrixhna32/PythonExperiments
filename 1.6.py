#calculator using conditional statements
n1 = float(input("enter any number: "))
operator = input("enter the operation you want to find: ")
n2 = float(input("enter any number: "))
if(operator == '+'):
  ans = n1+n2
  print("ANS = ",ans)
elif(operator == '-'):
  ans = n1-n2
  print("ANS = ",ans)
elif(operator == '*'):
  ans = n1*n2
  print("ANS = ",ans)
elif(operator == '/'):
  ans = n1/n2
  print("ANS = ",ans)
else:
  print("INVALID OPERATOR!!")