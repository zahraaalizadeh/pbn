from app.image_processing import utilities
from app.models import dataclasses, enums


class TestParseSettings:
    def test_parse_settings_default_values(self):
        user_input = dataclasses.UserInput()  # Default values
        settings = utilities.parse_settings(user_input)

        assert settings.k_means_clustering_color_space == enums.ClusteringColorSpace.RGB
        assert settings.remove_facets_from_large_to_small is True
        assert settings.random_seed == 0
        assert settings.k_means_nr_of_clusters == 16
        assert settings.k_means_min_delta_difference == 1
        assert settings.k_means_color_restrictions == []
        assert settings.color_aliases == {}
        assert settings.narrow_pixel_strip_cleanup_runs == 3
        assert settings.remove_facets_smaller_than_nr_of_points == 20
        assert settings.maximum_number_of_facets == 2**31 - 1
        assert settings.nr_of_times_to_halve_border_segments == 2
        assert settings.resize_image_if_too_large is True
        assert settings.resize_image_width == 1024
        assert settings.resize_image_height == 1024

    def test_parse_settings_custom_values(self):
        user_input = dataclasses.UserInput(
            color_space="HSL",
            facet_removal_largest_to_smallest=False,
            resize_image=False,
            random_seed=42,
            nr_of_clusters=10,
            cluster_precision=0.5,
            resize_height=512,
            resize_width=512,
            maximum_number_of_facets=1000,
            nr_of_times_to_halve_border_segments=4,
            k_means_color_restrictions="255,0,0\n0,255,0\n0,0,255",
            remove_facets_smaller_than=50,
            narrow_pixel_strip_cleanup_runs=10,
        )
        settings = utilities.parse_settings(user_input)

        assert settings.k_means_clustering_color_space == enums.ClusteringColorSpace.HSL
        assert settings.remove_facets_from_large_to_small is False
        assert settings.random_seed == 42
        assert settings.k_means_nr_of_clusters == 10
        assert settings.k_means_min_delta_difference == 0.5
        assert settings.color_aliases == {}
        assert settings.narrow_pixel_strip_cleanup_runs == 10
        assert settings.remove_facets_smaller_than_nr_of_points == 50
        assert settings.maximum_number_of_facets == 1000
        assert settings.nr_of_times_to_halve_border_segments == 4
        assert settings.resize_image_if_too_large is False
        assert settings.resize_image_width == 512
        assert settings.resize_image_height == 512
        assert (255, 0, 0) in settings.k_means_color_restrictions

    def test_parse_settings_with_invalid_input(self):
        user_input = dataclasses.UserInput(color_space="XYZ")  # Invalid color space
        settings = utilities.parse_settings(user_input)

        # Assuming the default behavior for invalid input is to revert to default values
        assert settings.k_means_clustering_color_space == enums.ClusteringColorSpace.RGB
