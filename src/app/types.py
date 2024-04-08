from typing import List, NamedTuple


class Point(NamedTuple):
    x: float
    y: float


PolygonRing = List[Point]
Polygon = List[PolygonRing]


class PointResult(NamedTuple):
    pt: Point
    distance: float
