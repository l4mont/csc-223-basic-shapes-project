"""Verify square behavior with repeatable unittest cases."""

import unittest
from rectangle import Rectangle
from square import Square


class TestSquare(unittest.TestCase):
    """Exercise public behavior and preserve shape invariants."""

    def test_construction(self):
        """Start with three equal dimensions and correct area."""
        shape = Square(10)
        self.assertEqual((shape.side, shape.length, shape.width), (10, 10, 10))
        self.assertEqual(shape.area, 100)

    def test_inheritance(self):
        """Reuse Rectangle behavior through multilevel inheritance."""
        shape = Square(3)
        self.assertIsInstance(shape, Rectangle)
        self.assertIs(Square.calc_area, Rectangle.calc_area)

    def test_names(self):
        """Support default and custom square names."""
        self.assertEqual(Square(2).name, "Square")
        self.assertEqual(Square(2, "Tile").name, "Tile")

    def test_decimal_side(self):
        """Calculate fractional square area."""
        self.assertAlmostEqual(Square(0.2).area, 0.04)

    def test_side_change(self):
        """Synchronize all dimensions when side changes."""
        shape = Square(10)
        shape.side = 20
        self.assertEqual((shape.side, shape.length, shape.width, shape.area), (20, 20, 20, 400))

    def test_length_change(self):
        """Synchronize all dimensions when inherited length changes."""
        shape = Square(10)
        shape.length = 7
        self.assertEqual((shape.side, shape.length, shape.width, shape.area), (7, 7, 7, 49))

    def test_width_change(self):
        """Synchronize all dimensions when inherited width changes."""
        shape = Square(10)
        shape.width = 5
        self.assertEqual((shape.side, shape.length, shape.width, shape.area), (5, 5, 5, 25))

    def test_successive_changes(self):
        """Preserve the invariant over a sequence of different assignments."""
        shape = Square(2)
        for attr, value in (("side", 3), ("length", 4), ("width", 2.5), ("side", 1)):
            setattr(shape, attr, value)
            self.assertEqual((shape.side, shape.length, shape.width), (value, value, value))
            self.assertAlmostEqual(shape.area, value * value)

    def test_invalid_construction(self):
        """Reject nonpositive, nonfinite, and wrongly typed sides."""
        for value, error in ((0, ValueError), (-2, ValueError), ("2", TypeError), (None, TypeError), (True, TypeError), (2j, TypeError), (float("nan"), ValueError), (float("inf"), ValueError)):
            with self.subTest(value=value):
                with self.assertRaises(error):
                    Square(value)

    def test_failed_assignment_preserves_state(self):
        """Preserve the entire square after any invalid public assignment."""
        shape = Square(4)
        for attr in ("side", "length", "width"):
            for value, error in ((0, ValueError), (-2, ValueError), ("2", TypeError), (None, TypeError), (True, TypeError), (float("nan"), ValueError)):
                with self.subTest(attr=attr, value=value):
                    before = (shape.side, shape.length, shape.width, shape.area)
                    with self.assertRaises(error):
                        setattr(shape, attr, value)
                    self.assertEqual((shape.side, shape.length, shape.width, shape.area), before)

    def test_unrepresentable_area(self):
        """Reject overflow and underflow through every dimension property."""
        for attr in ("side", "length", "width"):
            for value in (1e308, 1e-300):
                with self.subTest(attr=attr, value=value):
                    shape = Square(4)
                    with self.assertRaises(ValueError):
                        setattr(shape, attr, value)
                    self.assertEqual((shape.side, shape.length, shape.width, shape.area), (4, 4, 4, 16))
        for value in (1e308, 1e-300):
            with self.assertRaises(ValueError):
                Square(value)


if __name__ == "__main__":
    unittest.main()
