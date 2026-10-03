"""Verify rectangle behavior with repeatable unittest cases."""

import unittest
from rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Exercise public behavior and preserve shape invariants."""

    def test_construction(self):
        """Initialize both dimensions safely and calculate area."""
        shape = Rectangle(10, 20)
        self.assertEqual((shape.length, shape.width), (10, 20))
        self.assertEqual(shape.area, 200)

    def test_decimal_dimensions(self):
        """Calculate area for fractional dimensions."""
        self.assertAlmostEqual(Rectangle(0.1, 0.2).area, 0.02)

    def test_names(self):
        """Support default and custom rectangle names."""
        self.assertEqual(Rectangle(2, 3).name, "Rectangle")
        self.assertEqual(Rectangle(2, 3, "Panel").name, "Panel")

    def test_invalid_dimensions(self):
        """Reject invalid input for either constructor dimension."""
        for attr in ("length", "width"):
            for value, error in ((0, ValueError), (-1, ValueError), ("3", TypeError), (None, TypeError), (True, TypeError), (1j, TypeError), (float("nan"), ValueError), (float("inf"), ValueError)):
                with self.subTest(attr=attr, value=value):
                    args = {"length": 2, "width": 3}
                    args[attr] = value
                    with self.assertRaises(error):
                        Rectangle(**args)

    def test_length_recalculation(self):
        """Update area after changing length."""
        shape = Rectangle(10, 20)
        shape.length = 30
        self.assertEqual(shape.area, 600)
        self.assertEqual(shape.width, 20)

    def test_width_recalculation(self):
        """Update area after changing width."""
        shape = Rectangle(10, 20)
        shape.width = 40
        self.assertEqual(shape.area, 400)
        self.assertEqual(shape.length, 10)

    def test_failed_assignment_preserves_state(self):
        """Preserve both dimensions and area after rejection."""
        shape = Rectangle(10, 20)
        for attr in ("length", "width"):
            for value, error in ((0, ValueError), (-2, ValueError), ("4", TypeError), (True, TypeError), (float("nan"), ValueError)):
                with self.subTest(attr=attr, value=value):
                    before = (shape.length, shape.width, shape.area)
                    with self.assertRaises(error):
                        setattr(shape, attr, value)
                    self.assertEqual((shape.length, shape.width, shape.area), before)

    def test_explicit_calc_area(self):
        """Recalculate using the required public method."""
        shape = Rectangle(2, 3)
        shape.calc_area()
        self.assertEqual(shape.area, 6)

    def test_unrepresentable_area(self):
        """Reject products outside the positive finite float range."""
        for dims, value in (((10, 20), 1e308), ((1e-200, 1e-100), 1e-300)):
            for attr in ("length", "width"):
                with self.subTest(dims=dims, attr=attr):
                    shape = Rectangle(*dims)
                    before = (shape.length, shape.width, shape.area)
                    with self.assertRaises(ValueError):
                        setattr(shape, attr, value)
                    self.assertEqual((shape.length, shape.width, shape.area), before)
        for length, width in ((1e308, 20), (1e-300, 1e-300)):
            with self.assertRaises(ValueError):
                Rectangle(length, width)


if __name__ == "__main__":
    unittest.main()
