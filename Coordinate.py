class Coordinate:
    limit ={
        "width": -1,
        "height": -1
    }

    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return (self.x > other.x) and (self.y > other.y)

    def __lt__(self, other):
        return (self.x < other.x) and (self.y < other.y)

    def __ne__(self, other):
        return not self == other

    def __ge__(self, other):
        return (self.x >= other.x) and (self.y >= other.y)

    def __le__(self, other):
        return (self.x <= other.x) and (self.y <= other.y)

    @staticmethod
    def validate_coordinate(x,y):
        return (x < Coordinate.limit["width"] and x >= 0) and (y < Coordinate.limit["height"] and y >= 0)

    @property
    def X(self):
        return self.x

    @property
    def Y(self):
        return self.y