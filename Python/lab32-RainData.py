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
            #print(rain_values[1])
    return rain_data


def average(rain_data):
    # using the rain_data[1] which is daily rainfall. Calc average.
    avg = 0
    count = 0
    for data_row in rain_data:
        if data_row[1] != '-':
            avg += data_row[1]
            count += 1
    return avg/count

def variance(rain_data, rain_avg):
    total = 0
    count = 0
    for data_row in rain_data:
        if data_row[1] != '-':
            diff = int(data_row[1]) - rain_avg
            total += diff*diff
            count += 1
    return total/count

# av = average( insert nums )
# var = variance( insert nums, av)
# std = math.sqrt(var)



rain_file = 'raindata.txt'
rain_data = load_file(rain_file)
print(rain_data)
rain_avg = average(rain_data)
print('Average rainfall in inches: ',rain_avg)
rain_var = variance(rain_data, rain_avg)
print('Rain variance: ', rain_var)

## Now look for the highest value in the rain_data
## then look for the year that has the most rain on average.




## Version 3 - Look at the
