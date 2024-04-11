import math
import time


class Random:
    def __init__(self, seed=None):
        self.seed = seed if seed is not None else int(time.time())

    def next(self):
        self.seed += 1
        x = math.sin(self.seed) * 10000
        return x - math.floor(x)
