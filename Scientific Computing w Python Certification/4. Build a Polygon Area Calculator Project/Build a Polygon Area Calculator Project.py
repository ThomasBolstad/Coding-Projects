class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width
        return width

    def set_height(self, height):
        self.height = height
        return height


    def get_area(self):
        area = 0
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 0
        perimeter = (2 * self.width) + (2 * self.height)
        return perimeter


    def get_diagonal(self):
        diagonal = 0
        diagonal = ((self.width) ** 2 + (self.height) ** 2) ** .5
        return diagonal

    def get_picture(self):
        picture = ''
        if self.height > 50 or self.width > 50:
            picture = f'Too big for picture.'
        else:
            for line in range(self.height):
                line_str = '*' * self.width
                line_str += f'\n'
                picture += line_str
        return picture


    def get_amount_inside(self, shape_or_width, height=None):
        if isinstance(shape_or_width, (Rectangle, Square)):
            width = shape_or_width.width
            height = shape_or_width.height
        else:
            width = shape_or_width
            if height is None:
                raise ValueError("Height must be provided if first argument is not a shape")
        amount_inside = (self.width // width) * (self.height // height)
        return amount_inside

    def __str__(self):
        output  = ''
        if self.height >50 or self.width > 50:
            output = f'Too big for picture.'
        else:
            rect_str = f'Rectangle(width={self.width}, height={self.height})'
            output += rect_str
        return output

class Square(Rectangle):
    
    def __init__(self, width, height=0):
        super().__init__(width = width, height = height)
        self.height = self.width
        height = width
        
    def set_width(self, width):
        self.width = width
        self.height = width  # Ensure height equals width
        return width

    def set_height(self, height):
        self.height = height
        self.width = height  # Ensure width equals height
        return height

    def set_side (self,side):
        self.height = side
        self.width = side
        return side    
    
    def get_amount_inside(self, width, height=0):
        amount_inside = 0
        amount_inside = (self.width // width) ** 2
        print(self.width, width, self.height, height)
        return amount_inside

    def __str__(self):
        output  = ''
        if self.height >50 or self.width > 50:
            output = f'Too big for picture.'
        else:
            sqr_str = f'Square(side={self.width})'
            output += sqr_str
        return output
    
        


rect = Rectangle(25,10)
sq = Square(6)
print('\nArea of Rectangle:',rect.get_area(),'\n')
print('Length of Rectangle Diagonal',f'{rect.get_diagonal():.2f}\n')
print('Perimeter of Rectangle:',rect.get_perimeter(),'\n')
print(rect,'\n')
print(rect.get_picture())
print('-' * (max(rect.width, sq.width)))
print('\nArea of Square:',sq.get_area(),'\n')

print('Perimeter of Sq:',sq.get_perimeter(),'\n')
print(sq,'\n')
print(sq.get_picture())

print('The Square fits inside the Rectangle', rect.get_amount_inside(sq),'times')

