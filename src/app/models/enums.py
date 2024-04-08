from enum import Enum


class OrientationEnum(Enum):
    LEFT = "Left"
    TOP = "Top"
    RIGHT = "Right"
    BOTTOM = "Bottom"


class ClusteringColorSpace(Enum):
    RGB = "RGB"
    HSL = "HSL"
    LAB = "LAB"
