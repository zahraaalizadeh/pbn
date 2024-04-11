from app.image_processing import color_reduction
from app.models import dataclasses
from app.utils import data_structs


class TestColorMapResult:
    def test_colormap_initialization(self):
        result = color_reduction.ColorMapResult()
        assert isinstance(
            result.img_color_indices, data_structs.Array2D
        ), "img_color_indices should be an instance of Array2D"
        assert isinstance(
            result.colors_by_index, list
        ), "colors_by_index should be a list"
        assert (
            result.width == 0 and result.height == 0
        ), "Width and height should initialize to 0"

    def test_colormap_with_parameters(self):
        width, height = 10, 20
        colors = [dataclasses.RGB(255, 0, 0), dataclasses.RGB(0, 255, 0)]
        img_indices = data_structs.Array2D(width, height)
        img_indices.set(
            0, 0, 1
        )  # Set the first element to point to the second color (index 1)

        result = color_reduction.ColorMapResult(
            img_color_indices=img_indices,
            colors_by_index=colors,
            width=width,
            height=height,
        )
        assert (
            result.img_color_indices.get(0, 0) == 1
        ), "The color index should be set correctly"
        assert result.colors_by_index[0] == dataclasses.RGB(
            255, 0, 0
        ), "The first color should be dataclasses.RGB(255, 0, 0)"
        assert result.colors_by_index[1] == dataclasses.RGB(
            0, 255, 0
        ), "The second color should be dataclasses.RGB(0, 255, 0)"
        assert (
            result.width == width and result.height == height
        ), "Width and height should be set correctly"
