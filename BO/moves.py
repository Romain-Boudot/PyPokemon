from DataHolder import DataHolder
from GameEnv import Env
from types import Type

class Move:

    data = {}
    type = None
    pp = 0

    def __init__(self, id: int):
        self.data   = DataHolder.get("https://pokeapi.co/api/v2/move/%d/" % id)
        self.init()

    def __init__(self, url: str):
        self.data = DataHolder.get(url)
        self.init()

    def init(self):
        self.type   = Type(self.data['type']['url'])
        self.pp     = self.data['pp']

    def getDisplayName(self):
        for name in self.data['names']:
            if name['language']['name'] == Env.loc:
                return name['name']

    def getType(self):
        return self.type

    def getMaxPP(self):
        return self.data['pp']

    def getPP(self):
        return self.pp

    def addPP(self, amount):
        self.pp += amount

    def setFullPP(self):
        self.pp = self.data['pp']

    def getAccuracy(self):
        return self.data['accuracy']

    def getPower(self):
        return self.data['power']

    def getEffects(self):
        return self.data['effect_changes']

    def getCritRate(self):
        return self.data['meta']['crit_rate']

    def getDrain(self):
        return self.data['meta']['drain']

    def getFlinchChance(self):
        return self.data['meta']['flinch_chance']
    
    def getHealing(self):
        return self.data['meta']['healing']

    def getMaxHits(self):
        return self.data['meta']['max_hits']

    def getMaxTurn(self):
        return self.data['meta']['max_turns']

    def getMinHits(self):
        return self.data['meta']['min_hits']

    def getMinTurns(self):
        return self.data['meta']['min_turns']

    def getStatChance(self):
        return self.data['meta']['stat_chance']

    def getName(self):
        return self.data['name']

    def getTarget(self):
        return self.data['target']['name']