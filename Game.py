import pygame
from Board import *

class Game:
    def __init__(self, width=9, height=9, tile_size=30):
        pygame.init()
        self.screen = pygame.display.set_mode((width * tile_size, height * tile_size))
        self.clock = pygame.time.Clock()
        self.screen.fill(pygame.Color('black'))
        self.font = pygame.font.SysFont('Arial', 10)

        Coordinate.limit["width"], Coordinate.limit["height"] = width, height
        self.board = Board(width, height, tile_size)
        self.isGame = True
        self.width, self.height = width, height
        self.cells_around_bombs = []
        self.bombs = 0
        self.generate_bomb()
        self.FPS = 30

    def convert_index(self, index):
        return (int(index / self.width), int(index % self.width))

    def convert_mouse_position(self, position):
        size = self.board.Cells[0][0].Size
        row = position[1] // size
        column = position[0] // size
        return row, column

    def set_numbers_around_bombs(self):
        for cell in self.cells_around_bombs:
            _count = self.cells_around_bombs.count(cell)
            self.board.Cells[cell.X][cell.Y].Number = _count

    def get_cells_around_bomb(self, cell):
        [self.cells_around_bombs.append(coor) for coor in cell.Neighbors]

    def validate_neighbors(self):
        validated_neighbors = []
        for i in self.cells_around_bombs:
            cell = self.board.Cells[i.X][i.Y]
            if cell.State != Cell.states["BOMB"]:
                validated_neighbors.append(i)
        return validated_neighbors

    def generate_bomb(self):
        bombs_count = randrange(int(((self.width*self.height) // 4) / 2), (self.width*self.height) // 4)
        sequence = [idx for idx in range(self.width*self.height)]
        boms = random.sample(sequence, bombs_count)
        self.bombs = len(boms)

        for bomb_index in boms:
            row, column = self.convert_index(bomb_index)
            cell = self.board.Cells[row][column]
            self.get_cells_around_bomb(cell)
            cell.change_state("BOMB")
            # cell.change_color() # show all bombs
            cell.Number = -1 # special value for bombs

        self.cells_around_bombs = self.validate_neighbors()
        self.set_numbers_around_bombs()

    def detect_click(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            if event.button == 1: # left button
                self.isGame = self.board.open_cell(self.convert_mouse_position(mouse_position))
                self.isGame = not self.check_win()
            elif event.button == 3: # right button
                self.board.flag_cell(self.convert_mouse_position(mouse_position))

    def check_win(self):
        if self.isGame:
            return (self.width*self.height) - self.board.OpenedCells == self.bombs
        return True

    def Run(self):
        while self.isGame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                self.detect_click(event)

            self.draw()

    def text_in_cell(self, cell):
        if cell.State == Cell.states["OPEN"]:
            self.screen.blit(self.font.render(cell.Text, True, pygame.Color('red')), (cell.Position[1] + cell.Size / 3, cell.Position[0] + cell.Size / 5))
            pygame.display.update()

    def draw(self):
        indents = 2
        for cells in self.board.Cells:
            for cell in cells:
                pygame.draw.rect(self.screen, cell.Color, pygame.Rect(cell.Position[1], cell.Position[0], cell.Size-indents, cell.Size-indents))
                self.text_in_cell(cell)

        pygame.display.flip()
        self.clock.tick(self.FPS)