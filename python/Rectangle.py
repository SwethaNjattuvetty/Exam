

class Rectangle:
    def __init__(self, length: int, width: int):
        """
        Initialize the Rectangle with length and width.
        """
        self.length = length
        self.width = width

    def __iter__(self):
        """
        Iterate over the Rectangle object to return length and width step-by-step.
        """
        yield {'length': self.length}
        yield {'width': self.width}

rect = Rectangle(10, 5)


for attribute in rect:
    print(attribute)
