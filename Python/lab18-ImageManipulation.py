'''

Lab 18 - Image manipulation and drawing images

'''


# from PIL import Image, ImageDraw
#import colorsys

#img = Image.open("Lenna.png") # must be in same folder
#width, height = img.size
#pixels = img.load()
#
#for i in range(width):
#    for j in range(height):
#        r, g, b = pixels[i, j]
#        # h = hue, s = saturation, v = value
#        h, s, v = colorsys.rgb_to_hsv(r/87, g/201, b/133)
#
#        # do some math on h, s, v - change the values behind the rgb variables above.
#
#        r, g, b = colorsys.hsv_to_rgb(h, s, v)
#
#        #convert back to [0,255] below
#
#        r = int(r*255)
#        g = int(g*255)
#        b = int(b*255)
#
#
#        Y = int(0.299*r + 0.587*g + 0.114*b)
#
#        pixels[i, j] = (r, g, b)

# width = 500
# height = 500
# #
# img = Image.new('RGB', (width,height))
# #
# draw = ImageDraw.Draw(img)
# #
# # origin of the drawing begins at pixel (0, 0) - location top-left
#
#draw.rectangle(((0,0), (width,height)), fill="white")
# # this draws a rectangle that encompases the entire space, fills with white
# # you can see this by running the code using a starting spot such as (50, 50)
# # there will be a black edge along two sides
#
# # drawing a rectange from x0, y0 to x1, y1
# draw.rectangle(((100,100), (300,300)), fill='lightblue')
# # this inserts a rectangle in light blue off center of the image
#
# # draw a line from x0, y0, x1, y1
# color = (256, 128, 128) # pink
# #draw.line((0, 0, width, height), fill=color)
# draw.line((0, height, width, 0), fill=color)
# # these two draw.line are  going from the corners of the drawing to opposite corner
# ## what happens when I do:
# draw.line((height, width, 0, 0), fill=color)
# # same thing as the first draw.line because the variables are inverse
#
# circle_x = width/2
# circle_y = height/6
# circle_radius = 70
# draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='lightgreen')
#
# img.show()


### stick figure, well, not exactly a stick figure. ------------------------------------------------
# from PIL import Image, ImageDraw
#
# width = 500
# height = 500
# img = Image.new('RGB', (width,height))
# draw = ImageDraw.Draw(img)
# circle_x = width/2
# circle_y = height/6
# circle_radius = 70
#
# draw.rectangle(((0,0), (width,height)), fill="white")
# circle_xball = width/1
# circle_yball = height/1.5
# draw.ellipse((circle_xball-circle_radius, circle_yball-circle_radius, circle_xball+circle_radius, circle_yball+circle_radius), fill='red')
# draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='tan')
# draw.rectangle(((150,150),(350,350)), fill='grey')
# draw.line((150,180,50,250), fill='tan', width=19)
# draw.line((350,180,450,200), fill='tan', width=19)
# draw.line((180,350,160,450), fill='blue', width=24)
# draw.line((320,350,450,400), fill='blue', width=24)
# draw.text((400,300), text='kick', fill='black')
#
# img.show()

### part 4 ------------------------------------------------
# from PIL import Image, ImageDraw
# from random import randint
#
# width = 500
# height = 500
#
# img = Image.new('RGB', (width,height))
# draw = ImageDraw.Draw(img)
#
# for i in range(1000):
#     x0 = randint(0,width)
#     y0 = randint(0,height)
#     x1 = randint(0,width)
#     y1 = randint(0,height)
#     line_width = randint(5, 20)
#     red = randint(0,255)
#     green = randint(0,255)
#     blue = randint(0,255)
#     draw.line((x0, y0, x1, y1), fill=(red, green, blue), width=line_width)
#
# img.show()