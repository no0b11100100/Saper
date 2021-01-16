from Cell import *
from Coordinate import *
from random import randrange
import random
import collections

class Board:
    def __init__(self, w, h, tile_size):
        self.cells = [[Cell(j,i,tile_size) for i in range(w)] for j in range(h)]
        self.opened_cells = 0

    @property
    def Cells(self):
        return self.cells

    @property
    def OpenedCells(self):
        return self.opened_cells

    def open_around_cells(self, cell):
        cell.change_state("OPEN")
        cell.change_color()

        for neighbor in cell.Neighbors:
            if self.cells[neighbor.X][neighbor.Y].State == Cell.states["FLAG"]:
                self.cells[neighbor.X][neighbor.Y].change_state("CLOSE")

            self.open_cell(neighbor)

    def open_cell(self, index):
        if type(index) is Coordinate:
            row, column = index.X, index.Y
        else:
            row, column = index

        cell = self.cells[row][column]
        if cell.State == Cell.states["BOMB"]:
            cell.change_color()
            print("GAME OVER")
            return False
        elif cell.State == Cell.states["CLOSE"]:
            self.opened_cells += 1
            if cell.Number > 0:
                cell.change_state("OPEN")
                cell.change_color()
            else:
                self.open_around_cells(cell)

        return True

    def flag_cell(self, index):
        row, column = index
        cell = self.cells[row][column]

        if cell.State == Cell.states["BOMB"]:
            cell.change_state("FLAGBOMB")
            self.cells[row][column].change_color()

        elif cell.State == Cell.states["FLAGBOMB"]:
            cell.change_state("BOMB")
            cell.change_color(Cell.states["CLOSE"])

        elif cell.State == Cell.states["FLAG"]:
            cell.change_state("CLOSE")
            self.cells[row][column].change_color()

        elif cell.State == Cell.states["CLOSE"]:
            cell.change_state("FLAG")
            self.cells[row][column].change_color()