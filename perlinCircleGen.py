import PIL
from PIL import Image, ImageDraw
import math
from noise import snoise3
import random

def generate(width, height, fg, bkg):

    fg_color = (int(fg[1:3], 16), int(fg[3:5], 16), int(fg[5:7], 16))

    xoff = width/2
    yoff = height/2

    spread = 600

    frames = []

    for i in range(24):
        angle = 0
        image = Image.new('RGB', (width, height), color=bkg)
        pixels = image.load()

        z = random.random()

        while angle < 1080:
            x1 = (math.cos(math.radians(angle)))
            y1 = (math.sin(math.radians(angle)))
            radius = snoise3(x1, y1, z) * spread
            x = radius * math.cos(angle) - xoff
            y = radius * math.sin(angle) - yoff
            pixels[x,y] = fg_color
            angle += 0.1

        frames.append(image)
    
    frames[0].save('animated.png', format='PNG', append_images=frames[1:], save_all=True, duration=100, loop=0)