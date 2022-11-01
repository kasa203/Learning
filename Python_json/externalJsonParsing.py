# ****** Parse content from JSON file*******#
import json

with open('example.json') as f:
    data = json.load(f)

# print(data,type(data))

myItem = data['widget']
# print(myItem.keys())
print(data['widget']['text']['style'])
# for value,key in myItem.items():
#     print(f"{value},{key} \n")