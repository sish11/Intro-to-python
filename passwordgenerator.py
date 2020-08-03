def passwordGenerator ():
    #write your code here#
   lowerchars = ['a','b','c','d','e']
   upperchars =['A','B','C','D','E']
   specialchars = [ '%','*','@','$','?']
   numerichars=['1','2','3','4','5','6','7','8','9','0']
password=random.choice(lowerchars) + random.choice(upperchars)+random.choice(specialchars)+random.choice(numerichars)
 
 password = password + password 
 return password
