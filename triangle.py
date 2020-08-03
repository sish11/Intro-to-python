import math
a = input ("enter the length of the first side:")
b = input ("enter the length of the second side:")
c = input ("enter the length of the third side:")

#print (math.sqrt(9))

#perfom computation:area
s = ( a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
#output the lengths and area
print("the area of triangle with sides of length", a,"and",b,"and",c, "is",str(area+",")
