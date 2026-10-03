"""Verify basic shape behavior with repeatable unittest cases."""

import unittest
from basic_shape import BasicShape
from circle import Circle
from rectangle import Rectangle
from square import Square


class TestBasicShape(unittest.TestCase):
    """Exercise public behavior and preserve shape invariants."""

    def test_abstract_base(self):
        """Reject direct construction of the abstract interface."""
        with self.assertRaises(TypeError):
            BasicShape("Shape")

    def test_incomplete_subclass(self):
        """Require concrete implementation of the abstract method."""
        class Incomplete(BasicShape):
            """Intentionally leave the abstract method unimplemented."""

        with self.assertRaises(TypeError):
            Incomplete("Incomplete")

    def test_common_interface(self):
        """Expose inherited name and area on every concrete class."""
        for shape in (Circle(0, 0, 2), Rectangle(2, 3), Square(2)):
            with self.subTest(shape=type(shape).__name__):
                self.assertIsInstance(shape, BasicShape)
                self.assertIsInstance(shape.name, str)
                self.assertGreater(shape.area, 0)

    def test_rename(self):
        """Change a valid name without changing area."""
        shape = Circle(0, 0, 2)
        area = shape.area
        shape.name = "Updated"
        self.assertEqual(shape.name, "Updated")
        self.assertEqual(shape.area, area)

    def test_invalid_name_types(self):
        """Reject nonstring names without replacing a valid name."""
        shape = Square(2)
        for value in (None, 3, True, []):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    shape.name = value
                self.assertEqual(shape.name, "Square")
                with self.assertRaises(TypeError):
                    Square(2, value)

    def test_blank_names(self):
        """Reject empty and whitespace-only names."""
        shape = Rectangle(2, 3)
        for value in ("", " ", "\t\n"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    shape.name = value
                self.assertEqual(shape.name, "Rectangle")
                with self.assertRaises(ValueError):
                    Rectangle(2, 3, value)

    def test_read_only_area(self):
        """Protect calculated area from client assignment."""
        for shape in (Circle(0, 0, 2), Rectangle(2, 3), Square(2)):
            area = shape.area
            with self.assertRaises(AttributeError):
                shape.area = 99
            self.assertEqual(shape.area, area)


if __name__ == "__main__":
    unittest.main()
