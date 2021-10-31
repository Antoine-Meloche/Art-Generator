import PIL
from PIL import Image, ImageDraw
import math
import random
from pathlib import Path
import imageio


def generate(width, height, bkg, fg, pipes, prob, export_path):
    xincr = 50
    yincr = 100

    frames = []
    direction = "vertical"
    pt = [width//2, height//2]
    for _ in range(pipes):
        image = Image.new('RGB', (width, height), color=bkg)
        for i in range(50):
            if random.randrange(1, (1//prob)+1, 1) == 1:
                if direction == "vertical":
                    direction = "horizontal"
                else:
                    direction = "vertical"

                # image = Image.new('RGB', (width, height), color=bkg)

                if direction == "vertical":
                    y = pt[1]+(yincr*random.randrange(-1, 2, 2))
                    ImageDraw.Draw(image).line(
                        (pt[0], pt[1], pt[0], y), fill=fg)
                    pt = [pt[0], y]
                else:
                    x = pt[0]+(xincr*random.randrange(-1, 2, 2))
                    ImageDraw.Draw(image).line(
                        (pt[0], pt[1], x, pt[1]), fill=fg)
                    pt = [x, pt[1]]
                # frames.append(image)
            image.save(f'tmp/image{i}.png')

    path = Path('tmp/')
    imgs = list(path.glob('image*.png'))
    img_list = []
    for img in imgs:
        img_list.append(imageio.imread(img))

    imageio.mimwrite('animated.gif', img_list)

    # image.save("image.gif.png")
    # frames[0].save(export_path, save_all=True, format='GIF',
    #    append_images=frames[1:], duration=200, loop=0, optimize=True)
    return 201
