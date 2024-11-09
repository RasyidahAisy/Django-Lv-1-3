import re
pattern = r'\W+'
text = 'this is string! yes, this is string and 123 is number'
x = re.findall(pattern, text)
print(x)
