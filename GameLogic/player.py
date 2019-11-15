import pygame, GameLogic
from BO.players import Player as BoPlayer
from utils import tupleAddition

class Player(pygame.sprite.DirtySprite):

    MALE_WALK_SPRITE = "sprites/male_walk.png"
    MALE_RUN_SPRITE = "sprites/male_run.png"
    FEMALE_WALK_SPRITE = "sprites/female_walk.png"
    FEMALE_RUN_SPRITE = "sprites/female_run.png"

    WALK_TIME = 400 # ms
    RUN_TIME  = 200 # ms
    TURN_TIME = 100 # ms

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
        pygame.sprite.Sprite.__init__(self)

        self.updates = 0
        self.nextUpdate = 0

        self.pos = [0, 0]

        self.frameDuration = 1000 / GameLogic.game.Game.FPS # is ms

        if gender == BoPlayer.MALE:
            self.walkSrpiteSheet = GameLogic.spriteSheet.SpriteSheet(Player.MALE_WALK_SPRITE)
            self.runSrpiteSheet = GameLogic.spriteSheet.SpriteSheet(Player.MALE_RUN_SPRITE)
        else:
            self.walkSrpiteSheet = GameLogic.spriteSheet.SpriteSheet(Player.FEMALE_WALK_SPRITE)
            self.runSrpiteSheet = GameLogic.spriteSheet.SpriteSheet(Player.FEMALE_RUN_SPRITE)
        
        # dir
        self.dir = Player.DIR_FRONT
        self.lastDir = None

        # stats
        self.stat = Player.STAT_STAND
        self.lastStat = None

        self.update()
        self.rect = self.image.get_rect()
        self.rect.left = 311
        self.rect.top = 220

    def preUpdate(self):
        if self.updates >= self.nextUpdate:
            if self.lastDir != self.dir and self.lastStat == Player.STAT_STAND:
                self.nextUpdate = self.updates + (Player.TURN_TIME / self.frameDuration) # wait for TURN_TIME ms
                self.stat = Player.STAT_STAND
            else:
                if self.stat == Player.STAT_WALK:
                    self.nextUpdate = self.updates + (Player.WALK_TIME / self.frameDuration) # wait for WALK_TIME ms
                elif self.stat == Player.STAT_RUN:
                    self.nextUpdate = self.updates + (Player.RUN_TIME / self.frameDuration) # wait for RUN_TIME ms
        
        if self.stat != Player.STAT_STAND:
            if self.stat == Player.STAT_RUN:
                inc = 16 / (Player.RUN_TIME / self.frameDuration)
            elif self.stat == Player.STAT_WALK:
                inc = 16 / (Player.WALK_TIME / self.frameDuration)
            self.pos[0 if self.dir >= Player.DIR_LEFT else 1] += inc if self.dir == Player.DIR_RIGHT or self.dir == Player.DIR_FRONT else -inc

    def update(self, *args, **kwargs):

        self.updates += 1

        # list of tuple to addition to cut the right sprite in the sprite sheet
        flagList = [Player.BASE]
        # the sprite sheet to cut in
        spriteSheet = self.walkSrpiteSheet

        if self.stat == Player.STAT_STAND:
            flagList.append(Player.MIDDLE)
        else:
            _temp = self.pos[0]%16 + self.pos[1]%16
            if _temp > 8 and _temp <= 12:
                flagList.append(Player.RIGHT)
            elif _temp > 4 or _temp > 12:
                flagList.append(Player.MIDDLE)
            if self.stat == Player.STAT_RUN:
                spriteSheet = self.runSrpiteSheet

        """ LLLLL MMM RRRRR MMM  """

        # be default character is front side
        if self.dir == Player.DIR_BACK:
            flagList.append(Player.BACK)
        elif self.dir >= Player.DIR_LEFT: # if >= DIR_LEFT then it means the player is on the left or right side
            flagList.append(Player.SIDE)

        image = spriteSheet.image_at(tupleAddition(flagList))
        self.image = pygame.transform.flip(image, True, False) if self.dir == Player.DIR_RIGHT else image
        
        self.lastDir = self.dir
        self.lastStat = self.stat

    def canChangeStat(self):
        return self.updates >= self.nextUpdate

    def stand(self):
        if self.canChangeStat(): self.stat = Player.STAT_STAND
    def walk(self):
        if self.canChangeStat(): self.stat = Player.STAT_WALK
    def run(self):
        if self.canChangeStat(): self.stat = Player.STAT_RUN

    def front(self):
        if self.canChangeStat(): self.dir = Player.DIR_FRONT
    def back(self):
        if self.canChangeStat(): self.dir = Player.DIR_BACK
    def left(self):
        if self.canChangeStat(): self.dir = Player.DIR_LEFT
    def right(self):
        if self.canChangeStat(): self.dir = Player.DIR_RIGHT

    def getPos(self):
        return self.pos