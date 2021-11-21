import PIL
from PIL import Image, ImageDraw
import math

def generate(width, height, fg, bkg, n, steps, substeps, length, angleincr, angle, exportPath):
    bkg_color = (int(bkg[1:3], base=16), int(bkg[3:5], base=16), int(bkg[5:7], base=16))
    image = Image.new('RGB', (width, height), color=bkg_color)
    draw = ImageDraw.Draw(image)

    pt = [(-200), image.size[1]-2]
    points = []

    collatz_up(steps, substeps, n, pt, length,
               angle, angleincr, draw, fg, points)

    while len(points) > 0:
        for point in points:
            steps = point[0]
            n = point[1]
            pt = [point[2], point[3]]
            angle = point[4]

            collatz_up(steps, substeps, n, pt, length, angle,
                       angleincr, draw, fg, points)

            del points[points.index(point)]

    try:
        print("ok")
        image.save(exportPath)
        print("ok")
    except:
        return 418
    return 201


def is_even(n):
    if (n % 2) == 0:
        return True
    else:
        return False


def collatz_up(steps, substeps, n, pt, length, angle, angleincr, draw, fg, points):
    for i in range(steps):
        if is_even(n):
            if (n-1) % 3 == 0:
                tmp = (n-1)//3

                points.append((steps-i, tmp, pt[0], pt[1], angle))

            for _ in range(substeps):
                angle += (angleincr//substeps)
                incx, incy = increment(angle, length, substeps)

                draw.line((pt[0], pt[1], pt[0]+incx, pt[1]+incy), fill=fg)
                pt = [pt[0]+incx, pt[1]+incy]
        else:
            for _ in range(substeps):
                angle -= (angleincr//substeps)
                incx, incy = increment(angle, length, substeps)

                draw.line((pt[0], pt[1], pt[0]+incx, pt[1]+incy), fill=fg)
                pt = [pt[0]+incx, pt[1]+incy]

        n = n*2


def increment(angle, length, substeps):
    incx = round(math.sin(math.radians(angle))*length//substeps)
    incy = round(math.cos(math.radians(angle))*length//substeps)

    if angle > 360:
        angle -= 360
        incx = round(math.sin(math.radians(angle))*length//substeps)
        incy = round(math.cos(math.radians(angle))*length//substeps)

    return incx, incy
