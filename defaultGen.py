from PIL import Image


def generate(width, height, bkg, exportPath):
    image = Image.new('RGB', (width, height), color=bkg)
    try:
        image.save(exportPath)
    except Error:
        return 418
    return 201
