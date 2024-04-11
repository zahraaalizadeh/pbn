from app.data_structures import random


class TestRandom:
    def test_random_range(self):
        rnd = random.Random()
        results = [rnd.next() for _ in range(1000)]
        assert all(
            0 <= num < 1 for num in results
        ), "All random numbers should be between 0 and 1"

    def test_random_consistency(self):
        seed = 12345
        rnd1 = random.Random(seed)
        rnd2 = random.Random(seed)
        results1 = [rnd1.next() for _ in range(10)]
        results2 = [rnd2.next() for _ in range(10)]
        assert (
            results1 == results2
        ), "Random numbers should be consistent for the same seed"
