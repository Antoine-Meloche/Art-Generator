from PIL import Image
import math
# from noise import snoise3
from perlin_noise import PerlinNoise
import random

def generate(width: int, height: int, fg: str, bkg: str, export_path: str):

    fg_color = (int(fg[1:3], 16), int(fg[3:5], 16), int(fg[5:7], 16))

    xoff = width/2
    yoff = height/2

    spread = width//2-100 if width < height else height//2-100

    angle = 0
    image = Image.new('RGB', (width, height), color=bkg)
    pixels = image.load()

    z = random.random()

    noise = PerlinNoise()

    while angle < 1080:
        x1 = (math.cos(math.radians(angle)))
        y1 = (math.sin(math.radians(angle)))
        radius = noise([x1, y1, z]) * spread
        x = radius * math.cos(angle) - xoff
        y = radius * math.sin(angle) - yoff
        pixels[x,y] = fg_color
        angle += 0.1

    try:
        image.save(export_path)
    except:
        return 418
    return 201