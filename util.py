class Circle :
    def __init__(self, radius=1):
        self.radius = radius
    def __str__(self):
        return f"radius = {self.radius}"

    def perimeter(self):
        return self.radius * 2 * 3.14


def add(n1, n2) :
    return n1 + n2


def test() :
    print("test function called")


