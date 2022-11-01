import json

with open('example.json') as fi:
    data1 = json.load(fi)

with open('example_2.json') as f:
    data2 = json.load(f)
    # print(data1 == data2)
    assert data1 == data2