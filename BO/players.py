from test2 import Pokemon


class players:

    id = 0
    name = ""
    money = 0
    score = 0
    playTime = 0
    pokemonsList = []

    def __init__(self):
        pass

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getMoney(self, money):
        return self.money

    def setMoney(self, money):
        self.money = money

    def getScore(self):
        return self.score

    def setScore(self, score):
        self.score = score

    def getPlayTime(self):
        return self.playTime

    def setPlayTime(self, playTime):
        self.playTime = playTime

    def getSprite(self):
        return None
