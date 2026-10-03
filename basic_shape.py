"""Define the formal interface and shared validation for geometric shapes."""

from abc import ABC, abstractmethod
from math import isfinite
from numbers import Real


class BasicShape(ABC):
    """Require area calculation while sharing a name and read-only area."""

    def __init__(self, name):
        """Validate a nonblank name and initialize area without subclass data."""
        self.name = name
        self._area = 0.0

    @property
    def name(self):
        """Nonblank string label; invalid types/blank values raise TypeError/ValueError."""
        return self._name

    @name.setter
    def name(self, value):
        """Validate the new label before replacing the existing name."""
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        if not value.strip():
            raise ValueError("name must not be blank")
        self._name = value

    @property
    def area(self):
        """Return the latest calculated area; client assignment is not allowed."""
        return self._area

    @staticmethod
    def _validate_number(value, label, positive=False):
        """Return a finite real float, excluding bool; optionally require positivity."""
        if isinstance(value, bool) or not isinstance(value, Real):
            raise TypeError(f"{label} must be a real number, not bool")
        try:
            number = float(value)
        except OverflowError as exc:
            raise ValueError(f"{label} is too large") from exc
        if not isfinite(number):
            raise ValueError(f"{label} must be finite")
        if positive and number <= 0:
            raise ValueError(f"{label} must be greater than zero")
        return number

    @abstractmethod
    def calc_area(self):
        """Calculate and store area using the concrete shape's current dimensions."""

