from random import choice, randint

class GameCtx:

    def getRandomPokemonLevel(self):
        return choice(range(5, 8))

    def genRadomIV(self):
        return {
            "speed": randint(0, 31),
            "special-defense": randint(0, 31),
            "special-attack": randint(0, 31),
            "defense": randint(0, 31),
            "attack": randint(0, 31),
            "hp": randint(0, 31)
        }