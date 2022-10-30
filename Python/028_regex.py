import re

mystr = 'You can learn any programming langueage, whenther it is Python2, Python3, Perl, Java,javascript or PHP.'
#match()

a = re.match("You", mystr)
print(a) # <re.Match object; span=(0, 3), match='You'>

a = re.match("abc", mystr)
print(a, type(a)) #None

# a.group()
# print(a)

a = re.match("you", mystr, re.I) #ignore upper\lower
print(a.group())

