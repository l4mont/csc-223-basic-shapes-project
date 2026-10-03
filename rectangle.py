"""Define Rectangle with validated dimensions and automatic area updates."""

from basic_shape import BasicShape


class Rectangle(BasicShape):
    """Represent a rectangle with positive finite real length and width."""

    def __init__(self, length, width, name="Rectangle"):
        """Initialize the base class and set dimensions through public properties."""
        super().__init__(name)
        self.length = length
        self.width = width

    @property
    def length(self):
        """Positive finite real length; changes update area once width exists.

        Wrong types raise TypeError; nonpositive/nonfinite values raise ValueError.
        """
        return self._length

    @length.setter
    def length(self, value):
        """Validate length before assignment, then update area when initialized."""
        self._length = self._validate_number(value, "length", positive=True)
        # The first constructor assignment happens before width exists.
        if hasattr(self, "_width"):
            self.calc_area()

    @property
    def width(self):
        """Positive finite real width; changes update area once length exists.

        Wrong types raise TypeError; nonpositive/nonfinite values raise ValueError.
        """
        return self._width

    @width.setter
    def width(self, value):
        """Validate width before assignment, then update area when initialized."""
        self._width = self._validate_number(value, "width", positive=True)
        if hasattr(self, "_length"):
            self.calc_area()

    def calc_area(self):
        """Store current length times width; Square inherits this implementation."""
        self._area = self._length * self._width

