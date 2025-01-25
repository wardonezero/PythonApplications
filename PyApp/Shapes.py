class Shape:
    def __init__(self, color, isFilled):
        self.color = color
        self.isFilled = isFilled

class Triangle(Shape):
    def __init__(self, color, isFilled, base, height):
        super().__init__(color, isFilled)
        self.base = base
        self.height = height

    def describe(self):
        print(f"It is a triangle with an area of {self.base * self.height / 2}cm^2")
        super().describe()

class Circle(Shape):
    def __init__(self, color, isFilled, radius):
        super().__init__(color, isFilled)
        self.radius = radius
    
    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2")
        super().describe()

class Square(Shape):
    def __init__(self, color, isFilled, side):
        super().__init__(color, isFilled)
        self.side = side

    def describe(self):
        print(f"It is a square with an area of {self.width * self.width}cm^2")
        super().describe()