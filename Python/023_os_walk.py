'''
Os.walk(path)
used to generate directory and file names in a directory tree by walking

'''

#find path -name *.txt

import os

path = r'C:\git_repos\Learning'
#print(os.path.exists(path))
#print(os.walk(path))
# print(list(os.walk(path)))

for r,d,f in list(os.walk(path,topdown=False)):
    print(r)

#Task

import os
req_file = input('Enter your file name to search')
for r,d,f in os.walk("/home/ec2-user"):
    for each_file in f:
        print(os.path.join(r,each_file))