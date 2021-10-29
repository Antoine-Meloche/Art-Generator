from warnings import filterwarnings
import PIL
from PIL import Image, ImageDraw
import math
import random


def generate(width, height, bkg, fg, pipes, prob, export_path):
    xincr = 75
    yincr = 100

    frames = []
    direction = "vertical"
    pt = [height//2, width//2]
    for _ in range(pipes):
        for _ in range(10):
            if random.randrange(1, (1//prob)+1, 1) == 1:
                if direction == "vertical":
                    direction = "horizontal"
                else:
                    direction = "vertical"

                image = Image.new('RGB', (width, height), color=bkg)
                if direction == "vertical":
                    y = pt[1]+yincr*random.randrange(-1, 2, 2)
                    ImageDraw.Draw(image).line(
                        (pt[0], pt[1], pt[0], y), fill=fg)
                    pt = [pt[0], y]
                else:
                    x = pt[0]+xincr*random.randrange(-1, 2, 2)
                    ImageDraw.Draw(image).line(
                        (pt[0], pt[1], x, pt[1]), fill=fg)
                    pt = [x, pt[1]]
                frames.append(image)
                #draw_turn(draw, direction, random.randrange(-1, 2, 2), pt)

    try:
        frames[0].save(export_path, format="GIF",
                       append_images=frames[1:], save_all=True, duration=len(frames)//24, loop=0)
    except:
        return 418
    return 201
