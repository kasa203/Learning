list1 = []

for i in range(10):
    result = i ** 2
    list1.append(result)

print(list1)

list2 = [x ** 2 for x in range(10)]
print(list2)

list3 = [x ** 2 for x in range(10) if x > 5]
print(list3)

set1 = {x ** 2 for x in range(10)}
print(set1, type(set1))

dict1 = {x: x * 2 for x in range(10)}
print(dict1)

# List / Set / Dictionary comprehensions
# Instead of...
list1 = []
for i in range(10):
    j = i ** 2
    list1.append(j)

# ...we can use a list comprehension
list2 = [x ** 2 for x in range(10)]

list3 = [x ** 2 for x in range(10) if x > 5]  # with a conditional statament

set1 = {x ** 2 for x in range(10)}  # set comprehension

dict1 = {x: x * 2 for x in range(10)}  # dictionary comprehension

list4 = [x * 10 for x in range(11) if x >= 7]
print([x * 10 for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if x >= 7])
print(list4)