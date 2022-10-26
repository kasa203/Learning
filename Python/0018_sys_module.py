import sys

print(dir(sys))
print(help(sys))

print(sys.platform) # win32
print(sys.version) # 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)]

print(sys.version_info) #(major=3, minor=7, micro=0, releaselevel='final', serial=0)

print(sys.modules) #Modules importing auto by python
sys_output = sys.__stdout__
print(sys.path) #sys.path is an environment varibles for python

sys.exit() #Stop your running python script
print("Hello2")


