import csv

csv_file = r'C:\users\Asaf\Desktop\asaf.csv'

#Reading a file:
#
# cf = open(csv_file, 'r')
# content = csv.reader(cf)
#
# # print(list(content))
#
# for each_line in list(content):
#     print(each_line)
#

fo = open(csv_file, 'w')
csv_writer = csv.writer(fo, determine=',')
my_data = [['This is ','New Row'], ['This is ','New Row'], ['This is ','New Row']]

csv_writer.writerows(my_data)
fo.close()
