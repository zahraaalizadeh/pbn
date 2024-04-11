from app.utils import arrays


class TestArray2D:
    def test_initialization(self):
        width, height = 10, 15
        array_2d = arrays.Array2D(width, height)
        assert all(
            all(cell == 0 for cell in row) for row in array_2d.array
        ), "All cells should be initialized to 0"

    def test_set_and_get(self):
        array_2d = arrays.Array2D(10, 10)
        test_val = 123
        x, y = 5, 5
        array_2d.set(x, y, test_val)
        assert (
            array_2d.get(x, y) == test_val
        ), f"Cell at ({x}, {y}) should have the value {test_val}"

    def test_match_all_around(self):
        array_2d = arrays.Array2D(3, 3)
        # Set a value in the middle and surrounding cells
        value = 1
        for x in range(3):
            for y in range(3):
                array_2d.set(x, y, value)

        # The middle cell should match all around since all cells have the same value
        assert array_2d.match_all_around(
            1, 1, value
        ), "Middle cell should match all surrounding cells"

    def test_match_all_around_edge_case(self):
        array_2d = arrays.Array2D(3, 3)
        # Set only the middle cell
        array_2d.set(1, 1, 1)
        # Expect match_all_around to return False since not all surrounding cells are set to the same value
        assert not array_2d.match_all_around(
            1, 1, 1
        ), "Middle cell should not match all surrounding cells when they are different"
