import math

import pytest
from app.utils import clustering
from app.utils.random import Random


class TestVector:
    def test_vector_creation(self):
        v = clustering.Vector([1, 2, 3])
        assert v.values == [1, 2, 3]
        assert v.weight == 1.0, "Default weight should be 1.0"

    def test_distance_to(self):
        v1 = clustering.Vector([1, 2, 3])
        v2 = clustering.Vector([4, 5, 6])
        # Distance calculation should be correct
        assert v1.distance_to(v2) == pytest.approx(
            math.sqrt(27)
        ), "Distance calculation is incorrect"

    def test_distance_to_with_different_weights_ignored(self):
        v1 = clustering.Vector([1, 2, 3], weight=2)
        v2 = clustering.Vector([1, 2, 3], weight=3)
        # Weights are irrelevant for distance calculation
        assert (
            v1.distance_to(v2) == 0
        ), "Distance should be zero for identical vectors, regardless of weight"

    def test_average_single_vector(self):
        v = clustering.Vector([1, 2, 3], weight=2)
        avg = clustering.Vector.average([v])
        assert avg.values == [
            1,
            2,
            3,
        ], "Average of a single vector should be the vector itself"
        assert avg.weight == 1.0, "Weight of the average vector should be reset to 1.0"

    def test_average_multiple_vectors(self):
        v1 = clustering.Vector([2, 4, 6], weight=2)
        v2 = clustering.Vector([4, 6, 8], weight=1)
        avg = clustering.Vector.average([v1, v2])
        expected_values = [
            (2 * 2 + 4 * 1) / 3,
            (4 * 2 + 6 * 1) / 3,
            (6 * 2 + 8 * 1) / 3,
        ]  # Weighted average
        assert avg.values == pytest.approx(
            expected_values
        ), "Averaged values are incorrect"

    def test_average_zero_elements(self):
        with pytest.raises(ValueError):
            clustering.Vector.average(
                []
            )  # Averaging zero vectors should raise an error

    def test_vector_mismatched_dimensions(self):
        v1 = clustering.Vector([1, 2, 3])
        v2 = clustering.Vector([4, 5])
        with pytest.raises(ValueError):
            v1.distance_to(v2)  # Dimension mismatch should raise an error


class TestKMeans:
    @pytest.fixture
    def image_colors(self):
        # This fixture simulates an image with 3 unique colors and various frequencies
        colors = [
            ([255, 0, 0], 50),  # Red color appears 50 times
            ([0, 255, 0], 30),  # Green color appears 30 times
            ([0, 0, 255], 20),  # Blue color appears 20 times
        ]
        vectors = [
            clustering.Vector(color, weight=frequency) for color, frequency in colors
        ]
        return vectors

    def test_initialization_with_image_colors(self, image_colors):
        random = Random(42)
        kmeans = clustering.KMeans(points=image_colors, k=2, random=random)
        assert len(kmeans.centroids) == 2, "Should initialize two centroids"
        assert (
            sum(len(cat) for cat in kmeans.points_per_category) == 0
        ), "Categories should initially be empty"

    def test_convergence_based_on_delta_distance(self, image_colors):
        random = Random(42)
        kmeans = clustering.KMeans(points=image_colors, k=2, random=random)
        iterations = 0
        # Ensure the loop runs at least once regardless of the initial delta distance
        kmeans.step()
        while kmeans.current_delta_distance_difference > 0.01 and iterations < 100:
            kmeans.step()
            iterations += 1
        assert iterations < 100, "KMeans did not converge within 100 iterations"
        assert all(
            len(cat) > 0 for cat in kmeans.points_per_category
        ), "All categories should have at least one point"

    def test_color_space_impact_on_clustering(self, image_colors):
        random = Random(42)
        kmeans_rgb = clustering.KMeans(points=image_colors, k=2, random=random)
        # Simulate converting RGB to a hypothetical color space, changing the color values
        altered_colors = [
            clustering.Vector([v * 1.1 for v in vec.values], weight=vec.weight)
            for vec in image_colors
        ]
        kmeans_altered = clustering.KMeans(points=altered_colors, k=2, random=random)

        kmeans_rgb.step()
        kmeans_altered.step()

        assert (
            kmeans_rgb.centroids != kmeans_altered.centroids
        ), "Centroids should differ with altered color spaces"

    def test_weight_effectiveness(self, image_colors):
        random = Random(42)
        # Increase the weight of one color disproportionately
        image_colors[0] = clustering.Vector(
            [255, 0, 0], weight=500
        )  # Red color weight boosted
        kmeans = clustering.KMeans(points=image_colors, k=2, random=random)
        kmeans.step()  # Perform one step

        # Determine which centroid is closest to the original heavy red vector
        red_vector = image_colors[0]
        distances = [red_vector.distance_to(centroid) for centroid in kmeans.centroids]
        red_cluster_index = distances.index(
            min(distances)
        )  # Index of the closest centroid to the red vector

        red_cluster_weight = sum(
            vec.weight for vec in kmeans.points_per_category[red_cluster_index]
        )
        total_weight = sum(vec.weight for vec in image_colors)

        # Check if the heavily weighted red color dominates its cluster
        assert (
            red_cluster_weight / total_weight > 0.8
        ), "Red color should dominate its cluster due to high weight"
