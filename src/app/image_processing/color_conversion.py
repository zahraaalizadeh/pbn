import math

from app.models import dataclasses

#  From https://stackoverflow.com/a/9493060/694640


def rgb_to_hsl(rgb: dataclasses.RGB) -> tuple:
    """
    Converts an RGB color value to HSL. Conversion formula
    adapted from http://en.wikipedia.org/wiki/HSL_color_space.
    Assumes r, g, and b are contained in the set [0, 255] and
    returns h, s, and l in the set [0, 1].
    """
    r, g, b = rgb.r / 255.0, rgb.g / 255.0, rgb.b / 255.0
    max_color = max(r, g, b)
    min_color = min(r, g, b)
    h, s, l = 0, 0, (max_color + min_color) / 2  # noqa: E741

    if max_color == min_color:
        h = s = 0  # Achromatic
    else:
        d = max_color - min_color
        s = d / (2 - max_color - min_color) if l > 0.5 else d / (max_color + min_color)

        if max_color == r:
            h = (g - b) / d + (6 if g < b else 0)
        elif max_color == g:
            h = (b - r) / d + 2
        elif max_color == b:
            h = (r - g) / d + 4

        h /= 6

    return h, s, l


def hsl_to_rgb(hsl: dataclasses.HSL) -> list:
    """
    Converts an HSL color value to RGB. Conversion formula
    adapted from http://en.wikipedia.org/wiki/HSL_color_space.
    Assumes h, s, and l are contained in the set [0, 1] and
    returns r, g, and b in the set [0, 255].
    """

    def hue2rgb(p, q, t):
        if t < 0:
            t += 1
        if t > 1:
            t -= 1
        if t < 1 / 6:
            return p + (q - p) * 6 * t
        if t < 1 / 2:
            return q
        if t < 2 / 3:
            return p + (q - p) * (2 / 3 - t) * 6
        return p

    h, s, l = hsl.hue, hsl.saturation, hsl.lightness  # noqa: E741
    if s == 0:
        r = g = b = l  # achromatic
    else:
        q = l * (1 + s) if l < 0.5 else l + s - l * s
        p = 2 * l - q
        r = hue2rgb(p, q, h + 1 / 3)
        g = hue2rgb(p, q, h)
        b = hue2rgb(p, q, h - 1 / 3)

    return [int(r * 255), int(g * 255), int(b * 255)]


# From https://github.com/antimatter15/rgb-lab/blob/master/color.js
def lab2rgb(lab: dataclasses.LAB) -> list:
    y = (lab.L + 16) / 116
    x = lab.a / 500 + y
    z = y - lab.b / 200

    x = 0.95047 * (x**3 if x**3 > 0.008856 else (x - 16 / 116) / 7.787)
    y = 1.00000 * (y**3 if y**3 > 0.008856 else (y - 16 / 116) / 7.787)
    z = 1.08883 * (z**3 if z**3 > 0.008856 else (z - 16 / 116) / 7.787)

    r = x * 3.2406 + y * -1.5372 + z * -0.4986
    g = x * -0.9689 + y * 1.8758 + z * 0.0415
    b = x * 0.0557 + y * -0.2040 + z * 1.0570

    r = 255 * (1.055 * (r ** (1 / 2.4)) - 0.055 if r > 0.0031308 else 12.92 * r)
    g = 255 * (1.055 * (g ** (1 / 2.4)) - 0.055 if g > 0.0031308 else 12.92 * g)
    b = 255 * (1.055 * (b ** (1 / 2.4)) - 0.055 if b > 0.0031308 else 12.92 * b)

    return [max(0, min(255, r)), max(0, min(255, g)), max(0, min(255, b))]


def rgb2lab(rgb: dataclasses.RGB) -> list:
    r, g, b = rgb.r / 255.0, rgb.g / 255.0, rgb.b / 255.0

    r = ((r + 0.055) / 1.055) ** 2.4 if r > 0.04045 else r / 12.92
    g = ((g + 0.055) / 1.055) ** 2.4 if g > 0.04045 else g / 12.92
    b = ((b + 0.055) / 1.055) ** 2.4 if b > 0.04045 else b / 12.92

    x = (r * 0.4124 + g * 0.3576 + b * 0.1805) / 0.95047
    y = (r * 0.2126 + g * 0.7152 + b * 0.0722) / 1.00000
    z = (r * 0.0193 + g * 0.1192 + b * 0.9505) / 1.08883

    x = math.pow(x, 1 / 3) if x > 0.008856 else (7.787 * x) + (16 / 116)
    y = math.pow(y, 1 / 3) if y > 0.008856 else (7.787 * y) + (16 / 116)
    z = math.pow(z, 1 / 3) if z > 0.008856 else (7.787 * z) + (16 / 116)

    return [(116 * y) - 16, 500 * (x - y), 200 * (y - z)]
