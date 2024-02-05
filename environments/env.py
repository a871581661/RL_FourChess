import numpy as np




class A():
    def __init__(self):
        self.a = [1,2,3,4,5,6]
        self.b = 2

    def get_a(self):
        for i in self.a:
            yield i


