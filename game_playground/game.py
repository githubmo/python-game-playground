from sys import exit

import pygame
from pygame import Vector2

from game_playground.logic.game_state import GameState


def main():
    cell_size = 40
    cell_number = 20

    pygame.init()
    screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
    clock = pygame.time.Clock()

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 100)

    game_state = GameState(cell_size, cell_number)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == SCREEN_UPDATE:
                game_state.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if game_state.snake.direction.y != 1:
                        game_state.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_DOWN:
                    if game_state.snake.direction.y != -1:
                        game_state.snake.direction = Vector2(0, 1)
                if event.key == pygame.K_LEFT:
                    if game_state.snake.direction.x != 1:
                        game_state.snake.direction = Vector2(-1, 0)
                if event.key == pygame.K_RIGHT:
                    if game_state.snake.direction.x != -1:
                        game_state.snake.direction = Vector2(1, 0)

        screen.fill((175, 215, 70))
        game_state.draw_elements(screen)
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
