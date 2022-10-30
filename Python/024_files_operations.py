# '''
# File operations.
# File modes:
#
# r - reading (defualt)
# w - writing
# a - appending
# b - binary format - like photos, pdf, exe etc.
# x - exclusive creation
#
# \n - new line
# \t - new tab
# \U - unicode
#
#
# '''

# my_file = open(r'routers.txt', 'r')
#
# print(my_file.mode)
# print(my_file.read()) #All file content
# print(my_file.read(2)) #Read
# print(my_file.seek(0)) #position
#

# my_file.seek(0)
# for line in my_file.readlines():
#     if line.startswith('A'):
#         print(line)
#
# my_file = (r'routers.txt', 'x')

#Writing\Overwrite and appending

# new_file = open('new_file.txt', 'w', encoding='utf-8')
# new_file.write('I like Python! Do you?')
# new_file.writelines(['Cisco', 'Jupiter', 'HP'])
# new_file.close()
# #Append
# new_file = open('new_file.txt', 'a', encoding='utf-8')
# new_file.write('This string was appended')
# new_file.close()
#
#
# new_file = open('new_file.txt', 'w+')
# new_file.seek(0)
# print(new_file.read())
# new_file.close()
#
# print(new_file.closed)#True

#With method - automatically close the files

# with open('new_file.txt','w') as f:
#     f.write('Hello Python!!!')
#
#Delete files

f = open('new_file.txt')
f.seek(0)
print(len(f.read()))
f.close()

f = open('new_file.txt', 'r+')
# f.truncate() # Delete all content from file
print(f.read(10))
f.truncate(10) # Delete and keep this string 'on!!!'
print(f.read())


