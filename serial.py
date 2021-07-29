"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    Attributes:
    ___________
    start: int
        start number for the generator
    number: int
        a next sequential number 

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """create an instance of class SerialGenerator that starts from 'start' number"""
        self.start = start
        self.number = start-1

    def generate(self):
        """generate the next sequential number"""
        self.number = self.number + 1
        return self.number 

    def reset(self):
        """reset the generater to start number"""
        self.number = self.start-1
        



