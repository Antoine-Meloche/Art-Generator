from PIL import Image, ImageDraw
import math
import random

def generate(width, height, fg, bkg, n, steps, substeps, length, angleincr, angle, exportPath):
    image = Image.new('RGB', (width, height), color=bkg)
    draw = ImageDraw.Draw(image)

    pt = [(-200), image.size[1]-2]
    points = []

    collatz_up(steps, substeps, n, pt, length, angle, angleincr, draw, fg, points)

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
        image.save(exportPath)
    except Error:
        return 418
    return 201


def is_even(n):
    if (n % 2) == 0:
        return True
    else:
        return False


def collatz_up(steps: int, substeps: int, n: int, pt: list, length: int, angle: int, angleincr: int, draw: 'PIL.ImageDraw.ImageDraw', fg: str, points: list) -> None:
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