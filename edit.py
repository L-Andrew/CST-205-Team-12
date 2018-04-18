from PIL import Image

#img1 = Image.open("1.png")
#img2 = Image.open("2.png")

def distance(color_1, color_2):
    red_diff = math.pow((color_1[0] - color_2[0]), 2)
    green_diff = math.pow((color_1[1] - color_2[1]), 2)
    blue_diff = math.pow((color_1[2] - color_2[2]), 2)
    return math.sqrt(red_diff + green_diff + blue_diff)

def chromakey(source, bg):
    white = (0, 0, 0)
    for x in range(source.width):
        for y in range(source.height):
            cur_pixel = source.getpixel((x,y))
            if distance(cur_pixel, white) < 250:
                # grab the color at the same spot from the new background
                source.putpixel((x,y), bg.getpixel((x,y)))
    source.save("result.png")
    source.show()

def crop(source, x1, y1, x2, y2):
    if (x1 != x2 and y1 != y2):
        size = (min(source.width, max(x1, x2)) - min(x1, x2), min(source.height, max(y1, y2)) - min(y1, y2))
        new_img = Image.new("RGB", size, "white")
        for x in range(min(x1, x2), min(source.width, max(x1, x2))):
            for y in range(min(y1, y2), min(source.height, max(y1, y2))):
                new_img.putpixel((x - min(x1, x2), y - min(y1, y2)), source.getpixel((x, y)))
        new_img.save("result.png")
        new_img.show()
    else:
        print("x1 == x2 || y1 == y2")

def resize(source, percent):
    size = (int(percent * source.width), int(percent * source.height))
    new_img = Image.new("RGB", size, "white")
    for x in range(size[0]):
        for y in range(size[1]):
            new_img.putpixel((x, y), source.getpixel((int(x / percent), int(y / percent))))
    new_img.show()
    new_img.save("result.png")

#chromakey(img2, img1)
#crop(img1, int(img1.width*.2), int(img1.height*.2), int(img1.width*.8), int(img1.height*.8))
#resize(img1, 0.5)
#resize(img1, 2)
