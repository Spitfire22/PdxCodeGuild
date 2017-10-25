'''

Local Portland Oregon Rain Data - rain data != gray data

'''

import datetime
import math

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
    rain_data = []
    with open(rain_file, 'r') as file:
        lines = file.read().split('\n')
        for i in range(11,len(lines)-1):
            rain_values = lines[i].split()
            rain_values[0] = datetime.datetime.strptime(rain_values[0], '%d-%b-%Y')
            for j in range(1, len(rain_values)):
                if rain_values[j] != '-':
                    rain_values[j] = int(rain_values[j])
            rain_data.append(rain_values)
    return rain_data


# def average(rain_data):
#     # using the rain_data[1] which is daily rainfall. Calc average.
#     avg = 0
#     for num in rain_data[1]:
#         avg += num
#     return avg/len(rain_data)
#
# def variance(nums, average):
#     total = 0
#     for num in nums:
#         diff = num - average
#         total += diff*diff
#     return total/len(nums)

#av = average( insert nums )
#var = variance( insert nums, av)
#std = math.sqrt(var)




# index 1 is the total of the day of each list

rain_file = 'raindata.txt'
rain_data = load_file(rain_file)
# rain_avg = average(rain_data)
print(rain_data)
# print(rain_avg)


