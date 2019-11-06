import sys, pygame
from pygame.locals import *
from GameLogic.player import Player

class Game:

    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()
        self.player = Player(0)
        self.sprites = pygame.sprite.Group()
        self.dirKeyDown = 0

        self.sprites.add(self.player)

        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == QUIT:
                    done = True
                elif event.type == KEYDOWN:
                    if event.key == K_LSHIFT:
                        self.player.run()
                    elif event.key == K_DOWN or event.key == K_RIGHT or event.key == K_UP or event.key == K_DOWN:
                        self.dirKeyDown += 1
                        self.player.walk()
                        if event.type == K_DOWN:    self.player.left()
                        elif event.type == K_RIGHT: self.player.right()
                        elif event.type == K_UP:    self.player.back()
                        elif event.type == K_DOWN:  self.player.front()
                elif event.type == KEYUP:
                    if event.key == K_LSHIFT:
                        self.player.stopRun()
                    elif event.key == K_DOWN or event.key == K_RIGHT or event.key == K_UP or event.key == K_DOWN:
                        self.dirKeyDown -= 1
                    if self.dirKeyDown == 0:
                        self.player.stand()

            self.sprites.update()
            self.sprites.draw(self.window)
            pygame.display.flip()