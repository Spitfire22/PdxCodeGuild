from turtle import *
'''
this draws a Daniel-san from Karate Kid.
'''

pu()
goto(0,120)
pd()
circle(50)
#head
forward(90)
right(90)
forward(220)
right(90)
forward(180)
right(90)
forward(220)
right(90)
forward(90)
right(90)
pu()
goto(90,80)
pd()
# Right Arm
left(90)
forward(90)
left(90)
forward(90)
circle(10)
pu()
goto(-90,80)
pd()
# Left Arm
left(90)
forward(90)
right(90)
forward(90)
circle(10)
pu()
goto(-90,-100)
pd()
# Left Leg
left(90)
forward(90)
left(90)
forward(90)
# Foot
right(90)
forward(50)
left(90)
forward(30)
left(90)
forward(50)
left(90)
forward(30)
pu()
goto(90,-100)
pd()
# Right Leg
left(180)
forward(180)
# Foot
right(90)
forward(50)
left(90)
forward(30)
left(90)
forward(50)
left(90)
forward(30)
# End stick figure
# begin letter 'K'

pu()
goto(-250,300)
pd()
left(180)
forward(50)
left(180)
forward(25)
right(144)
forward(35)
pu()

goto(-250,280)
pd()
left(80)
forward(35)

# Begin letter 'A'
pu()

done()