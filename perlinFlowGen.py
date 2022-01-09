from random import uniform, randrange
from math import pi
from PIL import Image
import math


def generate(width: int, height: int, fg: str, bkg: str, octaves: int, nb_particles: int, iterations: int, length: int, export_path: str):
    bkg_color = (int(bkg[1:3], base=16), int(
        bkg[3:5], base=16), int(bkg[5:7], base=16))
    image = Image.new('RGB', (width, height), color=bkg_color)
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

    fg1 = int(fg[1:3], base=16)
    fg2 = int(fg[3:5], base=16)
    fg3 = int(fg[5:7], base=16)

    for _ in range(nb_particles):
        pos = (randrange(0, width-1), randrange(0, height-1))

        for _ in range(iterations):
            x = pos[0]
            y = pos[1]

            if x > width:
                x -= width
            if y > height:
                y -= height

            try:
                colour1 = (pixels[x, y][0] + fg1) // 2
                colour2 = (pixels[x, y][1] + fg2) // 2
                colour3 = (pixels[x, y][2] + fg3) // 2
            except IndexError:
                pass

            pixels[x, y] = (colour1, colour2, colour3)

            angle = grid[map_num(y, 0, height, 0, octaves)
                         ][map_num(x, 0, width, 0, octaves)]

            x_incr = math.cos(angle) * length
            y_incr = math.sin(angle) * length

            pos = (abs(pos[0]+x_incr), abs(pos[1]+y_incr))

    try:
        image.save(export_path)
        return 201
    except:
        return 418


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
            k = grid[pt[1]+(i//3-2)][pt[0]+(i-3*(i//3)-2)]
        except ValueError:
            continue
        if k != 0:
            neighbours += k
            divisor += 1

    average = (neighbours + lagrange_value) / divisor
    return average


def map_num(n, start, end, t_start, t_end):
    return int((((n-start)/(end-start))*(t_end-t_start))+t_start)
