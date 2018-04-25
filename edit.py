from PIL import Image
import math

img1 = Image.open("1.png").convert("RGB")
img2 = Image.open("2.png").convert("RGB")

DEBUG = True

def distance(color_1, color_2):
    red_diff = math.pow((color_1[0] - color_2[0]), 2)
    green_diff = math.pow((color_1[1] - color_2[1]), 2)
    blue_diff = math.pow((color_1[2] - color_2[2]), 2)
    return math.sqrt(red_diff + green_diff + blue_diff)

def chromakey(source, bg):
    new_img = source.copy()
    white = (0, 0, 0)
    for x in range(source.width):
        for y in range(source.height):
            cur_pixel = source.getpixel((x,y))
            if distance(cur_pixel, white) < 250:
                # grab the color at the same spot from the new background
                new_img.putpixel((x,y), bg.getpixel((x,y)))
    if DEBUG:
        new_img.show()
    return source

def crop(source, x1, y1, x2, y2):
    if (x1 != x2 and y1 != y2):
        size = (min(source.width, max(x1, x2)) - min(x1, x2), min(source.height, max(y1, y2)) - min(y1, y2))
        new_img = Image.new("RGB", size)
        for x in range(min(x1, x2), min(source.width, max(x1, x2))):
            for y in range(min(y1, y2), min(source.height, max(y1, y2))):
                new_img.putpixel((x - min(x1, x2), y - min(y1, y2)), source.getpixel((x, y)))
        # new_img.save("result.png")
        if DEBUG:
            new_img.show()
        return new_img
    else:
        print("x1 = x2 OR y1 = y2")

def resize(source, percent):
    size = (int(percent * source.width), int(percent * source.height))
    new_img = Image.new("RGB", size)
    for x in range(size[0]):
        for y in range(size[1]):
            new_img.putpixel((x, y), source.getpixel((int(x / percent), int(y / percent))))
    if DEBUG:
        new_img.show()
    return new_img

def collageH(source, *sourceList):
    totalX = source.width
    sList = list(sourceList)
    for i, img in enumerate(sList):
        if (img.height != source.height):
            img = resize(img, source.height/img.height)
            sList[i] = img
        totalX = totalX + img.width
    new_img = Image.new("RGB", (totalX, source.height))
    for x in range(source.width):
        for y in range(source.height):
            new_img.putpixel((x, y), source.getpixel((x, y)))
    offsetX = source.width
    for img in sList:
        for x in range(img.width):
            for y in range(img.height):
                new_img.putpixel((offsetX + x, y), img.getpixel((x, y)))
        offsetX = offsetX + img.width
    if DEBUG:
        new_img.show()
    return new_img

def collageV(source, *sourceList):
    totalY = source.height
    sList = list(sourceList)
    for i, img in enumerate(sList):
        if (img.width != source.width):
            img = resize(img, source.width/img.width)
            sList[i] = img
        totalY = totalY + img.height
    new_img = Image.new("RGB", (source.width, totalY))
    for x in range(source.width):
        for y in range(source.height):
            new_img.putpixel((x, y), source.getpixel((x, y)))
    offsetY = source.height
    for img in sList:
        for x in range(img.width):
            for y in range(img.height):
                new_img.putpixel((x, offsetY + y), img.getpixel((x, y)))
        offsetY = offsetY + img.height
    if DEBUG:
        new_img.show()
    return new_img

def filterGrayscale(source):
    new_img = source.copy()
    for x in range(source.width):
        for y in range(source.height):
            r, g, b = source.getpixel((x, y))
            avg = int((r + g + b) / 3)
            new_img.putpixel((x,y), (avg, avg, avg))
    if DEBUG:
        new_img.show()
    return new_img

def filterR(source, percent):
    new_img = source.copy()
    for x in range(source.width):
        for y in range(source.height):
            r, g, b = source.getpixel((x, y))
            r = int(r * percent)
            new_img.putpixel((x,y), (r, g, b))
    if DEBUG:
        new_img.show()
    return new_img

def filterG(source, percent):
    new_img = source.copy()
    for x in range(source.width):
        for y in range(source.height):
            r, g, b = source.getpixel((x, y))
            g = int(g * percent)
            new_img.putpixel((x,y), (r, g, b))
    if DEBUG:
        new_img.show()
    return new_img

def filterB(source, percent):
    new_img = source.copy()
    for x in range(source.width):
        for y in range(source.height):
            r, g, b = source.getpixel((x, y))
            b = int(b * percent)
            new_img.putpixel((x,y), (r, g, b))
    if DEBUG:
        new_img.show()
    return new_img

def filterCustom(source, rPercent, gPercent, bPercent):
    new_img = source.copy()
    new_img = filterR(filterG(filterB(new_img, bPercent), gPercent), rPercent)
    if DEBUG:
        new_img.show()
    return new_img

# crop(img1, int(img1.width*.2), int(img1.height*.2), int(img1.width*.8), int(img1.height*.8))
# resize(img1, 0.5)
# resize(img1, 2)
# collageH(img1, img2)
# collageV(img1, img2)
# filterGrayscale(img1)
# collageH(img1, img1, img2, img1)
# collageV(img1, img1, img2, img1)
# filterR(img2, 2)
# collageH(collageV(filterR(img1, 5), filterG(img2, 5), filterB(img1, 5), filterGrayscale(img1)), crop(img2, 100, 300, 500, 600))
# filterCustom(img1, 3, 1, 1)
# filterR(img1, 3)
