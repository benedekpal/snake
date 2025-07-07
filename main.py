import pygame
from constants import *
from snake import Snake
import random
from food import Food
import json

def get_free_space(validCoords, invalidCoords):
    vcords = validCoords.copy()
    for ex in invalidCoords:
        if ex in vcords:
            vcords.remove(ex)
    return vcords

def show_score(screen, score):
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

def show_scoreboard(screen, highscores):
    font = pygame.font.SysFont(None, FONT_SIZE)
    screen.fill((0,0,0))
    index = 0  
    for username, score in highscores.items():
        text = font.render(f"{username}: {score}", True, (255, 255, 255))
        screen.blit(text, (0, index * LINE_OFFSET))
        index += 1

    pygame.display.flip()             # Flip once
    
    # Now wait for user to close or press key
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                waiting = False


def get_username(screen):
    pygame.font.init()
    font = pygame.font.SysFont(None, 48)

    username = ""
    input_active = True

    while input_active:
        screen.fill((0, 0, 0))  # Clear screen
        prompt = font.render("Enter your name:", True, (255, 255, 255))
        text_surface = font.render(username + "|", True, (255, 255, 255))

        screen.blit(prompt, (50, 100))
        screen.blit(text_surface, (50, 160))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                input_active = False
                return None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                elif event.unicode.isprintable():
                    username += event.unicode

    return username


def load_scores():
    with open(SAVES, 'r') as file:
        data = json.load(file)
    return data

def save_scores(data):
    with open(SAVES, 'w') as file:
        json.dump(data, file, indent=4)

def check_scores(score, highscores):
    scores = list(highscores.values())
    if scores[-1] < score:
        return True
    return False

def update_highscores(username, score, highscores):
    scores = list(highscores.items()) + [(username, score)] 
    scores.sort(key=lambda item: item[1], reverse=True)
    topScores = scores[:20]
    return dict(topScores)


def main():
    valid_coords = [(x, y) for x in range(0, SCREEN_WIDTH, BLOCK_SIZE) for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE)]
    username = ""

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
            highScores = load_scores()
            score = snake.score
            if check_scores(score, highScores):
                username = get_username(screen)
                highScores = update_highscores(username, score, highScores)
                show_scoreboard(screen, highScores)
                save_scores(highScores)
            else:
                show_score(screen, score)
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
