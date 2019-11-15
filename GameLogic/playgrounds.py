import pygame, GameLogic

class Playground():

    def __init__(self, road):
        self.road = road
        self.group = pygame.sprite.Group()
        for tile in road:
            for pos in tile[1]:
                sprite = GameLogic.tiles.Tile(tile[0], pos[0] * 16, pos[1] * 16)
                self.group.add(sprite)

    def update(self, pos): self.group.update(pos)
    def draw(self, window): self.group.draw(window)