from dataclasses import dataclass, field
from datetime import datetime

from app.models import enums


@dataclass
class Settings:
    k_means_nr_of_clusters: int = 16
    k_means_min_delta_difference: int = 1
    k_means_clustering_color_space: enums.ClusteringColorSpace = enums.ClusteringColorSpace.RGB

    # Assuming RGB is a tuple of three integers for simplicity
    k_means_color_restrictions: list[tuple | str] = field(default_factory=list)

    # This assumes a simple RGB structure; adjust as needed
    color_aliases: dict[str, tuple] = field(default_factory=dict)

    narrow_pixel_strip_cleanup_runs: int = 3
    remove_facets_smaller_than_nr_of_points: int = 20
    remove_facets_from_large_to_small: bool = True
    maximum_number_of_facets: int = float('inf')

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
