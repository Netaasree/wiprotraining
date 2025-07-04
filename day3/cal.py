#from calendar import *
'''
year=int(input("Enter a year number: "))
Month=int(input("Enter a month number: "))
str=month(year,Month)
print(str)
'''

#program to print the next 10 day dates continuously
from datetime import *
d=date.today()
print(d)
d=date(2005,2,4)
for x in range(1,10):
    nextdate=d+timedelta(days=x)
    print(nextdate)
    
    

