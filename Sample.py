from PIL import Image, ImageDraw
import sys
im = Image.open(utImage)

x1 = 580
y1 = 1630
x3 = 2180

anothercounter = 1
for i in range(x1, x3, 100):
    draw = ImageDraw.Draw(im)
    x4 = x1 + anothercounter*100
    draw.line([x1, y1, x4, y1], width=10, fill=RED)
    outImage = outdirectory + "Image" + '{:03d}'.format(filenamecounter) + ".png"
    # im.show()
    im.save(outImage)
    filenamecounter += 1
    anothercounter += 1

draw = ImageDraw.Draw(im)
draw.line([x1, y1, 2300, y1], width=10, fill=RED)
outImage = outdirectory + "Image" + '{:03d}'.format(filenamecounter) + ".png"
im.save(outImage)
