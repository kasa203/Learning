# import platform
#
# print(dir(platform))
# print(platform.machine())
# print(platform.release())
# print(platform.platform())
# print(platform.processor())
# print(platform.uname())

import getpass
#Getpass
#Getuser
db_pass = getpass.getpass()
print(f"The enter password is {db_pass}")
user = getpass.getuser()
print(f"Username {user}")