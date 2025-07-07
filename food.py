import random
import pygame
from constants import *

class Food:
    def __init__(self, valid_coords):
        self._position = random.choice(valid_coords)

    def square(self, x, y):
        return pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)

    def draw(self, screen):
        pygame.draw.rect(screen, "red", self.square(self.position[0], self.position[1]))

    @property
    def position(self):
        return self._position
