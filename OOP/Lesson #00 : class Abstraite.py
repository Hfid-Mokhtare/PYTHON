from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def affiche_shape_name(self):
        pass

class Square(Shape):
    def __init__(self):
        self.side = float(input("Enter the side of the square: "))

    def calculate_area(self):
        return self.side * self.side

    def affiche_shape_name(self):
        print("Shape: Square")

class Circle(Shape):
    def __init__(self):
        self.radius = float(input("Enter the radius of the circle: "))

    def calculate_area(self):
        return self.radius * self.radius * 3.14159

    def affiche_shape_name(self):
        print("Shape: Circle")

class Triangle(Shape):
    def __init__(self):
        self.base = float(input("Enter the base of the triangle: "))
        self.height = float(input("Enter the height of the triangle: "))

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def affiche_shape_name(self):
        print("Shape: Triangle")

def main():
    shape_choice = int(input("Enter the shape (1: Square, 2: Circle, 3: Triangle): "))

    if shape_choice == 1:
        shape = Square()
    elif shape_choice == 2:
        shape = Circle()
    elif shape_choice == 3:
        shape = Triangle()
    else:
        print("Invalid shape choice.")
        return

    shape.affiche_shape_name()
    area = shape.calculate_area()
    print("The area of the shape is:", area)

if __name__ == "__main__":
    main()
