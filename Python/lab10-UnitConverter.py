'''
This is lab 10

'''

#Exercise #1

#feet = float(input('How long is that in feet? '))
#meter_feet = feet * .3048
#meter_feet = str(meter_feet)[:5]
## Above line will limit the number of digits on the output!
#print('Oh', feet, 'feet? That\'s', meter_feet, 'meters long in Europe.')

# Exercise #2
# meter variable is above

length = int(input('How far is that? '))
measured = length
#conversion = ['feet', 'miles', 'meters', 'kilometers', 'yards', 'inches']
query = input('is that in feet, miles, meters, kilometers, yards, inches? ')
print('You have ', length, query)
convert = input('what unit do you want to convert to? ')

if query == 'feet':
    length *= .3048
elif query == 'miles':
    length *= 1609.34
elif query == 'meters':
    length *= 1
elif query == 'kilometers':
    length *= 1000
elif query == 'yards':
    length *= .9144
elif query == 'inches':
    length *= .0254
else :
    print('That ain\'t no unit of measure I heard of...')

if convert == 'feet:':
    length /= .3048
elif convert == 'miles:':
    length /= 1609.34
elif convert == 'meters':
    length /= 1
elif convert == 'kilometers':
    length /= 1000
elif convert == 'yards':
    length /= .9144
elif convert == 'inches':
    length /= .0254
else :
    print('What?')

length = str(length)[:8]

print('You have ', measured, query, ' then convert it to ', convert, 'which is this long: ', length)



