class Rectangle:
    """Class representing a rectangle"""

    def __init__(self, width: float, height: float) -> None:
        """Initialize a rectangle with width and height"""
        self.width = width
        self.height = height

    def area(self) -> float:
        """Return the area of the rectangle"""
        return self.width * self.height

    def perimeter(self) -> float:
        """Return the perimeter of the rectangle"""
        return 2 * (self.width + self.height)

    def is_square(self) -> bool:
        """Return True if rectangle is a square, else False"""
        return self.width == self.height

    def resize(self, new_width: float, new_height: float) -> None:
        """Change width and height of the rectangle"""
        self.width = new_width
        self.height = new_height


rect = Rectangle(5, 10)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())
print("Is square:", rect.is_square())

rect.resize(7, 7)
print("Resized area:", rect.area())
print("Is square after resize:", rect.is_square())
