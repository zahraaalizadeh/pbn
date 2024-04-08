from app.models import dataclasses


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
        assert point_result1 is not point_result2  # Ensure they are two distinct objects
