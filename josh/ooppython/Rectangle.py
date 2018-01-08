#! /usr/bin/env python3

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def output(self):
        #print("Length = " self.length " Width = " self.width)
        print(str(self.length))

rect1 = Rectangle(45,65)