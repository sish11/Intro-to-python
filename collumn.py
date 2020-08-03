#column.py 
num = eval(input("Enter a number: "))
 n = num 
 while(n<=num+47):
      print(n)
       n += 7


def days(month):
     if month in ["January", "March", "May", "July", "August", "October", "December"]:
          return 31 
          elif month is "February": 
          return 29
           else: 
           return 30 
           
    def main(): 
    month = input('Enter month: ')
     day = input('Enter start day: ')
      d = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
       ind = 0 for i, string in enumerate(d): 
       print('%2s' % string, end=' ')
        if day.startswith(string):
             ind = i
     print() 
             
           
for i in range(1, days(month)+1+ind): 
if i < ind+1: 
print(' ', end=' ')
 else:
      print('%2d' % (i-ind), end=' ') 
      if i % 7 == 0:
           print()
main()

