from app.models import dataclasses, enums

COLOR_SPACE_MAPPING = {
    "RGB": enums.ClusteringColorSpace.RGB,
    "HSL": enums.ClusteringColorSpace.HSL,
    "LAB": enums.ClusteringColorSpace.LAB,
}


def parse_settings(user_input: dataclasses.UserInput) -> dataclasses.Settings:
    settings = dataclasses.Settings()

    settings.k_means_clustering_color_space = COLOR_SPACE_MAPPING.get(
        user_input.color_space, enums.ClusteringColorSpace.RGB
    )

    settings.remove_facets_from_large_to_small = (
        user_input.facet_removal_largest_to_smallest
    )

    settings.random_seed = user_input.random_seed
    settings.k_means_nr_of_clusters = user_input.nr_of_clusters
    settings.k_means_min_delta_difference = user_input.cluster_precision

    settings.remove_facets_smaller_than_nr_of_points = (
        user_input.remove_facets_smaller_than
    )
    settings.maximum_number_of_facets = user_input.maximum_number_of_facets

    settings.nr_of_times_to_halve_border_segments = (
        user_input.nr_of_times_to_halve_border_segments
    )

    settings.narrow_pixel_strip_cleanup_runs = (
        user_input.narrow_pixel_strip_cleanup_runs
    )

    settings.resize_image_if_too_large = user_input.resize_image
    settings.resize_image_width = user_input.resize_width
    settings.resize_image_height = user_input.resize_height

    # Parsing kMeansColorRestrictions, assuming newline-separated RGB values in a single string
    for line in user_input.k_means_color_restrictions.split("\n"):
        rgb_parts = [int(part) for part in line.split(",") if part.isdigit()]
        if len(rgb_parts) == 3:
            settings.k_means_color_restrictions.append(tuple(rgb_parts))

    return settings
