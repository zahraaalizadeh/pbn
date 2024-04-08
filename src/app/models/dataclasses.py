from dataclasses import dataclass, field
from datetime import datetime

from app.models import enums


@dataclass
class UserInput:
    color_space: str = "RGB"
    facet_removal_largest_to_smallest: bool = True
    random_seed: int = 0
    nr_of_clusters: int = 16
    cluster_precision: float = 1.0
    remove_facets_smaller_than: int = 20
    maximum_number_of_facets: int = 2**31 - 1
    nr_of_times_to_halve_border_segments: int = 2
    narrow_pixel_strip_cleanup_runs: int = 3
    resize_image: bool = True
    resize_width: int = 1024
    resize_height: int = 1024
    k_means_color_restrictions: str = ""


@dataclass
class Settings:
    k_means_nr_of_clusters: int = 16
    k_means_min_delta_difference: int = 1
    k_means_clustering_color_space: enums.ClusteringColorSpace = (
        enums.ClusteringColorSpace.RGB
    )

    # Assuming RGB is a tuple of three integers for simplicity
    k_means_color_restrictions: list[tuple | str] = field(default_factory=list)

    # This assumes a simple RGB structure; adjust as needed
    color_aliases: dict[str, tuple] = field(default_factory=dict)

    narrow_pixel_strip_cleanup_runs: int = 3
    remove_facets_smaller_than_nr_of_points: int = 20
    remove_facets_from_large_to_small: bool = True
    maximum_number_of_facets: int = 2**31 - 1

    nr_of_times_to_halve_border_segments: int = 2

    resize_image_if_too_large: bool = True
    resize_image_width: int = 1024
    resize_image_height: int = 1024

    random_seed: int = field(default_factory=lambda: int(datetime.now().timestamp()))


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


@dataclass
class PathPoint(Point):
    """
    This is a point with an orientation that indicates which wall border is set
    """

    orientation: enums.OrientationEnum

    def get_wall_x(self) -> float:
        x = self.x
        if self.orientation == enums.OrientationEnum.LEFT:
            x -= 0.5
        elif self.orientation == enums.OrientationEnum.RIGHT:
            x += 0.5
        return x

    def get_wall_y(self) -> float:
        y = self.y
        if self.orientation == enums.OrientationEnum.TOP:
            y -= 0.5
        elif self.orientation == enums.OrientationEnum.BOTTOM:
            y += 0.5
        return y

    def get_neighbour(self, facet_result) -> int:
        pass

    def __str__(self):
        return f"{self.x},{self.y} {self.orientation.value}"


@dataclass
class RGB:
    r: int
    g: int
    b: int


@dataclass
class LAB:
    L: float
    a: float
    b: float
