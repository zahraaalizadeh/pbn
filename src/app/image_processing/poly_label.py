from app.models import dataclasses


def get_seg_dist_sq(
    px: float, py: float, a: dataclasses.Point, b: dataclasses.Point
) -> float:
    """
    Calculate the squared Euclidean distance from a point (px, py) to a line segment [a-b].

    :param px: X coordinate of the point
    :param py: Y coordinate of the point
    :param a: Point object representing the start of the segment
    :param b: Point object representing the end of the segment
    :return: The squared distance from the point to the segment
    """
    x = a.x
    y = a.y
    dx = b.x - x
    dy = b.y - y

    if dx != 0 or dy != 0:
        t = ((px - x) * dx + (py - y) * dy) / (dx * dx + dy * dy)

        if t > 1:
            x = b.x
            y = b.y
        elif t > 0:
            x += dx * t
            y += dy * t

    dx = px - x
    dy = py - y

    return dx * dx + dy * dy
