from BO.pokemons import Pokemon
import GameLogic

class Player:

    # genders
    MALE = 0
    FEMALE = 1

    id = 0
    gender = 0
    name = "unset"
    money = 0
    score = 0
    playTime = 0
    team = []
    sprite = None

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.sprite = GameLogic.player.Player(self)

    def getTeam(self):          return self.team

    def getId(self):            return self.id
    # def setId(self, id):        self.id = id
    
    def getName(self):          return self.name
    def setName(self, name):    self.name = name
    
    def getMoney(self, money):  return self.money
    def setMoney(self, money):  self.money = money
    
    def getScore(self):         return self.score
    def setScore(self, score):  self.score = score
    
    def getPlayTime(self):      return self.playTime
    # def setPlayTime(self, playTime): self.playTime = playTime

    def getSprite(self):        return None