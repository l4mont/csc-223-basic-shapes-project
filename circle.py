"""Define Circle as a concrete implementation of BasicShape."""

from math import pi

from basic_shape import BasicShape


class Circle(BasicShape):
    """Represent a circle with finite real coordinates and a positive radius."""

    def __init__(self, x_center, y_center, radius, name="Circle"):
        """Initialize the inherited name, validated coordinates, radius, and area."""
        super().__init__(name)
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius

    @property
    def x_center(self):
        """Finite real x coordinate; TypeError for wrong types, ValueError if nonfinite."""
        return self._x_center

    @x_center.setter
    def x_center(self, value):
        """Validate x before assignment; moving the center does not change area."""
        self._x_center = self._validate_number(value, "x_center")

    @property
    def y_center(self):
        """Finite real y coordinate; TypeError for wrong types, ValueError if nonfinite."""
        return self._y_center

    @y_center.setter
    def y_center(self, value):
        """Validate y before assignment; moving the center does not change area."""
        self._y_center = self._validate_number(value, "y_center")

    @property
    def radius(self):
        """Positive finite real radius; changes recalculate area automatically.

        Wrong types raise TypeError; nonpositive/nonfinite values raise ValueError.
        Values whose area overflows or underflows also raise ValueError.
        """
        return self._radius

    @radius.setter
    def radius(self, value):
        """Validate and store the radius before invoking the area calculation."""
        value = self._validate_number(value, "radius", positive=True)
        # Check the prospective area before changing an existing valid object.
        self._validate_number(pi * value * value, "area", positive=True)
        self._radius = value
        self.calc_area()

    def calc_area(self):
        """Store pi times the current radius squared as the inherited area."""
        self._area = pi * self._radius * self._radius

