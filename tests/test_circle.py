"""Verify circle behavior with repeatable unittest cases."""

import unittest
from math import pi
from circle import Circle


class TestCircle(unittest.TestCase):
    """Exercise public behavior and preserve shape invariants."""

    def test_construction(self):
        """Accept negative and zero coordinates and a positive radius."""
        shape = Circle(-2, 0, 4)
        self.assertEqual((shape.x_center, shape.y_center, shape.radius), (-2, 0, 4))
        self.assertAlmostEqual(shape.area, 16 * pi)

    def test_decimal_radius(self):
        """Calculate area correctly for a fractional radius."""
        shape = Circle(1.5, -2.5, 0.5)
        self.assertAlmostEqual(shape.area, pi / 4)

    def test_names(self):
        """Support default and custom names."""
        self.assertEqual(Circle(0, 0, 1).name, "Circle")
        self.assertEqual(Circle(0, 0, 1, "Disk").name, "Disk")

    def test_zero_radius(self):
        """Reject zero radius."""
        with self.assertRaises(ValueError):
            Circle(0, 0, 0)

    def test_negative_radius(self):
        """Reject negative radius."""
        with self.assertRaises(ValueError):
            Circle(0, 0, -1)

    def test_invalid_radius_types(self):
        """Reject strings, None, bool, and complex radius values."""
        for value in ("2", None, True, 2j):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    Circle(0, 0, value)

    def test_nonfinite_radius(self):
        """Reject NaN and infinite radius values."""
        for value in (float("nan"), float("inf"), -float("inf")):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    Circle(0, 0, value)

    def test_radius_recalculation(self):
        """Update cached area automatically after a radius change."""
        shape = Circle(0, 0, 4)
        shape.radius = 8
        self.assertEqual(shape.radius, 8)
        self.assertAlmostEqual(shape.area, 64 * pi)

    def test_coordinate_changes(self):
        """Move the center without changing the area."""
        shape = Circle(0, 0, 4)
        area = shape.area
        shape.x_center = -7
        shape.y_center = 3.5
        self.assertEqual((shape.x_center, shape.y_center), (-7, 3.5))
        self.assertEqual(shape.area, area)

    def test_invalid_coordinates(self):
        """Reject invalid coordinates at construction and assignment."""
        shape = Circle(-2, 3, 4)
        for attr in ("x_center", "y_center"):
            for value, error in (("0", TypeError), (True, TypeError), (None, TypeError), (1j, TypeError), (float("nan"), ValueError), (float("inf"), ValueError)):
                with self.subTest(attr=attr, value=value):
                    before = (shape.x_center, shape.y_center, shape.area)
                    with self.assertRaises(error):
                        setattr(shape, attr, value)
                    self.assertEqual((shape.x_center, shape.y_center, shape.area), before)
                    args = [0, 0, 4]
                    args[0 if attr == "x_center" else 1] = value
                    with self.assertRaises(error):
                        Circle(*args)

    def test_failed_radius_preserves_state(self):
        """Retain radius and area when a new value fails validation."""
        shape = Circle(0, 0, 4)
        for value, error in ((0, ValueError), (-3, ValueError), ("8", TypeError), (True, TypeError), (float("nan"), ValueError)):
            with self.subTest(value=value):
                before = (shape.radius, shape.area)
                with self.assertRaises(error):
                    shape.radius = value
                self.assertEqual((shape.radius, shape.area), before)

    def test_explicit_calc_area(self):
        """Allow recalculation through the formal method."""
        shape = Circle(0, 0, 4)
        shape.calc_area()
        self.assertAlmostEqual(shape.area, 16 * pi)

    def test_unrepresentable_area(self):
        """Reject overflow and underflow without changing valid state."""
        shape = Circle(0, 0, 4)
        for value in (1e308, 1e-300):
            with self.subTest(value=value):
                before = (shape.radius, shape.area)
                with self.assertRaises(ValueError):
                    shape.radius = value
                self.assertEqual((shape.radius, shape.area), before)
                with self.assertRaises(ValueError):
                    Circle(0, 0, value)


if __name__ == "__main__":
    unittest.main()
