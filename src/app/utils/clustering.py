import math
from dataclasses import dataclass, field
from typing import Any

from app.utils.random import Random


@dataclass
class Vector:
    values: list[float]
    weight: float = 1.0
    tag: Any = field(default=None)

    def distance_to(self, p: "Vector") -> float:
        if len(self.values) != len(p.values):
            raise ValueError("Vectors must be of the same dimensionality")
        return math.sqrt(sum((pv - sv) ** 2 for pv, sv in zip(p.values, self.values)))

    @staticmethod
    def average(pts: list["Vector"]) -> "Vector":
        """
        Calculates the weighted average of the given points
        """
        if not pts:
            raise ValueError("Can't average 0 elements")

        num_dimensions = len(pts[0].values)
        total_weight = sum(p.weight for p in pts)
        average_values = [0] * num_dimensions

        for p in pts:
            for i in range(num_dimensions):
                average_values[i] += p.weight * p.values[i]

        average_values = [x / total_weight for x in average_values]
        return Vector(average_values)


@dataclass
class KMeans:
    points: list[Vector]
    k: int  # The number of clusters in which the data points are to be divided
    random: Random
    centroids: list[Vector] = field(default_factory=list)
    current_iteration: int = 0
    points_per_category: list[list[Vector]] = field(init=False)
    current_delta_distance_difference: float = 0.0

    def __post_init__(self):
        if not self.centroids:
            self.init_centroids()
        else:
            self._clear_categories()

    def init_centroids(self):
        """
        Selects initial centroids randomly based on the provided Random instance
        """
        chosen_indices = set()
        while len(chosen_indices) < self.k:
            index = int(len(self.points) * self.random.next())
            chosen_indices.add(index)
        self.centroids = [self.points[idx] for idx in chosen_indices]
        self._clear_categories()

    def _clear_categories(self):
        self.points_per_category = [[] for _ in range(self.k)]

    def step(self):
        # Clear categories
        self._clear_categories()

        # Assign points to the nearest centroid
        for p in self.points:
            min_dist = float("inf")
            centroid_index = -1
            for i, centroid in enumerate(self.centroids):
                dist = centroid.distance_to(p)
                if dist < min_dist:
                    min_dist = dist
                    centroid_index = i
            self.points_per_category[centroid_index].append(p)

        # Recalculate centroids and measure change
        total_distance_diff = 0.0
        for i, category in enumerate(self.points_per_category):
            if category:
                new_centroid = Vector.average(category)
                dist = self.centroids[i].distance_to(new_centroid)
                total_distance_diff += dist
                self.centroids[i] = new_centroid

        self.current_delta_distance_difference = total_distance_diff
        self.current_iteration += 1
