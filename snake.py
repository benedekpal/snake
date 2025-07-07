import pygame
from constants import *

class Snake:
    def __init__(self, startX, startY):
        self.head = (startX, startY)
        self.body = []
        self.stomach = []
        self.direction = (-1, 0)

        self.moveDelay = 500  # milliseconds between moves
        self.lastMoveTime = 0
        self.nextDirection = self.direction

    def square(self, x, y):
        return pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)

    def draw(self, screen):
        pygame.draw.rect(screen, "white", self.square(self.head[0], self.head[1]), 2)
        for segment in self.body:
            pygame.draw.rect(screen, "white", self.square(segment[0], segment[1]), 2)

    def is_on(self, obj1, obj2):
        return obj1 == obj2

    def eat(self, food):
        if self.is_on(self.head, food):
            self.stomach.append(food)

    def grow(self, segment):
        self.body.append(segment)

    def digest(self):
        for food in self.stomach:
            if (food not in self.body) or food != self.head:
                self.grow(food)

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

    @property
    def position(self):
        return self.body + [self.head]
