import sys

import pygame
from pygame import Surface

from game_playground.model.fruit import Fruit
from game_playground.model.snake import Snake


class GameState:
    def __init__(self, cell_size: int, cell_number: int):
        self.cell_size = cell_size
        self.cell_number = cell_number
        self.fruit = Fruit(cell_size, cell_number)
        self.snake = Snake(cell_size)

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self, screen: Surface):
        self.fruit.draw_fruit(screen, self.cell_size)
        self.snake.draw_snake(screen)

    def check_collision(self):
        if self.fruit.pos == self.snake.head_pos():
            print("snack")
            self.fruit.randomise()
            self.snake.add_block()
        else:
            print(f"fruit: {self.fruit.pos} ::: snake: {self.snake.head_pos()}")

    def check_fail(self):
        if (
                not 0 <= self.snake.body[0].x < self.cell_number
                or not 0 <= self.snake.body[0].y < self.cell_size
        ):
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()
