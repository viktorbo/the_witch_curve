class Circle:
    centre = None
    radius = None

    def __init__(self, centre: tuple or list, radius: int or float):
        assert radius > 0, f'Wrong radius for {self}'  # If radius <= 0 then it's negative number or single point
        self.centre = centre
        self.radius = radius

    def __str__(self):
        return f"({self.centre}, {self.radius})"
