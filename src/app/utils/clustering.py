import math
from dataclasses import dataclass, field
from typing import Any


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
