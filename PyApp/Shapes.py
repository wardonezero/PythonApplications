from abc import ABC, abstractmethod

class Shape:
    def __init__(self, color, isFilled):
        self.color = color
        self.isFilled = isFilled
    
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.isFilled else 'not filled'}")
    
    @abstractmethod
    def area(self):
        pass

class Triangle(Shape):
    def __init__(self, color, isFilled, base, height):
        super().__init__(color, isFilled)
        self.base = base
        self.height = height

    def describe(self):
        print(f"It is a triangle with an area of {self.area()}cm^2")
        super().describe()
    
    def area(self):
        return self.base * self.height / 2

class Circle(Shape):
    def __init__(self, color, isFilled, radius):
        super().__init__(color, isFilled)
        self.radius = radius
    
    def describe(self):
        print(f"It is a circle with an area of {self.area()}cm^2")
        super().describe()

    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, color, isFilled, side):
        super().__init__(color, isFilled)
        self.side = side

    def describe(self):
        print(f"It is a square with an area of {self.area}cm^2")
        super().describe()

    def area(self):
        return self.side * self.side