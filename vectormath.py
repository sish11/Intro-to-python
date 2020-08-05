
import math
def addition(vectorA, vectorB):
return [i + j for i, j in zip(vectorA, vectorB)]
def dotProduct(vectorA, vectorB):

return sum([i* j for i, j in zip(vectorA, vectorB)])
def getNorm(vectorA):
norm = math.sqrt(sum(map(lambda x:x*x,vectorA)))
return format(norm, '.2f')
A = raw_input("Enter vector A:")
A = map(int, A.split())
B= raw_input("Enter vector B:")
B= map(int, B.split())
print("A+B ="+str(addition(A,B)))
print("A.B ="+str(dotProduct(A,B)))
print("|A| ="+str(getNorm(A)))
print("|A| ="+str(getNorm(B)))
#NewCode
import math
def addition(vectorA, vectorB):
return [i + j for i, j in zip(vectorA, vectorB)]
def dotProduct(vectorA, vectorB):
return [i* j for i, j in zip(vectorA, vectorB)]
def getNorm(vectorA):
norm = math.sqrt(sum(map(lambda x:x*x,vectorA)))
return format(norm, '.2f')
A = input("Enter vector A:")
#A1 = map(int, A.split(" "))
B= input("Enter vector B:")
#B1= map(int, B.split())
print("A+B ="+str(addition(map(int, A.split(" ")),map(int, B.split()))))
#print(list(B1))
print("A.B ="+str(dotProduct(map(int, A.split(" ")),map(int, B.split()))))
print("|A| ="+str(getNorm(map(int, A.split(" "))))
print("|A| ="+str(getNorm(map(int, B.split()))))
