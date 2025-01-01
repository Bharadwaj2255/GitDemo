

class Calculator:
    num = 100

    def getData(self, a, b):
        self.a = a
        self.b = b
        print(a+b)

    def setprint(self):
        print(self.a + self.b)

object = Calculator()
object.getData(10, 20)