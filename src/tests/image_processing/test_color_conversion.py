import pytest

from app.image_processing import color_conversion
from app.models import dataclasses


# Example test cases
@pytest.mark.parametrize(
    "rgb, expected_lab",
    [
        (dataclasses.RGB(0, 0, 0), [0, 0, 0]),  # Black
        (dataclasses.RGB(255, 255, 255), [100, 0, 0]),  # White
        (
            dataclasses.RGB(255, 0, 0),
            [53.23288178584245, 80.10930952982204, 67.22006831026425],
        ),  # Red
        (
            dataclasses.RGB(0, 255, 0),
            [87.73703347354422, -86.18463649762525, 83.18116474777854],
        ),  # Green
        (
            dataclasses.RGB(0, 0, 255),
            [32.302586667249486, 79.19666178930935, -107.86368104495168],
        ),  # Blue
    ],
)
def test_rgb2lab(rgb, expected_lab):
    lab = color_conversion.rgb2lab(rgb)
    # Allowing a small margin of error due to potential floating-point arithmetic variations
    assert all(
        abs(a - b) < 0.02 for a, b in zip(lab, expected_lab)
    ), f"Expected {expected_lab}, got {lab}"
