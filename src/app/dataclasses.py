from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float


@dataclass
class PointResult:
    pt: Point
    distance: float


PolygonRing = list[Point]
Polygon = list[PolygonRing]
