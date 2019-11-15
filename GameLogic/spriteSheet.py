import pygame

class SpriteSheet:

    def __init__(self, filename):
        self.sheet = pygame.image.load(filename).convert_alpha()
        # Load a specific image from a specific rectangle

    def image_at(self, rectangle, colorkey = -1):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert_alpha()
        image.blit(self.sheet, (0, 0), rect)
        image.set_colorkey((163, 73, 164), pygame.RLEACCEL)
        return image