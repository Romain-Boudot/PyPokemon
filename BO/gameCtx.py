from random import choice, randint

class GameCtx:

    @staticmethod
    def getRandomPokemonLevel():
        return choice(range(50, 55))

    @staticmethod
    def genRadomIV():
        return {
            "speed": randint(0, 31),
            "special-defense": randint(0, 31),
            "special-attack": randint(0, 31),
            "defense": randint(0, 31),
            "attack": randint(0, 31),
            "hp": randint(0, 31)
        }

    @staticmethod
    def getRandomPokemonId():
        return choice(range(1, 150))