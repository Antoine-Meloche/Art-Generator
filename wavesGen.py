from PIL import Image
import math
from random import random as rand

def generate(width: int, height: int, fg: str, bkg: str, duration: int, framerate: int, functions: int, export_path: str):
    frames = duration * framerate
    bkg_color = (int(bkg[1:3], base=16), int(bkg[3:5], base=16), int(bkg[5:7], base=16))
    fg_color = (int(fg[1:3], base=16), int(fg[3:5], base=16), int(fg[5:7], base=16))

    images = []

    for i in range(frames):
        image = Image.new('RGB', (width, height), color=bkg_color)
        pixels = image.load()
        for j in range(functions):
            h = i*(j+1)
            draw_sin_circ(h, width, height, fg_color, pixels)
        images.append(image)

    try:
        appends = images[1:]
        appends.extend(images[::-1][:-1])
        images[0].save("tmp.webp", format='WEBP', append_images=appends, save_all=True, duration=duration, loop=0)
    except:
        return 418
    return 201

def draw_sin_circ(h: int, width: int, height: int, fg_color: tuple, pixels):
    angle = 0
    radius = 100
    while angle <= 360:
        # x = (radius+radius*math.sin(math.radians(1*(angle-h)))) * math.cos(math.radians(angle)) + width//2
        x = (radius-h+((radius-h)*math.sin(math.radians(10*(angle-h))))) * math.cos(math.radians(angle)) + width//2

        # y = (radius+radius*math.sin(math.radians(1*(angle-h)))) * math.sin(math.radians(angle)) + height//2
        y = (radius-h+((radius-h)*math.sin(math.radians(10*(angle-h))))) * math.sin(math.radians(angle)) + height//2
        try:
            if y < 0 or x < 0:
                raise IndexError
            pixels[x, y] = fg_color
        except IndexError:
            pass
        angle += 0.1
    # for x in range(100):
    #     print(16800 - x**2)
    #     y1 = math.sqrt(16800 - x**2)+(math.sin(x-h)/2)
    #     y2 = -math.sqrt(16800 - x**2)+(math.sin(x-h)/2)
    #     x = x+(math.sin(x-h)/2)
    #     try:
    #         pixels[x, y1] = fg_color
    #         pixels[x, y2] = fg_color
    #     except IndexError:
    #         pass