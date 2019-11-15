import pygame
from GameLogic.spriteSheet import SpriteSheet

class Tile(pygame.sprite.DirtySprite):
    
    # tiles types
    SIMPLE = 0
    MULTIPLE = 1
    ANIMATED = 2
    PARTIAL_ANMATION = 3

    # tiles rects
    WATER = {
        "type": MULTIPLE,
        "rects": [
            (171, 1, 16, 16),
            (188, 1, 16, 16),
            (205, 1, 16, 16),
            (171, 18, 16, 16),
            (188, 18, 16, 16),
            (205, 18, 16, 16),
            (171, 35, 16, 16),
            (188, 35, 16, 16),
            (205, 35, 16, 16)
        ]
    }

    FLOWER = {
        "type": ANIMATED,
        "rects": [
            (89, 36, 16, 16),
            (105, 36, 16, 16),
            (121, 36, 16, 16),
            (137, 36, 16, 16),
            (153, 36, 16, 16)
        ]
    }

    FLOOR_GRASS = {
        "type": MULTIPLE,
        "rects": [
            (103, 1, 16, 16),
            (120, 1, 16, 16),
            (103, 18, 16, 16),
            (120, 18, 16, 16)
        ]
    }

    POKEBALL = {
        "type": SIMPLE,
        "rect": (137, 18, 16, 16)
    }

    POKE_CENTER = {
        "type": SIMPLE,
        "rect": (488, 0, 80, 80)
    }

    POKE_SHOP = {
        "type": SIMPLE,
        "rect": (575, 11, 64, 64)
    }

    GYM = {
        "type": SIMPLE,
        "rect": (486, 101, 112, 80)
    }

    SINGLE_DOOR = {
        "type": PARTIAL_ANMATION,
        "rects": [
            (0, 0, 0, 0),
            (503, 82, 16, 16),
            (520, 82, 16, 16),
            (537, 82, 16, 16)
        ]
    }

    DOUBLE_DOOR = {
        "type": PARTIAL_ANMATION,
        "rects": [
            (0, 0, 0, 0),
            (120, 312, 16, 16),
            (137, 312, 16, 16),
            (154, 312, 16, 16)
        ]
    }

    BIG_TREE = {
        "type": SIMPLE,
        "rect": (236, 292, 32, 48)
    }

    TALL_TREE = {
        "type": SIMPLE,
        "rect": (216, 292, 16, 48)
    }

    LITTLE_TREE = {
        "type": SIMPLE,
        "rect": (235, 340, 16, 32)
    }

    ROAD_VILLAGE = {
        "Type": MULTIPLE,
        "rects": [
            (1, 1, 16, 16),
            (18, 1, 16, 16),
            (35, 1, 16, 16),
            (52, 1, 16, 16),
            (69, 1, 16, 16),
            (18, 18, 16, 16),
            (35, 18, 16, 16),
            (52, 18, 16, 16),
            (69, 18, 16, 16),
            (18, 35, 16, 16),
            (35, 35, 16, 16),
            (52, 35, 16, 16),
            (69, 35, 16, 16)
        ]
    }

    ROAD_DIRT = {
        "Type": MULTIPLE,
        "rects": [
            (1, 103, 16, 16),
            (18, 103, 16, 16),
            (35, 103, 16, 16),
            (52, 103, 16, 16),
            (69, 103, 16, 16),
            (18, 120, 16, 16),
            (35, 120, 16, 16),
            (52, 120, 16, 16),
            (69, 120, 16, 16),
            (18, 137, 16, 16),
            (35, 137, 16, 16),
            (52, 137, 16, 16),
            (69, 137, 16, 16)
        ]
    }

    ROAD_GRASS = {
        "Type": MULTIPLE,
        "rects": [
            (1, 52, 16, 16),
            (18, 52, 16, 16),
            (35, 52, 16, 16),
            (52, 52, 16, 16),
            (69, 52, 16, 16),
            (18, 69, 16, 16),
            (35, 69, 16, 16),
            (52, 69, 16, 16),
            (69, 69, 16, 16),
            (18, 86, 16, 16),
            (35, 86, 16, 16),
            (52, 86, 16, 16),
            (69, 86, 16, 16)
        ]
    }

    ROAD_SOLID = {
        "Type": MULTIPLE,
        "rects": [
            (1, 205, 16, 16),
            (18, 205, 16, 16),
            (35, 205, 16, 16),
            (52, 205, 16, 16),
            (69, 205, 16, 16),
            (18, 222, 16, 16),
            (35, 222, 16, 16),
            (52, 222, 16, 16),
            (69, 222, 16, 16),
            (18, 239, 16, 16),
            (35, 239, 16, 16),
            (52, 239, 16, 16),
            (69, 239, 16, 16)
        ]
    }

    JUMPS = {
        "type": MULTIPLE,
        "rects": [
            (137, 103, 16, 16),
            (120, 120, 16, 16),
            (137, 120, 16, 16),
            (103, 137, 16, 16),
            (120, 137, 16, 16),
            (137, 137, 16, 16),
            (103, 154, 16, 16),
            (120, 154, 16, 16),
            (137, 154, 16, 16)
        ]
    }

    LONG_GRASS = {
        "type": SIMPLE,
        "rect": (137, 1, 16, 16)
    }

    def __init__(self, obj, offesetX, offesetY, index = 0):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = SpriteSheet("sprites/tileset2.png")
        self.origin = (offesetX, offesetY)

        if obj["type"] == Tile.SIMPLE:
            self.image = self.sprite.image_at(obj["rect"])
        elif obj["type"] == Tile.ANIMATED or obj["type"] == Tile.PARTIAL_ANMATION:
            self.image = self.sprite.image_at(obj["rects"][0])
        elif obj["type"] == Tile.MULTIPLE:
            self.image = self.sprite.image_at(obj["rects"][index])
        
        self.rect = self.image.get_rect()
        self.rect.left = offesetX
        self.rect.top = offesetY - self.rect.y

    def update(self, *args, **kwargs):
        self.rect.left = self.origin[0] - args[0][0]
        self.rect.top = self.origin[1] - args[0][1]