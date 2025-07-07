import pygame

class SquareShape(pygame.prite.Sprite):
    def __init__(self, x, y, size):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.size = size

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def collision(self, shape)
        distance = self.position.sitance_to(shape.position)
        if distance < selfe.radius + shape.radius:
            return True
        return False

    def ison(self, shape)
        if (self.x == shape.x) and (self.y == shape.y):
            return True
        return False