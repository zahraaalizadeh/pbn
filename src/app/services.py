import dataclasses
from enum import Enum


class ClusteringColorSpace(Enum):
    RGB = "RGB"
    HSL = "HSL"
    LAB = "LAB"


@dataclasses.dataclass
class Settings:
    def __init__(self):
        self.kMeans_clustering_color_space = ClusteringColorSpace.RGB
        self.remove_facets_from_large_to_small = True
        self.kMeans_nr_of_clusters = 16
        self.kMeans_min_delta_difference = 1
        self.remove_facets_smaller_than_nr_of_points = 20
        self.nr_of_times_to_halve_border_segments = 2

        self.resize_image_if_too_large = True
        self.resize_image_width = 1024
        self.resize_image_height = 1024


def parse_settings(
    *,
    opt_color_space: ClusteringColorSpace,
    opt_facet_removal: bool,
    nr_of_clusters: int,
    cluster_precision: float,
    remove_facets_smaller_than_nr_of_points: int,
    resize_image_if_too_large: bool,
    resize_image_width: int,
    resize_image_height: int,
    nr_of_times_to_halve_border_segments: int,
):
    settings = Settings()

    # Parse simulated user input values
    settings.kMeans_clustering_color_space = opt_color_space
    settings.remove_facets_from_large_to_small = opt_facet_removal
    settings.kMeans_nr_of_clusters = nr_of_clusters
    settings.kMeans_min_delta_difference = cluster_precision
    settings.remove_facets_smaller_than_nr_of_points = (
        remove_facets_smaller_than_nr_of_points
    )
    settings.nr_of_times_to_halve_border_segments = nr_of_times_to_halve_border_segments
    settings.resize_image_if_too_large = resize_image_if_too_large
    settings.resize_image_width = resize_image_width
    settings.resize_image_height = resize_image_height

    return settings
