from math import sqrt

import numpy as np
import pylab


class Circle:
    centre = None
    R = None
    points = None

    def __init__(self, centre, r):  # centre == (xo, yo)  r == integer
        self.centre = centre
        self.R = r

    def y(self, x):  # уравнение окружности в виде у(х)
        s = sqrt(pow(self.R, 2) - pow(x - self.centre[0], 2))
        return s + self.centre[1], -s + self.centre[1]

    def generate_points(self, n: int, additional_points_number: int = 5):
        # Итоговое количество точек равно
        # (n-1) * 4 + additional_points_number * 4

        # TODO: обработка случаев при n<2?
        assert n >= 2, f"Неверное количетво точек для построения! ({n} < 2)"
        assert additional_points_number >= 0, f"Неверное число дополнительных точек: {additional_points_number}"
        self.points = []

        origin_X = np.linspace(self.centre[0], self.centre[0] + self.R, n)
        mini_X = np.linspace(origin_X[-2], origin_X[-1], additional_points_number + 2)[1:-1]
        X = [*origin_X, *mini_X]
        for x in X:
            val_y = self.y(x)  # (+, -)
            self.points.extend({
                *[(x, y) for y in val_y],
                *[(-x, y) for y in val_y]
            })
        return self

    def prepare_points(self):
        sorted_points = sorted(self.points)
        positive_y, negative_y, zero_y = [], [], []
        for point in sorted_points:
            if point[1] > 0:
                positive_y.append(point)
            elif point[1] < 0:
                negative_y.append(point)
            else:
                zero_y.append(point)

        ordered_points = [zero_y[0], *positive_y, zero_y[1], *negative_y[::-1]]
        unpacked_points = {'x': [], 'y': []}
        for point in [*ordered_points, ordered_points[0]]:  # необходимо замкнуть контур
            unpacked_points['x'].append(point[0])
            unpacked_points['y'].append(point[1])
        return {'ordered': ordered_points, 'unpacked': unpacked_points}


n_points = 12
# TODO:
#   поправить реализацию окружности, чтобы можно было ставить центр в других четверятях кроме 1
circle = Circle((0, 0), 2).generate_points(n_points)
tmp_points = circle.prepare_points()

pylab.figure('Circle')
pylab.axis('equal')
pylab.grid()
pylab.xlabel('x')
pylab.ylabel('y(x)')
pylab.title(f'Circle ({len(circle.points)} points)')
pylab.plot(tmp_points['unpacked']['x'], tmp_points['unpacked']['y'])
for point in tmp_points['ordered']:
    pylab.scatter(*point, marker='o', c='r')

pylab.show()
