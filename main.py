import pygame
from constants import *
from snake import Snake
import random
from food import Food

def get_free_space(validCoords, invalidCoords):
    vcords = validCoords.copy()
    for ex in invalidCoords:
        if ex in vcords:
            vcords.remove(ex)
    return vcords

def main():
    valid_coords = [(x, y) for x in range(0, SCREEN_WIDTH-BLOCK_SIZE, BLOCK_SIZE) for y in range(0, SCREEN_HEIGHT-BLOCK_SIZE, BLOCK_SIZE)]

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    snake = Snake(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    food = Food(get_free_space(valid_coords, snake.position))

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        snake.draw(screen)
        food.draw(screen)
        snake.update()
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
