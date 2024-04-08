class Array2D:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        # Initialize a 2D list (array) filled with zeros
        self.array = [[0 for _ in range(width)] for _ in range(height)]

    def get(self, x: int, y: int) -> int:
        return self.array[y][x]

    def set(self, x: int, y: int, value: int):
        self.array[y][x] = value

    def match_all_around(self, x: int, y: int, value: int) -> bool:
        return (
            (x - 1 >= 0 and self.array[y][x - 1] == value)
            and (y - 1 >= 0 and self.array[y - 1][x] == value)
            and (x + 1 < self.width and self.array[y][x + 1] == value)
            and (y + 1 < self.height and self.array[y + 1][x] == value)
        )
