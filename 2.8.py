'''8.	Print the grade sheet of a student for the given range of cgpa. Scan marks of five subjects and calculate the percentage.
CGPA=percentage/10
CGPA range:
0 to 3.4 -> F
3.5 to 5.0->C+
5.1 to 6->B
6.1 to 7-> B+
7.1 to 8-> A
8.1 to 9->A+
9.1 to 10-> O (Outstanding)
Sample Gradesheet
Name: Rohit Sharma
Roll Number: R17234512			SAPID: 50005673
Sem: 1						Course: B.Tech. CSE AI&ML

Subject name: Marks
PDS: 		70
Python: 	80
Chemistry: 	90
English: 	60
Physics: 	50
Percentage: 70%
CGPA:7.0
Grade:  
'''
name = input("enter the name of student:")
roll_number = input("enter the roll number:")
sapid = input("enter the SAP-ID:")
sem = input("enter the sem:")
course = input("enter the course:")
print("Name:",name)
print("Roll Number:",roll_number,"\t\tSAPID:",sapid)
print("Sem:",sem,"\t\t\t\tCourse:",course)
print("\nSubject name:\tMarks")

sub1 = int(input("enter the marks of PDS:"))
sub2 = int(input("enter the marks of Python:"))
sub3 = int(input("enter the marks of Chemistry:"))
sub4 = int(input("enter the marks of English:"))
sub5 = int(input("enter the marks of Physics:"))
total = sub1+sub2+sub3+sub4+sub5
percentage = (total/500)*100
cgpa = percentage/10
print("percentage is: ",percentage)
print("cgpa is: ",cgpa)
if cgpa>=0 and cgpa<=3.4:
    print("grade is: F")
elif cgpa>=3.5 and cgpa<=5.0:
    print("grade is: C+")
elif cgpa>=5.1 and cgpa<=6.0:
    print("grade is: B")
elif cgpa>=6.1 and cgpa<=7.0:
    print("grade is: B+")
elif cgpa>=7.1 and cgpa<=8.0:
    print("grade is: A")
elif cgpa>=8.1 and cgpa<=9.0:
    print("grade is: A+")
elif cgpa>=9.1 and cgpa<=10.0:
    print("grade is: O (Outstanding)")
else:
    print("invalid cgpa!!")


