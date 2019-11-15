import pygame
from GameLogic.spriteSheet import SpriteSheet

class Image(pygame.sprite.DirtySprite):

    def __init__(self, url, offesetX, offesetY):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = SpriteSheet(str(url))

        self.origin = (offesetX, offesetY)

        self.image = pygame.image.load(url).convert()
        self.rect = self.image.get_rect()
        self.rect.left = offesetX
        self.rect.top = offesetY

    def update(self, *args, **kwargs):
        self.rect.left = self.origin[0] - args[0][0]
        self.rect.top = self.origin[1] - args[0][1]