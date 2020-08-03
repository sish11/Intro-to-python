#Take input from the user
N=(int)(input('Enter the start point N:\n'))
M=(int)(input('Enter the end point M:\n'))
print('The palindromic primes are:')

#loop through N to M
for i in range(N,M):
j=(str)(i)

#check whether it is a palindrome
if j==j[::-1]:
flag=0
#if it is palindrome check whether it is prime
for k in range(2,i-1):
if i%k == 0:
flag=1
break
if flag==0:
print(i)
