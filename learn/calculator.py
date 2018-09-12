class Calculator:
    def __init__(self, name, price, hight):
        self.n = name
        self.p = price
        self.h = hight

    def add(self, x, y):
        print(x + y)

    def subtract(self, x, y):
        print(x - y)

    def multiply(self, x, y):
        print(x * y)

    def divide(self, x, y):
        print(x / y)


c = Calculator(6, 6, 6)
c.n
c.p
c.h
c.add(2, 3)
c.subtract(3, 3)
c.multiply(5, 3)
c.divide(6, 3)
