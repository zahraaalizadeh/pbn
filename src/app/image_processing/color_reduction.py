from dataclasses import dataclass, field

from app.models import dataclasses
from app.utils import arrays


@dataclass
class ColorMapResult:
    img_color_indices: arrays.Array2D = field(
        default_factory=lambda: arrays.Array2D(1, 1)
    )
    colors_by_index: list[dataclasses.RGB] = field(default_factory=list)
    width: int = 0
    height: int = 0
