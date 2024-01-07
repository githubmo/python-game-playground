import pygame
from pygame import Vector2, Surface


class Snake:
    def __init__(self, cell_size: int):
        self.body = [Vector2(7, 10), Vector2(6, 10), Vector2(5, 10)]
        self.cell_size = cell_size
        self.direction = Vector2(1, 0)
        self.new_block = False

    def draw_snake(self, screen: Surface) -> None:
        for block in self.body:
            block_rect = pygame.Rect(
                block.x * self.cell_size,
                block.y * self.cell_size,
                self.cell_size,
                self.cell_size,
            )
            pygame.draw.rect(screen, (100, 100, 255), block_rect)

    def head_pos(self) -> Vector2:
        return Vector2(self.body[0].x * self.cell_size, self.body[0].y * self.cell_size)

    def move_snake(self) -> None:
        new_head = self.body[0] + self.direction
        self.body.insert(0, new_head)
        if self.new_block:
            self.new_block = False
        else:
            self.body.pop()

    def add_block(self):
        self.new_block = True
