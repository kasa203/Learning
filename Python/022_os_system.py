#Execute OS commands

import os
import platform
# #Run command
# os.system('ipconfig')
# my_output = os.system('powershell gci')
#
# #Getting the output
# # Status code - 0 Good, 1- Error
#
# cmd = 'ipconfig'
# code = os.system(cmd)
#
# if code == 0:
#     print('Your command success excecuted!')
# else:
#     print('You got an error!')
#
#

#Task - Write python script to clear terminal of any os

if platform.system() == 'windows':
    command = 'cls'
    os.system(command)
    if command == 0:
        print('Your command success executed!')
    else:
        print('Your command not executed!')
elif platform.system() == 'Linux':
    command = 'clear'
    os.system(command)
    if command == 0:
        print('Your command success executed!')
    else:
        print('Your command not executed!')