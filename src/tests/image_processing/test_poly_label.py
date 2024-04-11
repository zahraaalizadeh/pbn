from app.image_processing import poly_label
from app.models import dataclasses


def test_get_seg_dist_sq():
    a = dataclasses.Point(0, 0)
    b = dataclasses.Point(4, 0)
    px, py = (2, 2)
    assert (
        poly_label.get_seg_dist_sq(px, py, a, b) == 4
    ), "Should return 4 because the perpendicular distance is 2, and 2^2 = 4"
    px, py = (5, 0)
    assert (
        poly_label.get_seg_dist_sq(px, py, a, b) == 1
    ), "Should return 1 because the closest point is (4,0) and distance is 1"
