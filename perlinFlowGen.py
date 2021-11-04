from random import randrange
# import PIL
from PIL import Image, ImageFilter, ImageDraw
# import numpy as np


def generate(width: int, height: int, fg: str, bkg: str, octaves: int, export_path: str):
    image = Image.new('RGB', (width, height), color=bkg)
    draw = ImageDraw.Draw(image)
    pixels = image.load()

    grid = noise(octaves)

    ratiox = width/octaves
    ratioy = height/octaves

    for row in range(octaves):
        for col in range(octaves):
            draw.rectangle([(row*ratiox-(ratiox-1), col*ratioy-(ratioy-1)), (row*ratiox, col*ratioy)], fill=grid[row][col])
            # pixels[row, col] = grid[row][col]

    # gridimg = Image.fromarray(noise(octaves))

    # if gridimg.mode != 'RGB':
    #     gridimg.convert('RGB').save("tmp.png")
    # else:
    #     gridimg.save("tmp.png")
    for _ in range(10):
        image = image.filter(ImageFilter.BLUR)
    image.save("tmp.png")
    return 201


def noise(octaves: int):
    # grid = np.zeros(octaves**2).reshape(octaves, octaves)
    grid=[]

    # for row in range(grid.shape[0]):
    for row in range(octaves):
        grid.append([])
        # for col in range(grid.shape[1]):
        for _ in range(octaves):
            # grid[row].append((255, 255, 255) if randrange(
            #     0, 2, 1) == 1 else (0, 0, 0))
            grid[row].append("#ffffff" if randrange(
                0, 2, 1) == 1 else "#000000")

    return grid
