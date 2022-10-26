import os.path

print(os.path.sep) # /
my_path = r'C:\users\Asaf'
print(os.path.basename(my_path))
print(os.path.dirname(my_path))

path1 = 'C:\\'
path2 = 'users'
print(os.path.join(path1,path2))
print(os.path.split(my_path))
print(os.path.getsize(my_path))
print(os.path.exists(my_path)) #True0
print(os.path.isdir(my_path)) #True
print(os.path.isfile(my_path)) #false
print(os.path.islink(my_path)) #False