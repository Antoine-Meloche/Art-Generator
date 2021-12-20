# import random
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

from random import uniform
# import random
from math import pi
from PIL import Image, ImageDraw


def generate(width: int, height: int, fg: str, bkg: str, octaves: int, export_path: str):
    bkg_color = (int(bkg[1:3], base=16), int(bkg[3:5], base=16), int(bkg[5:7], base=16))
    image = Image.new('RGB', (octaves, octaves), color=bkg_color)
    pixels = image.load()

    pts = []
    for _ in range(octaves):
        pts.append(uniform(-pi, pi))

    grid = []
    for _ in range(octaves):
        row = []
        for _ in range(octaves):
            row.append(0)
        grid.append(row)

    pt = (octaves//2, octaves//2)
    direction = "down"

    x = uniform(0, octaves)

    while in_nested(grid, 0):
        prev_x = x
        x = (prev_x+uniform(0, octaves))/2
        lagrange_value = noise(pts, x)
        value = average_k(grid, pt, lagrange_value)
        grid[pt[1]][pt[0]] = abs(value)

        try:
            pt_changed = False
            if direction == "down":
                if grid[pt[1]][pt[0]+1] == 0:
                    pt = (pt[0]+1, pt[1])
                    pt_changed = True
                elif grid[pt[1]+1][pt[0]] == 0:
                    pt = (pt[0], pt[1]+1)
                    pt_changed = True
            elif direction == "right":
                if grid[pt[1]-1][pt[0]] == 0:
                    pt = (pt[0], pt[1]-1)
                    pt_changed = True
                elif grid[pt[1]][pt[0]+1] == 0:
                    pt = (pt[0]+1, pt[1])
                    pt_changed = True
            elif direction == "up":
                if grid[pt[1]][pt[0]-1] == 0:
                    pt = (pt[0]-1, pt[1])
                    pt_changed = True
                elif grid[pt[1]-1][pt[0]] == 0:
                    pt = (pt[0], pt[1]-1)
                    pt_changed = True
            elif direction == "left":
                if grid[pt[1]+1][pt[0]] == 0:
                    pt = (pt[0], pt[1]+1)
                    pt_changed = True
                elif grid[pt[1]][pt[0]-1] == 0:
                    pt = (pt[0]-1, pt[1])
                    pt_changed = True
            
            if pt_changed == False:
                new_point(octaves, grid)
        except:
            pt = new_point(octaves, grid)
            if pt == None:
                print("done")

        # pos = ""
        # if pt[0] == len(grid)-1:
        #     pos = "right"
        # if pt[0] == 0:
        #     pos = "left"
        # if pt[1] == len(grid)-1:
        #     if pt[0] == 0:
        #         pos = "bot left"
        #     elif pt[0] == len(grid)-1:
        #         pos = "bot right"
        #     else:
        #         pos = "bot"
        # if pt[1] == 0:
        #     if pt[0] == 0:
        #         pos = "top left"
        #     elif pt[0] == len(grid)-1:
        #         pos = "top right"
        #     else:
        #         pos = "top"

        # pt_changed = False

        # try:
        #     if not "bot" in pos:
        #         if grid[pt[1]+1][pt[0]] == 0:
        #             pt = (pt[0], pt[1]+1)
        #             pt_changed = True
        #     elif not "bot" in pos and not "right" in pos:
        #         if grid[pt[1]+1][pt[0]+1] == 0:
        #             pt = (pt[0]+1, pt[1]+1)
        #             pt_changed = True
        #     elif not "right" in pos:
        #         if grid[pt[1]][pt[0]+1] == 0:
        #             pt = (pt[0]+1, pt[1])
        #             pt_changed = True
        #     elif not "top" in pos and not "right" in pos:
        #         if grid[pt[1]-1][pt[0]+1] == 0:
        #             pt = (pt[0]+1, pt[1]-1)
        #             pt_changed = True
        #     elif not "top" in pos:
        #         if grid[pt[1]-1][pt[0]] == 0:
        #             pt = (pt[0], pt[1]-1)
        #             pt_changed = True
        #     elif not "top" in pos and not "left" in pos:
        #         if grid[pt[1]-1][pt[0]-1] == 0:
        #             pt = (pt[0]-1, pt[1]-1)
        #             pt_changed = True
        #     elif not "left" in pos:
        #         if grid[pt[1]][pt[0]-1] == 0:
        #             pt = (pt[0]-1, pt[1])
        #             pt_changed = True
        #     elif not "bot" in pos and not "left" in pos:
        #         if grid[pt[1]+1][pt[0]-1] == 0:
        #             pt = (pt[0]-1, pt[1]+1)
        #             pt_changed = True
        # except IndexError as e:
        #     print(pt)
        #     raise e

        # if not pt_changed:
        #     print('pt not changed')
        #     for i in range(octaves):
        #         try:
        #             pt = (grid[i].index(0), i)
        #             break
        #         except ValueError:
        #             continue
    print(grid)

    for y in range(octaves): # row
        for x in range(octaves): # column
            try:
                color_value = round((grid[y][x]*255)/(2*pi))
                pixels[x,y] = (color_value, color_value, color_value)
            except OverflowError:
                print(y, x)
                print(grid[y][x])
                quit()

    image.save(export_path)

def new_point(octaves, grid):
    for i in range(octaves):
        try:
            pt = (grid[i].index(0), i)
            break
        except ValueError:
            continue
    try:
        return pt
    except:
        return None

def noise(pts, x):
    y = 0
    for i in range(len(pts)):
        jresult = 1
        for j in range(len(pts)):
            if i == j:
                continue
            jresult *= ((x-pts[j])/(pts[i]-pts[j]))
        y += pts[i]*jresult
    return y


def in_nested(nest, num):
    for nested in nest:
        if num in nested:
            return True
    return False


def average_k(grid, pt, lagrange_value):
    neighbours = 0
    # Starts at one bc of lagrange value that will be added later in the process
    divisor = 1
    for i in range(9):
        try:
            # k = grid[pt[1]//3][pt[0]//3*3]
            k = grid[pt[1]+(i//3-2)][pt[0]+(i-3*(i//3)-2)]
        except ValueError:
            continue
        if k != 0:
            neighbours += k
            divisor += 1
            # if not neighbours+k > 18*pi:
            #     neighbours += k
            # else:
            #     neighbours -= k

    average = (neighbours + lagrange_value) / divisor
    if average > 2*pi:
        print(neighbours)
        print(lagrange_value)
        print(divisor)
        quit()
    # if average > 2*pi:
    #     average = 2*pi
    # elif average < 0:
    #     average = 0
    return average