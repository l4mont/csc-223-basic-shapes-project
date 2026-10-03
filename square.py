"""Define Square using Rectangle's area behavior and synchronized dimensions."""

from rectangle import Rectangle


class Square(Rectangle):
    """Keep side, length, and width equal after every successful public assignment."""

    def __init__(self, side, name="Square"):
        """Pass equal dimensions to Rectangle; overridden setters synchronize them."""
        super().__init__(side, side, name)

    @property
    def side(self):
        """Positive finite real side; changes synchronize all dimensions and area.

        Wrong types raise TypeError; nonpositive/nonfinite values raise ValueError.
        Rejected values leave the previous valid state unchanged.
        """
        return self._side

    @side.setter
    def side(self, value):
        """Validate first, then update all dimensions before calculating area."""
        value = self._validate_number(value, "side", positive=True)
        self._side = self._length = self._width = value
        self.calc_area()

    @property
    def length(self):
        """Alias for side; assignment has side's validation and updates all dimensions."""
        return self._length

    @length.setter
    def length(self, value):
        """Route inherited length assignments through the invariant-preserving setter."""
        self.side = value

    @property
    def width(self):
        """Alias for side; assignment has side's validation and updates all dimensions."""
        return self._width

    @width.setter
    def width(self, value):
        """Route inherited width assignments through the invariant-preserving setter."""
        self.side = value

