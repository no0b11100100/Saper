from Coordinate import *

class Cell:
    states = {
        "CLOSE": 0,
        "OPEN": 1,
        "FLAG": 2,
        "BOMB": 3,
        "FLAGBOMB": 4
    }

    colors = [
        (150,150,150),
        (230,230,230),
        (0,200,0),
        (200,0,0),
        (0,200,0)
    ]

    def __init__(self, x, y, tile_size):
        self.state = Cell.states["CLOSE"]
        self.color = Cell.colors[self.state]
        self.size = tile_size
        self.position = (x*self.size, y*self.size)
        self.number = 0
        self.neighbors = [Coordinate(i,j) for i in range(x-1, x+2) for j in range(y-1, y+2) if not Coordinate(i,j) == Coordinate(x,y) and Coordinate.validate_coordinate(i,j)]

    def change_state(self, newState):
        self.state = Cell.states[newState]

    def change_color(self, state=None):
        self.color = Cell.colors[self.state] if state == None else Cell.colors[state]

    @property
    def Neighbors(self):
        return self.neighbors

    @property
    def Text(self):
        if self.number == 0:
            return ""
        return str(self.number)

    @property
    def Number(self):
        return self.number

    @Number.setter
    def Number(self, new_number):
        self.number = new_number

    @property
    def State(self):
        return self.state

    @property
    def Color(self):
        return self.color

    @property
    def Position(self):
        return self.position

    @property
    def Size(self):
        return self.size