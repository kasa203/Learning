import json

#https://jsoneditoronline.org

courses = '{"name": "Asaf", "lang": ["Python", "C"]}'

#Loads method parse json strings and it returns dict
dict_courses = json.loads(courses)
# print(type(dict_courses))
# print(dict_courses)

print(dict_courses['name'])
print(dict_courses['lang'][0])

item = 0
for key,value in dict_courses.items():
    item += 1
    print(f"{item}:{key}:{value}")


