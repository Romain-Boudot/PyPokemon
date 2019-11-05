from DataHolder import DataHolder
from GameEnv import Env
from BO.types import Type
from BO.GameCtx import GameCtx
import random

class Pokemon:

    # genders
    NONE = -1
    MALE = 0
    FEMALE = 1

    pokemonData = {}
    speciesData = {}
    levels = []
    level = 0
    experience = 0
    type1 = None
    type2 = None
    stats = []
    fightStats = []
    maxHp = 0
    hp = 0
    moves = {}

    def __init__(self, creationData, GameCtx: GameCtx):
        if creationData is int:
            self.pokemonData = DataHolder.get("https://pokeapi.co/api/v2/pokemon/%d/" % creationData)
            self.speciesData = DataHolder.get("https://pokeapi.co/api/v2/pokemon-species/%d/" % creationData)
        elif creationData is str:
            self.pokemonData = DataHolder.get(creationData)
            self.speciesData = DataHolder.get(self.pokemonData['species']['url'])
        self.level = GameCtx.getRandomPokemonLevel()
        self.updateStats(True)

        def updateStats(self, firstUpdate = False):
            self.levels = DataHolder.get(self.speciesData['growth_rate']['url'])['levels']
            self.experience = next(level for level in self.levels if level['level'] == self.level)['experience']
            self.type1 = Type(next(type for type in self.pokemonData['types'] if type['slot'] == 1)['type']['url'])
            self.type2 = Type(next(type for type in self.pokemonData['types'] if type['slot'] == 2)['type']['url'])
            self.stats = {
                'speed': next(stat for stat in self.pokemonData['stats'] if stat['stat']['name'] == 'speed'),
                'special-defense': next(stat for stat in self.pokemonData['stats'] if stat['stat']['name'] == 'special-defense'),
                'special-attack': next(stat for stat in self.pokemonData['stats'] if stat['stat']['name'] == 'special-attack'),
                'defense': next(stat for stat in self.pokemonData['stats'] if stat['stat']['name'] == 'defense'),
                'attack': next(stat for stat in self.pokemonData['stats'] if stat['stat']['name'] == 'attack')
            }
            self.fightStats = { 'speed': 0, 'special-defense': 0, 'special-attack': 0, 'defense': 0, 'attack': 0 }
            self.maxHp = next(stat for stat in self.pokemonData['stats'] if stat['stat']['name'] == 'hp')
            if firstUpdate: 
                self.level = GameCtx.getRandomPokemonLevel()
                self.hp = self.maxHp
                self.gender = Pokemon.NONE if self.speciesData['gender_rate'] == -1 else Pokemon.FEMALE if random.randint(0, 8) < self.speciesData['gender_rate'] else Pokemon.MALE

        def getMaxHp(self): return self.maxHp
        def getHp(self): return self.hp
        def getSpeed(self): return self.stats['speed'] + self.fightStats['speed']
        def getSpecialDefense(self): return self.stats['special-defense'] + self.fightStats['special-defense']
        def getSpecialAttack(self): return self.stats['special-attack'] + self.fightStats['special-attack']
        def getDefense(self): return self.stats['defense'] + self.fightStats['defense']
        def getAttack(self): return self.stats['attack'] + self.fightStats['attack']
        def getLevel(self): return self.level
        def getGender(self): return self.gender
