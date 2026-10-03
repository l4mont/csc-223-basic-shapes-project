"""Demonstrate polymorphism and automatic area updates through public properties."""

from basic_shape import BasicShape
from circle import Circle
from rectangle import Rectangle
from square import Square


def main():
    """Display five shapes and show circle, rectangle, and square dimension changes."""
    circle = Circle(0, 0, 4, "Circle_1")
    rectangle = Rectangle(10, 20, "Rectangle_1")
    square = Square(10)
    shapes: list[BasicShape] = [
        circle, Circle(-3, 2, 9, "Circle_2"),
        rectangle, Rectangle(20, 30, "Rectangle_2"), square,
    ]

    print("--- Polymorphism check ---")
    for shape in shapes:
        print(f"{shape.name}: area = {shape.area:.5f}")

    print("\n--- Automatic recalculation ---")
    print(f"{circle.name} before: radius={circle.radius:g}, area={circle.area:.5f}")
    circle.radius = 8
    print(f"{circle.name} after:  radius={circle.radius:g}, area={circle.area:.5f}")
    print(f"{rectangle.name} before: length={rectangle.length:g}, "
          f"width={rectangle.width:g}, area={rectangle.area:g}")
    rectangle.length = 20
    print(f"After length change: length={rectangle.length:g}, "
          f"width={rectangle.width:g}, area={rectangle.area:g}")
    rectangle.width = 40
    print(f"After width change:  length={rectangle.length:g}, "
          f"width={rectangle.width:g}, area={rectangle.area:g}")
    print(f"{square.name} before: side={square.side:g}, length={square.length:g}, "
          f"width={square.width:g}, area={square.area:g}")
    square.side = 20
    print(f"{square.name} after:  side={square.side:g}, length={square.length:g}, "
          f"width={square.width:g}, area={square.area:g}")


if __name__ == "__main__":
    main()
