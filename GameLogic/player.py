import pygame
from BO.players import Player as BoPlayer
from GameLogic.spriteSheet import SpriteSheet
from utils import tupleAddition

class Player(pygame.sprite.DirtySprite):

    MALE_WALK_SPRITE = "sprites/male_walk.png"
    MALE_RUN_SPRITE = "sprites/male_run.png"
    FEMALE_WALK_SPRITE = "sprites/female_walk.png"
    FEMALE_RUN_SPRITE = "sprites/female_run.png"

    STAT_STAND = 0
    STAT_WALK = 1
    STAT_RUN = 2
    DIR_FRONT = 0
    DIR_BACK = 1
    DIR_LEFT = 2
    DIR_RIGHT = 3

    BASE  = (0, 0, 16, 32)

    FRONT = (0, 0, 0, 0)
    SIDE  = (0, 64, 0, 0)
    BACK  = (0, 32, 0, 0)

    MIDDLE = (16, 0, 0, 0)
    LEFT  = (0, 0, 0, 0)
    RIGHT = (32, 0, 0, 0)

    def __init__(self, gender):
        self.gender = gender

        pygame.sprite.Sprite.__init__(self)

        if gender == BoPlayer.MALE:
            self.walkSrpiteSheet = SpriteSheet(Player.MALE_WALK_SPRITE)
            self.runSrpiteSheet = SpriteSheet(Player.MALE_RUN_SPRITE)
        else:
            self.walkSrpiteSheet = SpriteSheet(Player.FEMALE_WALK_SPRITE)
            self.runSrpiteSheet = SpriteSheet(Player.FEMALE_RUN_SPRITE)
        
        # dirs
        #        (y)
        #        -1
        # (x) -1 +0 +1
        #        +1
        # (x, y)
        self.dir = self.DIR_FRONT

        # stats
        # 0 : stand
        # 1 : walk
        # 2 : run
        self.stat = self.STAT_STAND

        self.update()
        self.rect = self.image.get_rect()
        self.rect.left = 311
        self.rect.top = 220

    def update(self, *args, **kwargs):
        # list of tuple to addition to cut the right sprite in the sprite sheet
        flagList = [self.BASE]
        # the sprite sheet to cut in
        spriteSheet = self.walkSrpiteSheet

        if self.stat == self.STAT_STAND or self.stat == self.STAT_RUN:
            flagList.append(self.MIDDLE)
        elif self.stat == self.STAT_RUN + self.STAT_WALK:
            spriteSheet = self.runSrpiteSheet

        # be default character is front side
        if self.dir == self.DIR_BACK:
            flagList.append(self.BACK)
        elif self.dir >= self.DIR_LEFT: # if >= DIR_LEFT then it means the player is on the left or right side
            flagList.append(self.SIDE)

        print(flagList)
        image = spriteSheet.image_at(tupleAddition(flagList))
        self.image = pygame.transform.flip(image, False, True) if self.dir == self.DIR_RIGHT else image

    def stand(self): self.stat = self.STAT_STAND
    def walk(self): self.stat += self.STAT_WALK
    def run(self): self.stat += self.STAT_RUN
    def stopRun(self): self.stat -= self.STAT_RUN

    def front(self): self.dir = self.DIR_FRONT
    def back(self): self.dir = self.DIR_BACK
    def left(self): self.dir = self.DIR_LEFT
    def right(self): self.dir = self.DIR_RIGHT