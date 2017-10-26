'''

Local Portland Oregon Rain Data - rain data != gray data

'''

import datetime
import math
import matplotlib.pyplot as plt

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

# find the day that returned max sky_water
def max_rain(rain_data):
    count = 0
    sky_water = 0
    date = 0
    for data_row in rain_data:
        if data_row[1] != '-':
            if int(data_row[1]) > sky_water:
                sky_water = int(data_row[1])
                date = (data_row[0])
            count += 1
    #return sky_water, str(date.month), str(date.day), str(date.year) # this returns a string of each
    return sky_water, str(date.date())

def max_year(rain_data):
    years = []
    # pulling the years out of the data and appending them to a list.
    for data_row in rain_data:
        year = data_row[0].year
        if year in years:
            continue
        years.append(year)
    years.sort()
    # print(years)
    #loop through the data of each year to return the total rainfall and number of counts of that year
    averages = []
    counts = []
    for year in years:
        total = 0
        count = 0
        for data_row in rain_data:
            if data_row[0].year == year:
                if data_row[1] != '-':
                    total += data_row[1]
                    count += 1
        averages.append(total/count), counts.append(count)
    # print(averages)
    # print(counts)
    # find the largest value, find the index of that value,
    high_avg = 0
    high_avg_year = 0
    for index, num in enumerate(averages):
        if num > high_avg:
            high_avg = num
            high_avg_year = years[index]

    # print(high_avg)
    return high_avg, high_avg_year

## Ideally computing the data: use a dictionary to break into key value pairs
## (keys = years, values = rain total & count)
## after the dictionary is populated, then you can calculate the averages using the values of the dictionary.
# sky_water_dict = {
#     2010: {total: 'total', count: 'count'},
#     2011: {total: 'total', count: 'count'}
# }
# count_dict = {2010: 3}
# total_dict = {2010: 45}

rain_file = 'raindata.txt'
rain_data = load_file(rain_file)
# print(rain_data)
rain_avg = average(rain_data)
print('Average rainfall in inches: ',rain_avg)
rain_var = variance(rain_data, rain_avg)
print('Rain variance: ', rain_var)
fallen_water = max_rain(rain_data)
print('Highest daily rainfall: ',fallen_water)
max = max_year(rain_data)
print('Highest Avg rainfall through years 2005-2017: ',max)


## Version 3 - Look at the

def plotting(rain_data):
    y_values = data_row[1]
    # I want to use the daily totals in the
    x_values = data_row[0]
    # I want to use the date as the x_val
    plt.plot(x_values, y_values)
    plt.ylabel('rainfall')
    plt.xlabel('date')
    plt.show()

plotting(rain_data)