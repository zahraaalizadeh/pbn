from app.models import dataclasses, enums


class TestPoint:
    def test_point_initialization(self):
        point = dataclasses.Point(x=10.5, y=-20.3)
        assert point.x == 10.5
        assert point.y == -20.3

    def test_point_equality(self):
        point1 = dataclasses.Point(x=10.5, y=-20.3)
        point2 = dataclasses.Point(x=10.5, y=-20.3)
        assert point1 == point2
        assert point1 is not point2  # Ensure they are two distinct objects

    def test_pointresult_initialization(self):
        point = dataclasses.Point(x=10.5, y=-20.3)
        point_result = dataclasses.PointResult(pt=point, distance=100.2)
        assert point_result.pt == point
        assert point_result.distance == 100.2


class TestPointResult:
    def test_pointresult_equality(self):
        point1 = dataclasses.Point(x=10.5, y=-20.3)
        point_result1 = dataclasses.PointResult(pt=point1, distance=100.2)
        point2 = dataclasses.Point(x=10.5, y=-20.3)
        point_result2 = dataclasses.PointResult(pt=point2, distance=100.2)
        assert point_result1 == point_result2
        assert (
            point_result1 is not point_result2
        )  # Ensure they are two distinct objects


class TestSettings:
    def test_settings_initialization_with_defaults(self):
        settings = dataclasses.Settings()
        assert settings.k_means_nr_of_clusters == 16
        assert settings.k_means_min_delta_difference == 1
        assert settings.k_means_clustering_color_space == enums.ClusteringColorSpace.RGB
        assert settings.k_means_color_restrictions == []
        assert settings.color_aliases == {}
        assert settings.narrow_pixel_strip_cleanup_runs == 3
        assert settings.remove_facets_smaller_than_nr_of_points == 20
        assert settings.remove_facets_from_large_to_small is True
        assert settings.maximum_number_of_facets == float("inf")
        assert settings.nr_of_times_to_halve_border_segments == 2
        assert settings.resize_image_if_too_large is True
        assert settings.resize_image_width == 1024
        assert settings.resize_image_height == 1024
        # No need to assert on random_seed as it's dynamic

    def test_settings_custom_initialization(self):
        custom_settings = dataclasses.Settings(
            k_means_nr_of_clusters=10,
            k_means_min_delta_difference=2,
            k_means_clustering_color_space=enums.ClusteringColorSpace.LAB,
            k_means_color_restrictions=[(255, 255, 255), "exclude"],
            color_aliases={"alias1": (255, 0, 0)},
            narrow_pixel_strip_cleanup_runs=5,
            remove_facets_smaller_than_nr_of_points=15,
            remove_facets_from_large_to_small=False,
            maximum_number_of_facets=1000,
            nr_of_times_to_halve_border_segments=1,
            resize_image_if_too_large=False,
            resize_image_width=800,
            resize_image_height=600,
            random_seed=123456,
        )

        assert custom_settings.k_means_nr_of_clusters == 10
        assert custom_settings.k_means_min_delta_difference == 2
        assert (
            custom_settings.k_means_clustering_color_space
            == enums.ClusteringColorSpace.LAB
        )
        assert custom_settings.k_means_color_restrictions == [
            (255, 255, 255),
            "exclude",
        ]
        assert custom_settings.color_aliases == {"alias1": (255, 0, 0)}
        assert custom_settings.narrow_pixel_strip_cleanup_runs == 5
        assert custom_settings.remove_facets_smaller_than_nr_of_points == 15
        assert custom_settings.remove_facets_from_large_to_small is False
        assert custom_settings.maximum_number_of_facets == 1000
        assert custom_settings.nr_of_times_to_halve_border_segments == 1
        assert custom_settings.resize_image_if_too_large is False
        assert custom_settings.resize_image_width == 800
        assert custom_settings.resize_image_height == 600
        assert custom_settings.random_seed == 123456
