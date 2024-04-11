from dataclasses import dataclass, field

from app.models import dataclasses
from app.utils import data_structs


@dataclass
class ColorMapResult:
    img_color_indices: data_structs.Array2D = field(
        default_factory=lambda: data_structs.Array2D(1, 1)
    )
    colors_by_index: list[dataclasses.RGB] = field(default_factory=list)
    width: int = 0
    height: int = 0
