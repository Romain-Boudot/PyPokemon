import sys, pygame, GameLogic
from pygame.locals import *
from GameLogic.player import Player
from GameLogic.tiles import Tile
from GameLogic.image import Image
from playgrounds.road1 import road1
from GameLogic.playgrounds import Playground

class Game:

    FPS = 40

    def __init__(self):
        self.window = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()

        self.player = Player(0)
        # image = Image("sprites/r1.png", 7, 12)
        
        self.world = pygame.sprite.Group()
        # self.menu = pygame.sprite.Group()
        # self.bag = pygame.sprite.Group()
        # self.fight = pygame.sprite.Group()

        self.playground = Playground(road1)

        # self.world.add(image)
        self.world.add(self.player)

    def run(self):
        done = False
        runKeyDown = False
        dirKeys = []
        while not done:
            for event in pygame.event.get():

                if event.type == QUIT:
                    done = True

                elif event.type == KEYDOWN:

                    if event.key == K_LSHIFT:
                        runKeyDown = True

                    elif event.key == K_DOWN or event.key == K_RIGHT or event.key == K_UP or event.key == K_LEFT:
                        dirKeys.append(event.key)

                elif event.type == KEYUP:

                    if event.key == K_LSHIFT:
                        runKeyDown = False

                    elif event.key == K_DOWN or event.key == K_RIGHT or event.key == K_UP or event.key == K_LEFT:
                        dirKeys.remove(event.key)
            
            if len(dirKeys) == 0:
                self.player.stand()
            else:
                lastKey = dirKeys[len(dirKeys) - 1]
                if lastKey == K_LEFT:     self.player.left()
                elif lastKey == K_RIGHT:  self.player.right()
                elif lastKey == K_UP:     self.player.back()
                elif lastKey == K_DOWN:   self.player.front()
                if runKeyDown:
                    self.player.run()
                else:
                    self.player.walk()

            # update sprites, draw 'em and refresh the screen
            self.player.preUpdate()
            self.world.update(self.player.getPos())
            self.playground.update(self.player.getPos())
            self.window.fill((0, 0, 0))
            self.world.draw(self.window)
            self.playground.draw(self.window)
            pygame.display.flip()

            # limit the frame rate at FPS/s
            self.clock.tick(Game.FPS)