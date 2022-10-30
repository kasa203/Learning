# import os
#
# status_code = os.system('ipconfig')
# print(status_code)

#subprocess - running your commands, store your output in vars

import subprocess


#sp = subprocess.Popen(cmd,Shell=True/False,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

'''
if Shell true
cmd = 'ls -ltr'
Shell=True

If Shell false
cmd=['ls','-ltr']
Shell=False
'''

cmd='ipconfig'
sp = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc = sp.wait() #return code, will auto wait for your command - 0 - success, else - failed
out,err=sp.communicate()
print(f'OUTPUT is \n{out.splitlines()}') #Convert it into a list, line by line
print(f'ERRORS is \n{err.splitlines()}') #Convert it into a list, line by line
print(type(out),type(err))