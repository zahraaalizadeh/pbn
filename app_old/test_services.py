import unittest

from src.app_old import services


class TestParseSettings(unittest.TestCase):
    def test_happy_path(self):
        # Simulated user input values
        opt_color_space = services.ClusteringColorSpace.LAB
        opt_facet_removal = False
        nr_of_clusters = 5
        cluster_precision = 0.1
        remove_facets_smaller_than_nr_of_points = 20
        resize_image_if_too_large = False
        resize_image_width = 512
        resize_image_height = 512
        nr_of_times_to_halve_border_segments = 4

        settings = services.parse_settings(
            opt_color_space=opt_color_space,
            opt_facet_removal=opt_facet_removal,
            nr_of_clusters=nr_of_clusters,
            cluster_precision=cluster_precision,
            remove_facets_smaller_than_nr_of_points=remove_facets_smaller_than_nr_of_points,
            resize_image_if_too_large=resize_image_if_too_large,
            resize_image_width=resize_image_width,
            resize_image_height=resize_image_height,
            nr_of_times_to_halve_border_segments=nr_of_times_to_halve_border_segments,
        )

        # Assert the expected output
        self.assertEqual(settings.kMeans_clustering_color_space, opt_color_space)
        self.assertEqual(settings.remove_facets_from_large_to_small, opt_facet_removal)
        self.assertEqual(settings.kMeans_nr_of_clusters, nr_of_clusters)
        self.assertEqual(settings.kMeans_min_delta_difference, cluster_precision)
        self.assertEqual(
            settings.remove_facets_smaller_than_nr_of_points,
            remove_facets_smaller_than_nr_of_points,
        )
        self.assertEqual(settings.resize_image_if_too_large, resize_image_if_too_large)
        self.assertEqual(settings.resize_image_width, resize_image_width)
        self.assertEqual(settings.resize_image_height, resize_image_height)
        self.assertEqual(
            settings.nr_of_times_to_halve_border_segments,
            nr_of_times_to_halve_border_segments,
        )


if __name__ == "__main__":
    unittest.main()
