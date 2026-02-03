#7.	Write a program which takes any date as input and display next date of the calendar
#e.g.
#I/P: day=20 month=9 year=2005 
#O/P: day=21 month=9 year 2005
day = int(input("enter the day: "))
month = int(input("enter the month: "))
year = int(input("enter the year: "))
#check for months having 31 days
if month in (1,3,5,7,8,10):
    if day<31:
        day+=1
    else:
        day = 1
        month+=1
#check for months having 30 days
elif month in (4,6,9,11):
    if day<30:
        day+=1
    else:
        day = 1
        month += 1
#check for february month
elif month == 2:
    if (year%4==0 and year%100!=0)or(year%400==0):
        if day<29:
            day+=1
        else:
            day = 1
            month+=1
    else:
        if day<28:
            day+=1
        else:
            day = 1
            month+=1
#check for december month
elif month == 12:
    if day<31:
        day+=1
    else:
        day = 1
        month = 1
        year+=1
print("the next date is: ",day,"/",month,"/",year)


