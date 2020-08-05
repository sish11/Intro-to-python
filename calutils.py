import os
import re
#functions used in python
class calutils():

def __init__(self):
print ("your in init");
def findleapYear(self,year):
print
if (year % 4) == 0:
if (year % 100) == 0:
if (year % 400) == 0:
print("{0} is a leap year".format(year))
else:
print("{0} is not a leap year".format(year))
else:
print("{0} is a leap year".format(year))
else:
print("{0} is not a leap year".format(year))
def userSelected(self,userChoice):
if (userChoice == 1):
year = int(input("enter a year"))
#selected year sent to function
c.findleapYear(year)
elif(userChoice == 2):
print ("Month number 1 is January.\n");
print ("Month number 2 is February.\n"); print ("Month number 3 is March.\n");
print ("Month number 4 is April.\n");
print ("Month number 5 is May.\n");
print ("Month number 6 is June.\n");
print ("Month number 7 is July.\n");
print ("Month number 8 is August.\n");

print ("Month number 9 is September.\n");
print ("Month number 10 is October.\n");
print ("Month number 11 is November.\n");
print ("Month number 12 is Decemeber.\n");
c = calutils();
userChoice = int(input("Choose from the following option\n"));
print("0. quit\n");
print("1. Test is_leap_year().\n");
print("2. Test month_name().\n");
print("3. Test days_in_month().\n");
print("4. Test first_day_of_year().\n");
print("5. Test first_day_of_month().\n");
