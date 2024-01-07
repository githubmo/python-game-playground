from sys import exit

import pygame


def main():
    width = 400
    height = 500

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    test_surface = pygame.Surface((100, 200))
    test_surface.fill((0, 0, 255))
    test_rect = test_surface.get_rect(center=(width / 2, height / 2))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill((175, 215, 70))
        test_rect.left += 1
        pygame.draw.rect(screen, "Red", test_rect)
        screen.blit(test_surface, test_rect)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
