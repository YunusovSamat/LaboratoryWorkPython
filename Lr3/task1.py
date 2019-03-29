import random

import pygame
from pygame.locals import *


class GameOfLife:
    def __init__(self, width=640, height=480, cell_size=10, speed=5):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed


    def draw_grid(self):
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (0, y), (self.width, y))


    def cell_list(self, randomize=False):
        if randomize:
            mas = [[random.randint(0, 1) for i in range(self.cell_width)]
                   for j in range(self.cell_height)]
        else:
            mas = [[0 for i in range(self.cell_width)]
                   for j in range(self.cell_height)]

        self.mas = mas
        return self.mas


    def draw_cell_list(self, rects="green"):
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                if self.mas[i][j] == 1:
                    pygame.draw.rect(self.screen, pygame.Color(rects), (j*20, i*20, 20, 20))
                else:
                    pygame.draw.rect(self.screen, pygame.Color("white"), (j*20, i*20, 20, 20))


    def get_neighbours(self, cell):
        row, col = cell
        len_r = len(self.mas)
        len_c = len((self.mas[0]))
        mas_frame = [[0 for j in range(len_c + 2)] for i in range(len_r + 2)]

        for i in range(1, len_r + 1):
            for j in range(1, len_c + 1):
                mas_frame[i][j] = self.mas[i - 1][j - 1]

        mas = []

        for i in range(3):
            for j in range(3):
                if not((i == 1) and (j == 1)):
                    mas.append(mas_frame[row + i][col + j])

        self.neighbors = mas
        return mas


    def update_cell_list(self, cell_list):
        mas_new = [[0 for j in range(len(cell_list[0]))] for i in range(len(cell_list))]
        for i in range(len(cell_list)):
            for j in range(len(cell_list[0])):
                mas_neighbors = self.get_neighbours((i, j))
                count = mas_neighbors.count(1)
                if cell_list[i][j] == 1:
                    if ((count != 2) and
                            (count != 3)):
                        mas_new[i][j] = 0
                    else:
                        mas_new[i][j] = 1
                else:
                    if count == 3:
                        mas_new[i][j] = 1
        return mas_new


    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))
        running = True
        self.cell_list(True)
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_grid()
            pygame.display.flip()
            self.draw_cell_list()
            self.mas = self.update_cell_list(self.mas.copy())

            clock.tick(self.speed)
            self.draw_cell_list()

        pygame.quit()

# row = int(input(("Введите размер строки: "))) * 20
# col = int(input(("Введите размер столбеца: "))) * 20

if __name__ == '__main__':
    game = GameOfLife(640, 320, 20)
    game.run()


