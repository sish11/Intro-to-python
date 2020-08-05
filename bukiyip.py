import math
def decimal_to_bukiyip(a):
bstr = ""
temp = awhile(temp > 0):
bstr = str(temp % 3)+bstr;
temp = int(temp/3);
return bstr;
def bukiyip_to_decimal (a):
bstr = 0
temp = a
i = 0;
while(temp > 0):
bstr = bstr + int(math.pow(3,i)) * (temp % 10);
temp = int(temp/10);

i = i+1
return bstr
def bukiyip_add (a, b):
num1 = bukiyip_to_decimal(a)
num2 = bukiyip_to_decimal(b)
return (decimal_to_bukiyip(num1+num2))
def bukiyip_multiply(a, b):
num1 = bukiyip_to_decimal(a)
num2 = bukiyip_to_decimal(b)
return (decimal_to_bukiyip(num1 * num2))
print("Available commands:\n");
print("d <number> : convert given decimal number to base-3.\n");
print("b <number> : convert given base-3 number to decimal.\n");
print("a <number> <number> : add the given base-3 numbers.\n");
print("m <number> <number> : multiply the given base-3 numbers.\n");
print("q : quit\n");
while(1):
option = input("Enter a command:")
if(option == "q"):
break;
#parse other commands
tokens = option.split(' ')
if(tokens[0] == 'd'):
print (bukiyip_add(int(tokens[1]),int(tokens[2])))
if(tokens[0] == 'm'):
print (bukiyip_multiply(int(tokens[1]),int(tokens[2])))
