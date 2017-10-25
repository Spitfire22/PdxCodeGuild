'''

Local Portland Oregon Rain Data - rain data != gray data

'''

import datetime
#
# datatime = '3-JUN-2014' # example
#
# date = datetime.datetime.strptime(datatime, '%d-%b-%Y')
# print(date.year)
# print(date.month)
# print(date.day)
#
# with open('raindata.txt', 'r') as file:
#     lines = file.read().split('\n')
#
# print(lines)


def load_file(rain_file):
    header = []
    rain_data = []
    with open(rain_file, 'r') as file:
        lines = file.read().split('\n')
        for i in range(12,len(lines)):
            rain_values = lines[i].split('  ')




rain_file = 'raindata.txt'