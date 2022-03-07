class Shape:
    def __init__(self,color='red',filled=True):
        self.__color = color
        self.__filled = filled

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self,color:str):
        self.__color = color

    @property
    def filled(self):
        return self.__filled

    @filled.setter
    def filled(self,filled:bool):
        self.__filled = filled

    def to_string(self):
        if self.__filled:
            return f'A Shape with color of {self.__color} and filled'
        else:
            return f'A Shape with color of {self.__color} and not filled'

class Circle(Shape):
    def __init__(self,radius=1.0,color='red',filled=True):
        Shape.__init__(self,color,filled)
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self,radius):
        self.__radius = radius

    @property
    def area(self):
        return 3.14159265359*(self.__radius**2)

    @property
    def perimeter(self):
        return 2*3.14159265359*self.__radius

    def to_string(self):
        return f'A Circle with radius {self.__radius}, which is a subclass of Shape class'


class Rectangle(Shape):
    def __init__(self,width=5.0,length=9.0,color='cyan',filled=True):
        Shape.__init__(self,color,filled)
        self.__width = width
        self.__length = length

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self,width):
        self.__width = width

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self,length):
        self.__length = length

    @property
    def area(self):
        return self.__width*self.__length

    @property
    def perimeter(self):
        return 2*(self.__width+self.__length)

    def to_string(self):
        return f'A Rectangle with width {self.__width} and length {self.__length}, which is a subclass of Shape class.'

class Square(Rectangle,Shape):
    def __init__(self, side=1.0, color='red', filled=True, width=4.0, length=6.0):
        Rectangle.__init__(self, width, length, color, filled)
        self.width = side
        self.length = side

    @property
    def side(self):
        return self.width

    @side.setter
    def side(self, side):
        self.width = side
        self.length = side

    def set_width(self, side):
        self.width = side
        self.length = side

    def set_length(self, side):
        self.length = side
        self.width = side

    def to_string(self):
        return f'A Square with side {self.width}, which is a subclass of Rectangle class'

def main():
    #shape class
    print(f'===shape===')
    a = Shape('blue', True)
    print(a.color)
    print(a.to_string())
    a.color = 'magenta'
    print(a.color)
    a.filled = False
    print(a.to_string())

    #circle class
    print(f'\n===circle===')
    b = Circle(1.0, 'black', True)
    print(b.color)
    print(b.area)
    print(b.to_string())
    b.radius = 5.0
    b.color = 'cyan'
    print(b.area)
    print(b.color)
    print(b.to_string())

    #rectangle class
    print(f'\n===rectangle===')
    c = Rectangle(4.0, 9.0, 'purple', True)
    print(c.color)
    print(c.area)
    print(c.perimeter)
    c.width = 8.3
    c.length = 19.1
    print(c.area)
    print(c.perimeter)
    print(c.to_string())

    #square class
    print(f'\n===square===')
    d = Square(9.0, 'yellow', True)
    print(d.color)
    print(d.side)
    print(d.area)
    print(d.perimeter)
    print(d.to_string())
    d.color = 'brown'
    d.side = 8.0
    print(d.color)
    print(d.area)
    print(d.perimeter)
    print(d.to_string())
    d.set_length(3.0)
    print(d.area)
    print(d.perimeter)
    print(d.to_string())
    d.set_width(4.0)
    print(d.area)
    print(d.perimeter)
    print(d.to_string())

main()