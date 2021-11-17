import matplotlib.pyplot as plt

from circle import Circle
from witch_curve import WitchCurve

base_circle = Circle((1, 2), 3)
curve = WitchCurve(base_circle, 50, 10)

zipped_points = list(zip(*curve.points))

plt.figure(num='The Witch Curve')
plt.grid()

c = plt.Circle(base_circle.centre, base_circle.radius, fill=False, color='blue')
plt.gca().add_artist(c)

plt.scatter(*zipped_points, c='red', edgecolors='black')
plt.plot(*zipped_points, c='black')

plt.title(f'{len(curve.points)} point(-s)')
plt.show()
