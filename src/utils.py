"""
16/09/2023 1:18pm ENE DANIELE
Utilities
"""
from PIL import Image


def compare(a, b):
    result = 0
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise Exception("Compared images must have the same resolution")
    else:
        for wa, wb in zip(range(len(a)), range(len(b))):
            for ha, hb in zip(a[wa], b[wb]):
                result += abs(sum(ha) - sum(hb))
    return result


def open_image(path):
    skip_rate = 50  # Determines how many pixels to skip when iterating over width and height
    result = []
    im = Image.open(f"../images/{path}.jpg").convert("RGB")
    for w in range(0, im.width, skip_rate):
        temp = []
        for h in range(0, im.height, skip_rate):
            r, g, b = im.getpixel((w, h))
            temp.append([r, g, b])
        result.append(temp)
    return result
