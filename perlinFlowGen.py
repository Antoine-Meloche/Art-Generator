import random
from PIL import Image, ImageFilter, ImageDraw


def generate(width: int, height: int, fg: str, bkg: str, octaves: int, export_path: str):
    image = Image.new('RGB', (width, height), color=bkg)
    draw = ImageDraw.Draw(image)
    pixels = image.load()

    noise(octaves, pixels, width, height)

    image.save("tmp.png")
    return 201


def noise(octaves: int, pixels, width: int, height: int):
    set1 = []

    pts = []
    for x in range(octaves):
        rand_y = random.random()
        pts.append((x, rand_y))

    pts = list(map(lambda pt: (map_nums(pt[0], octaves, width), map_nums(pt[1], 1, height)), pts))

    x = 0
    # for x in range(1,width+1):
    while x <= width:
        y = 0
        for i in range(len(pts)):
            jresult = 1
            for j in range(len(pts)):
                if i == j:
                    continue
                jresult *= ((x-pts[j][0])/(pts[i][0]-pts[j][0]))
            y += pts[i][1]*jresult

        if x % .5 == 0:
            set1.append((x, y))

        x += .5

    x = 0
    # for x in range(1,width+1):
    while x <= width:
        y = 0
        for i in range(len(set1)):
            jresult = 1
            for j in range(len(set1)):
                if i == j:
                    continue
                jresult *= ((x-set1[j][0])/(set1[i][0]-set1[j][0]))
            y += set1[i][1]*jresult

        set1[x*2][1] += y

        x += .5

    for (x, y) in set1:
        try:
            pixels[x, y] = (255, 255, 255)
        except IndexError:
            continue


def map_nums(value, init_stop, stop):
    return (value - 0) / init_stop * stop