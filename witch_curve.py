from copy import deepcopy

import numpy as np

from circle import Circle


class WitchCurve:
    base_circle = None
    points = None

    def __init__(self, circle: Circle, n=5 * 2, r_scale=2):
        self.base_circle = deepcopy(circle)
        self.points = self._generate_points(n, r_scale)

    def y(self, x):
        a = 2 * self.base_circle.radius
        return pow(a, 3) / (pow(a, 2) + pow(x, 2))

    def _generate_range_x(self, n: int, r_scale: float or int):
        right_end = self.base_circle.radius * r_scale
        x_range = np.linspace(0, right_end, n)
        return [*[-x for x in x_range[:0:-1]], *x_range]

    def _generate_points(self, n, r_scale):
        X = self._generate_range_x(n, r_scale)
        return [(x + self.base_circle.centre[0],
                 self.y(x) + self.base_circle.centre[1] - self.base_circle.radius)
                for x in X]
