import asyncio
import dataclasses
import logging
import traceback

from PIL import Image

from . import enums


@dataclasses.dataclass
class Settings:
    def __init__(self):
        self.kMeans_clustering_color_space = enums.ClusteringColorSpace.RGB
        self.remove_facets_from_large_to_small = True
        self.kMeans_nr_of_clusters = 16
        self.kMeans_min_delta_difference = 1
        self.remove_facets_smaller_than_nr_of_points = 20
        self.nr_of_times_to_halve_border_segments = 2

        self.resize_image_if_too_large = True
        self.resize_image_width = 1024
        self.resize_image_height = 1024


@dataclasses.dataclass
class ProcessResult:
    facet_result = None
    colors_by_index = None


def parse_settings(
    *,
    opt_color_space: enums.ClusteringColorSpace,
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


async def process(settings, cancellation_token):
    # This is a placeholder for loading and manipulating the image, which in a Python context,
    # would not be directly from an HTMLCanvasElement, but rather loaded from a file or similar.
    img = Image.open("path_to_image")
    width, height = img.size

    if settings["resizeImageIfTooLarge"] and (
        width > settings["resizeImageWidth"] or height > settings["resizeImageHeight"]
    ):
        if width > settings["resizeImageWidth"]:
            newWidth = settings["resizeImageWidth"]
            newHeight = int(height / width * newWidth)
            width, height = newWidth, newHeight
        if height > settings["resizeImageHeight"]:
            newHeight = settings["resizeImageHeight"]
            newWidth = int(width / height * newHeight)
            width, height = newWidth, newHeight

        img = img.resize((width, height), Image.ANTIALIAS)

    # Reset progress and other operations that would typically manipulate the DOM
    # in the TypeScript version would need to be handled differently in Python,
    # possibly through a web framework if this is part of a web application.

    # The following operations would need to be defined in your Python context,
    # as they involve complex operations like k-means clustering, color reduction, etc.
    # These are placeholders to suggest how you might structure the async calls.
    kmeansImgData = await process_kmeans_clustering(img, settings, cancellation_token)
    colormapResult = create_color_map(kmeansImgData)
    facet_result = await process_facet_building(img, colormapResult, cancellation_token)

    # Continuing with the other processing steps similarly...

    processResult = ProcessResult()
    processResult.facet_result = facet_result
    # Assuming colormapResult has a property `colors_by_index`
    processResult.colors_by_index = colormapResult.colors_by_index
    return processResult


# Placeholder for the async operations mentioned in the pseudo code.
async def process_kmeans_clustering(img, settings, cancellation_token):
    # Implementation of k-means clustering on the image data.
    pass


def create_color_map(kmeansImgData):
    # Implementation of color map creation based on k-means clustering result.
    pass


async def process_facet_building(img, colormapResult, cancellation_token):
    # Implementation of facet building from the image data and color map.
    pass


async def process():
    try:
        settings = parse_settings()

        process_result = await GUIProcessManager.process(settings, cancellationToken)
        await update_output()
        # Assuming M.Tabs is a class or object
        tabs_output = M.Tabs.get_instance(document.getElementById("tabsOutput"))
        tabs_output.select("output-pane")
    except Exception as e:
        logging.error("Error: %s at %s", e, traceback.format_exc())
