#techsupport.py
def welcome():
print('Welcome to the automated technical support system.')
print('Please describe your problem.')
def get_input():
return input().lower()
def main():
welcome()
list = {
'crashed': 'Are the drivers up to date?',
'blue': 'Ah, the blue screen of death. And then what happened?',
'hacked':'You should consider installing anti-virus software.',
'Bluetooth': 'Have you tried mouthwash?',
'windows': 'Ah, I think I see your problem. What version?',
'apple': 'You do mean the computer kind?',
'spam': 'You should see if your mail client can filter messages.',
'connection': 'Contact Telkom.'
}
query = raw_input()
lists = query.split()
while (not query=='quit'):
t = 0
for problem, solution in list.iteritems():
for word in lists:
if problem == word:
t = 1
print solution
break
if t == 0:
print('Curious, tell me more.')
query = raw_input()
lists = query.split()

main()
