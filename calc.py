class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        print('The addition of ', self.a, ' and ', self.b, ' is ', self.a + self.b)
    def sub(self):
        pass
    def mul(self):
        pass
    def div(self):
        pass

a = int(input("Enter the First value : "))
b = int(input("Enter second value : "))
c = Calculator(a,b)
c.add()
