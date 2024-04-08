import math

from app.models import dataclasses


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
