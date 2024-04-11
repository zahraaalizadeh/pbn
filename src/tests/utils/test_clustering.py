import math

import pytest

from app.utils import clustering


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
