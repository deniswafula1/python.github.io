class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

def perimeter(self):
            return  2 *(self.length + self.width)
def area(self):
             return self.length * self.width
def display_info(self):
    print(f"lenght: {self.length}, width: {self.width}")
    print(f"perimeter: {self.perimeter()}")
    print(f"Area: {self.area()}")
    print()
    #creating four rectangle objects
    rectangle1 = Rectangle(length=20, width=10)
    rectangle2 = Rectangle(length=6, width=4)
    rectangle3 = Rectangle(length=12, width=6)
    rectangle4 = Rectangle(length=21, width=9)
    #displaying the information


        rectangle1.display()
rectangle2.display()
rectangle3.display()
rectangle4.display()



