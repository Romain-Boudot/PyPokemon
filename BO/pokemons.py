from DataHolder import DataHolder
from GameEnv import Env
from BO.types import Type
from BO.gameCtx import GameCtx
import random, math

class Pokemon:

    # genders
    NOSEX = -1
    MALE = 0
    FEMALE = 1

    fightStatModificatorsBasicStats = [.25, .29, .33, .4, .5, .67, 1, 1.5, 2, 2.5, 3, 3.5, 4]
    fightStatModificatorsExtendedStats = [.33, .38, .43, .5, .6, .73, 1, 1.33, 1.67, 2, 2.33, 2.67, 3]

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
    iv = {}

    def __init__(self, creationData, ctx: GameCtx):
        if creationData is int:
            self.pokemonData = DataHolder.get("https://pokeapi.co/api/v2/pokemon/%d/" % creationData)
            self.speciesData = DataHolder.get("https://pokeapi.co/api/v2/pokemon-species/%d/" % creationData)
        elif creationData is str:
            self.pokemonData = DataHolder.get(creationData)
            self.speciesData = DataHolder.get(self.pokemonData['species']['url'])
        
        self.level = ctx.getRandomPokemonLevel()
        self.captureRate = self.speciesData['capture_rate']
        self.level = ctx.getRandomPokemonLevel()
        self.hp = self.maxHp
        self.gender = Pokemon.NOSEX if self.speciesData['gender_rate'] == -1 else Pokemon.FEMALE if random.randint(0, 8) < self.speciesData['gender_rate'] else Pokemon.MALE
        self.iv = ctx.genRadomIV()

        self.levels = DataHolder.get(self.speciesData['growth_rate']['url'])['levels']
        self.experience = next(level for level in self.levels if level['level'] == self.level)['experience']
        self.type1 = Type(next(type for type in self.pokemonData['types'] if type['slot'] == 1)['type']['url'])
        self.type2 = Type(next(type for type in self.pokemonData['types'] if type['slot'] == 2)['type']['url'])
        self.stats = {
            'speed':            next(stat for stat in self.pokemonData['stats'] if stat['stat']['name'] == 'speed'),
            'special-defense':  next(stat for stat in self.pokemonData['stats'] if stat['stat']['name'] == 'special-defense'),
            'special-attack':   next(stat for stat in self.pokemonData['stats'] if stat['stat']['name'] == 'special-attack'),
            'defense':          next(stat for stat in self.pokemonData['stats'] if stat['stat']['name'] == 'defense'),
            'attack':           next(stat for stat in self.pokemonData['stats'] if stat['stat']['name'] == 'attack'),
            'hp':               next(stat for stat in self.pokemonData['stats'] if stat['stat']['name'] == 'hp')
        }
        self.fightStats = { 'speed': 6, 'special-defense': 6, 'special-attack': 6, 'defense': 6, 'attack': 6, 'accuracy': 6, 'dodge': 6 }
        self.updateStats()
        self.hp = self.maxHp

    def updateStats(self):
        for stat in self.stats.keys():
            base = self.stats[stat]['base_stat']
            iv = iv[stat]
            ev = self.stats[stat]['effort']
            if stat == 'hp':
                self.maxHp = (((base + iv) * 2 + (math.sqrt(ev) / 4)) * self.level) / 100 + self.level + 10
            else:
                self.stats[stat]['stat'] = (((base + iv) * 2 + (math.sqrt(ev) / 4)) * self.level) / 100 + 5
            
    def gainExp(self, exp):
        self.experience += exp
        nextLevelExp = next(level for level in self.levels if level['level'] == self.level + 1)['experience']
        if self.experience > nextLevelExp:
            self.level += 1
            self.updateStats()
            self.gainExp(0) # making sure we passed all the levels

    def resetFightStat(self):       self.fightStats = { 'speed': 6, 'special-defense': 6, 'special-attack': 6, 'defense': 6, 'attack': 6, 'accuracy': 6, 'dodge': 6 }
    def getMaxHp(self):             return self.maxHp
    def getHp(self):                return self.hp
    def getSpeed(self):             return self.stats['speed']['stat'] * self.fightStatModificatorsBasicStats[self.fightStats['speed']]
    def getSpecialDefense(self):    return self.stats['special-defense']['stat'] * self.fightStatModificatorsBasicStats[self.fightStats['special-defense']]
    def getSpecialAttack(self):     return self.stats['special-attack']['stat'] * self.fightStatModificatorsBasicStats[self.fightStats['special-attack']]
    def getDefense(self):           return self.stats['defense']['stat'] * self.fightStatModificatorsBasicStats[self.fightStats['defense']]
    def getAttack(self):            return self.stats['attack']['stat'] * self.fightStatModificatorsBasicStats[self.fightStats['attack']]
    def getAccuracy(self):          return self.fightStatModificatorsExtendedStats[self.fightStats['accuracy']]
    def getDodge(self):             return self.fightStatModificatorsExtendedStats[self.fightStats['dodge']]
    def getLevel(self):             return self.level
    def getGender(self):            return self.gender