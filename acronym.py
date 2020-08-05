ignoreStrings = raw_input('Enter words to be ignored separated by commas:')
ignoreList = ignoreStrings.split(',')
title = raw_input('Enter a title to generate its acronym: ')
titleList = title.split()
from __builtin__ import any as b_any
for x in titleList:
if (b_any(x.lower() in y.lower() for y in ignoreList)):
print '',
else:
print x[0].upper()
