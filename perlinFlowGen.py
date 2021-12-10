## # # import random
# # # from PIL import Image, ImageFilter, ImageDraw


# # # def generate(width: int, height: int, fg: str, bkg: str, octaves: int, export_path: str):
# # #     image = Image.new('RGB', (width, height), color=bkg)
# # #     draw = ImageDraw.Draw(image)
# # #     pixels = image.load()

# # #     noise(octaves, pixels, width, height)

# # #     image.save("tmp.png")
# # #     return 201


# # # def noise(octaves: int, pixels, width: int, height: int):
# # #     set1 = []

# # #     pts = []
# # #     for x in range(octaves):
# # #         rand_y = random.random()
# # #         pts.append((x, rand_y))

# # #     pts = list(map(lambda pt: (map_nums(pt[0], octaves, width), map_nums(pt[1], 1, 1300)), pts))

# # #     # x = 0
# # #     # while x <= width:
# # #     for x in range(width+1):
# # #         y = 0
# # #         for i in range(len(pts)):
# # #             jresult = 1
# # #             for j in range(len(pts)):
# # #                 if i == j:
# # #                     continue
# # #                 jresult *= ((x-pts[j][0])/(pts[i][0]-pts[j][0]))
# # #             y += pts[i][1]*jresult

# # #         set1.append((x, y))
# # #         try:
# # #             pixels[x, y] = (255, 255, 255)
# # #         except IndexError:
# # #             continue

# # #     # x = 0
# # #     # while x <= width:
# # #     for x in range(width+1):
# # #         y = 0
# # #         for i in range(len(set1)):
# # #             jresult = 1
# # #             for j in range(len(set1)):
# # #                 if i == j:
# # #                     continue
# # #                 jresult *= ((x-set1[j][0])/(set1[i][0]-set1[j][0]))
# # #             y += set1[i][1]*jresult

# # #         y = map_nums(y, 2100, 100)

# # #         set1[x] = (set1[x][0], (set1[x][1]+y)-height//2)


# # #     # for (x, y) in set1:
# # #     #     try:
# # #     #         pixels[x, y] = (255, 255, 255)
# # #     #     except IndexError:
# # #     #         continue


# # # def map_nums(value, init_stop, stop):
# # #     return value / init_stop * stop


"""
    New Code
"""

from random import randrange
import random
from math import pi

def generate(width: int, height: int, fg: str, bkg: str, octaves: int, export_path: str):
    pts = []
    for _ in range(octaves):
        pts.append(randrange(-pi, pi))
    
    grid = []
    for _ in range(octaves):
        row = []
        for _ in range(octaves):
            row.append(0)
        grid.append(row)

    pt = (octaves//2, octaves//2)

    while in_nested(grid, 0):
        noise(pts, pt, octaves)
        if grid[pt[1]+1][pt[0]] == 0:
            pt = (pt[0], pt[1]+1)
        elif grid[pt[1]+1][pt[0]+1] == 0:
            pt = (pt[0]+1, pt[1]+1)
        elif grid[pt[1]][pt[0]+1] == 0:
            pt = (pt[0]+1, pt[1])
        elif grid[pt[1]-1][pt[0]+1] == 0:
            pt = (pt[0]+1, pt[1]-1)
        elif grid[pt[1]-1][pt[0]] == 0:
            pt = (pt[0], pt[1]-1)
        elif grid[pt[1]-1][pt[0]-1] == 0:
            pt = (pt[0]-1, pt[1]-1)
        elif grid[pt[1]][pt[0]-1] == 0:
            pt = (pt[0]-1, pt[1])
        elif grid[pt[1]+1][pt[0]-1] == 0:
            pt = (pt[0]-1, pt[1]+1)
        else:
            for i in range(octaves):
                try:
                    pt = (grid[i].index(0), i)
                    break
                except ValueError:
                    continue

def noise(pts, pt, octaves):
    x = 0
    while x < octaves:
        y = 0
        for i in range(len(pts)):
            jresult = 1
            for j in range(len(pts)):
                if i == j:
                    continue
                jresult *= ((x-pts[j][0])/(pts[i][0]-pts[j][0]))
            y += pts[i][1]*jresult
        x += .01
    return y

def in_nested(nest, num):
    for nested in nest:
        if num in nested:
            return True
        else:
            return False