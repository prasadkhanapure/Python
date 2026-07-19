import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return math.sqrt((self.width ** 2) + (self.height ** 2))

    def get_picture(self):
        if self.height > 50 or self.width >50:
            return "Too big for picture."
            
        picture = ""
        for item in range(self.height):
            picture += "*" * self.width + "\n"
        return picture
    
    
    def get_amount_inside(self, shape):
        return (self.height // shape.height) * (self.width // shape.width)

rect1 = Rectangle(15,10)
print(rect1.get_area())
print(rect1.get_perimeter())
print(rect1.get_diagonal())
print(rect1.get_picture())

rect2 = Rectangle(3,2)
print(rect2)



class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side,side)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_width(self, side):
        # super().set_width(side)
        self.width = side
        self.height = side

    def set_height(self, side):
        # super().set_height(side)
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side    

square1 = Square(7)
# print(square1)
print(Rectangle(15,10).get_amount_inside(Square(5)))