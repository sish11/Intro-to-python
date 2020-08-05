def is_vowel(c):
vowels = "aeiou"
vowels.find(c.lower())
if vowels.find(c.lower()) == -1:
return False
else:
return True
#Filtering function
def toPigLatin (sent):
new_word = ''
dammit = ''
for a in sent.split(" "):
if is_vowel(a[0]):
a = a+"way " dammit = dammit + a
else: for i in range(len(a)):
if not is_vowel(a[i]):
if i == (len(a)-1):
new_word = a[i+1:]+"a"+a[0:i+1]+"ay "
dammit = dammit + new_word
new_word = a[i+1:]+"a"+a[0:i+1]+"ay "
else:

dammit = dammit + new_word
break
return dammit

def toEnglish (sent):
sec = ''
for a in sent.split(" "):
if a[-3:] == "way":
sec = sec + a[0:-3]+ " "
else:
n = -3
new_word = ''
while True:
if a[n] == 'a':
new_word = new_word+ a[:n] + " "
break
else:
new_word = a[n] + new_word
n = n-1
sec = sec + new_word
return(sec)
main.py
# test program for english/piglatin translator
import piglatin
choice = input ("(E)nglish or (P)ig Latin?\n")
action = choice[:1]
if action == 'E':
s = input("Enter an English sentence:\n")
new_s = piglatin.toPigLatin(s)
print("Pig-Latin:")
print(new_s)
elif action =='P':
s = input("Enter a Pig Latin sentence:\n")
new_s = piglatin.toEnglish(s)
print("English:")
print(new_s)
