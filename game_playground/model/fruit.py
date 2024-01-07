import random

import pygame
from pygame import Surface
from pygame.math import Vector2


class Fruit:
    def __init__(self, cell_size: int, cell_number: int):
        self.cell_number = cell_number
        self.cell_size = cell_size
        self.randomise()

    def draw_fruit(self, screen: Surface, cell_size: int):
        fruit_rect = pygame.Rect(self.pos.x, self.pos.y, cell_size, cell_size)
        pygame.draw.rect(screen, (126, 166, 114), fruit_rect)

    def randomise(self):
        self.x = random.randint(0, self.cell_number - 1)
        self.y = random.randint(0, self.cell_number - 1)
        self.pos = Vector2(self.x * self.cell_size, self.y * self.cell_size)
