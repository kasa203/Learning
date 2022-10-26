import os

print(os.sep) # \ - Windows, /- For unix
print(os.getcwd()) # Current working dir
os.chdir(r'C:\users')
print(os.getcwd())
print(os.listdir())
os.makedirs('Users/New_folder')
os.remove('pathname') #remove path
os.removedirs('pathname') #Remove recursivly
os.rmdir('path')
print(os.environ) #Varible values of OS
os.getuid # user id
os.getpid() # process id
os.getgid() #group id