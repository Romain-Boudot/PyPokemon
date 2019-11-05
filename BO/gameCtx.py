from random import choice

class GameCtx:

    # def __init__(self):
        
    @staticmethod
    def getRandomPokemonLevel():
        return choice(range(5, 8))