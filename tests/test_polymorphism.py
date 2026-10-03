"""Verify polymorphism behavior with repeatable unittest cases."""

import unittest
from math import pi
from basic_shape import BasicShape
from circle import Circle
from rectangle import Rectangle
from square import Square


class TestPolymorphism(unittest.TestCase):
    """Exercise public behavior and preserve shape invariants."""

    def test_mixed_collection(self):
        """Read names and correct areas through one common interface."""
        shapes = [Circle(0, 0, 4, "C1"), Circle(-3, 2, 9, "C2"), Rectangle(10, 20, "R1"), Rectangle(20, 30, "R2"), Square(10)]
        expected = [("C1", 16*pi), ("C2", 81*pi), ("R1", 200), ("R2", 600), ("Square", 100)]
        for shape, (name, area) in zip(shapes, expected):
            with self.subTest(name=name):
                self.assertIsInstance(shape, BasicShape)
                self.assertEqual(shape.name, name)
                self.assertAlmostEqual(shape.area, area)

    def test_method_dispatch(self):
        """Call the same abstract-interface method on every concrete type."""
        shapes = [Circle(0, 0, 2), Rectangle(2, 3), Square(4)]
        for shape in shapes:
            shape.calc_area()
        for shape, expected in zip(shapes, (4*pi, 6, 16)):
            self.assertAlmostEqual(shape.area, expected)

    def test_updated_collection(self):
        """Observe changed areas through references in a mixed collection."""
        circle = Circle(0, 0, 1)
        rectangle = Rectangle(2, 3)
        square = Square(4)
        shapes = [circle, rectangle, square]
        circle.radius = 2
        rectangle.width = 5
        square.length = 6
        for shape, expected in zip(shapes, (4*pi, 10, 36)):
            self.assertAlmostEqual(shape.area, expected)


if __name__ == "__main__":
    unittest.main()
