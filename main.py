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

def show_scoreboard(screen, score):
    font = pygame.font.SysFont(None, 72)
    text = font.render(f"Final Score: {score}", True, (255, 255, 255))
    
    screen.fill((0, 0, 0))            # Clear screen once
    screen.blit(text, (100, 100))    # Draw text once
    pygame.display.flip()             # Flip once
    
    # Now wait for user to close or press key
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                waiting = False

def main():
    valid_coords = [(x, y) for x in range(0, SCREEN_WIDTH, BLOCK_SIZE) for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE)]

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    snake = Snake(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    food = Food(get_free_space(valid_coords, snake.position))
    #print("freespace: ", get_free_space(valid_coords, snake.position))

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return        

        screen.fill("black")

        keys = pygame.key.get_pressed()

        snake.draw(screen)
        food.draw(screen)

        if snake.selfe_colison():
            #print("Game over!")
            #print(f"Your Score: {snake.score}")
            show_scoreboard(screen, snake.score)
            exit()

        snake.handle_input(keys)
        snake.update()
        if snake.eat(food.position):
            food = Food(get_free_space(valid_coords, snake.position))

        snake.digest()
        pygame.display.flip()

        dt = clock.tick(60) / 1000

    


if __name__ == "__main__":
    main()
