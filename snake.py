import pygame
from constants import *

class Snake:
    def __init__(self, startX, startY):
        self.head = (startX, startY)
        self.body = []
        self.stomach = []
        self.direction = (-1, 0)

        self.moveDelay = DEFAULT_DELAY  # milliseconds between moves
        self.lastMoveTime = 0
        self.nextDirection = self.direction

        self._score = 0

    def square(self, x, y):
        return pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)

    def draw(self, screen):
        pygame.draw.rect(screen, "yellow", self.square(self.head[0], self.head[1]))
        for segment in self.body:
            pygame.draw.rect(screen, "green", self.square(segment[0], segment[1]))

    def is_on(self, obj1, obj2):
        return obj1 == obj2

    def increase_score(self):
        self._score += 1

        if self._score % DIFFICULTY_THRESHOLD == 0:
            self.moveDelay -= SPEED_UP
            self.moveDelay = max(MINIMUM_DELAY, self.moveDelay - SPEED_UP)

    def eat(self, food):
        if self.is_on(self.head, food):
            self.stomach.append(food)
            self.increase_score()
            return True
        return False

    def grow(self, segment):
        self.body.append(segment)

    def digest(self):
        digested = []

        for food in self.stomach:
            if food not in self.position:
                self.grow(food)
                digested.append(food)

        for food in digested:
            self.stomach.remove(food)

    def update(self):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastMoveTime >= self.moveDelay:
            self.direction = self.nextDirection
            self.move()
            self.lastMoveTime = currentTime

    def move(self):
        newHeadX = self.head[0] + self.direction[0] * BLOCK_SIZE
        newHeadY = self.head[1] + self.direction[1] * BLOCK_SIZE

        if newHeadX < 0:
            newHeadX = SCREEN_WIDTH - BLOCK_SIZE
        elif newHeadX >= SCREEN_WIDTH:
            newHeadX = 0

        if newHeadY < 0:
            newHeadY = SCREEN_HEIGHT - BLOCK_SIZE
        elif newHeadY >= SCREEN_HEIGHT:
            newHeadY = 0

        self.body.insert(0, self.head)
        if self.body:
            self.body.pop()
        self.head = (newHeadX, newHeadY)

    def handle_input(self, keys):
        if keys[pygame.K_UP] and self.direction != (0, 1):
            self.nextDirection = (0, -1)
        elif keys[pygame.K_DOWN] and self.direction != (0, -1):
            self.nextDirection = (0, 1)
        elif keys[pygame.K_LEFT] and self.direction != (1, 0):
            self.nextDirection = (-1, 0)
        elif keys[pygame.K_RIGHT] and self.direction != (-1, 0):
            self.nextDirection = (1, 0)

    def selfe_colison(self):
        if self.head in self.body:
            return True
        return False

    @property
    def position(self):
        return self.body + [self.head]

    @property
    def score(self):
        return self._score
