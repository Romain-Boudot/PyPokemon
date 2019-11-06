import pygame

class SpriteSheet:

    def __init__(self, filename):
        self.sheet = pygame.image.load(filename).convert_alpha()
        # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey = None):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert_alpha()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image