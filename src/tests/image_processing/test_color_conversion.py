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


@pytest.mark.parametrize(
    "lab, expected_rgb",
    [
        (dataclasses.LAB(0, 0, 0), [0, 0, 0]),  # Black
        (dataclasses.LAB(100, 0, 0), [255, 255, 255]),  # White
        (dataclasses.LAB(53.232881, 80.109309, 67.220068), [255, 0, 0]),  # Red
        (dataclasses.LAB(87.737033, -86.184636, 83.181164), [0, 255, 0]),  # Green
        (dataclasses.LAB(32.302586, 79.196661, -107.863681), [0, 0, 255]),  # Blue
    ],
)
def test_lab2rgb_conversion(lab, expected_rgb):
    rgb = color_conversion.lab2rgb(lab)
    # Assert each RGB component is within a margin of error
    assert all(
        abs(c - e) <= 1 for c, e in zip(rgb, expected_rgb)
    ), f"dataclasses.LAB {lab} should convert to RGB close to {expected_rgb}, got {rgb}"


@pytest.mark.parametrize(
    "hsl,expected_rgb",
    [
        (dataclasses.HSL(0, 0, 0), [0, 0, 0]),  # Black
        (dataclasses.HSL(0, 0, 1), [255, 255, 255]),  # White
        (dataclasses.HSL(0, 1, 0.5), [255, 0, 0]),  # Red
        (dataclasses.HSL(1 / 3, 1, 0.5), [0, 255, 0]),  # Green
        (dataclasses.HSL(2 / 3, 1, 0.5), [0, 0, 255]),  # Blue
        (dataclasses.HSL(0, 0, 0.5), [128, 128, 128]),  # Gray
    ],
)
def test_hsl_to_rgb(hsl, expected_rgb):
    rgb = color_conversion.hsl_to_rgb(hsl)
    # Allowing a small margin of error, e.g., 1 unit in the RGB space
    assert all(
        abs(a - b) <= 1 for a, b in zip(rgb, expected_rgb)
    ), f"HSL {hsl} should convert to RGB close to {expected_rgb}, got {rgb}"


@pytest.mark.parametrize(
    "rgb,expected_hsl",
    [
        (dataclasses.RGB(0, 0, 0), (0, 0, 0)),  # Black
        (dataclasses.RGB(255, 255, 255), (0, 0, 1)),  # White
        (dataclasses.RGB(255, 0, 0), (0, 1, 0.5)),  # Red
        (dataclasses.RGB(0, 255, 0), (1 / 3, 1, 0.5)),  # Green
        (dataclasses.RGB(0, 0, 255), (2 / 3, 1, 0.5)),  # Blue
    ],
)
def test_rgb_to_hsl(rgb, expected_hsl):
    assert color_conversion.rgb_to_hsl(rgb) == pytest.approx(
        expected_hsl
    ), f"RGB {rgb} should convert to HSL {expected_hsl}"
