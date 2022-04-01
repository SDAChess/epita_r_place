from PIL import Image
import numpy as np

IMAGE = "EPITA.png"

def color_to_string(color):
    if color == (255, 255, 255, 255):
        return "WHITE"
    elif color == (228, 228, 228, 255):
        return "PLATEWHITE"
    elif color == (0, 0, 0, 255):
        return "BLACK"
    elif color == (36, 80, 164, 255):
        return "BLUE"
    elif color == (54, 144, 234, 255):
        return "LIGHTBLUE"

OFFSET = (963, 428)

im = Image.open(IMAGE)
pixels = list(im.getdata())
width, height = im.size
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

for j in range(width):
    for i in range(height):
        if pixels[i][j] != (0, 0, 0, 0):
            print(pixels[i][j])
            #print("https://www.reddit.com/r/place/?cx=" + str(j + OFFSET[0]) + "&cy=" +
            #        str(i + OFFSET[1]) +"&px=10")
            #print(f"{OFFSET[0] + j},{OFFSET[1] + i},{color_to_string(pixels[i][j])}")
