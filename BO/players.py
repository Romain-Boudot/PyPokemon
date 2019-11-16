#from test2 import Pokemon


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

    def getMyPokemons(self):
        return self.pokemonsList

    def addPokemon(self, pokemon):
        if len(self.pokemonsList) < 6:
            self.pokemonsList.append(pokemon)
        else:
            print("Vous avez atteint la capacité maximal")

    def removePokemon(self, pokemon):
        if len(self.pokemonsList) > 1:
            try:
                self.pokemonsList.remove(pokemon)
            except:
                pass
                #print("Vous ne posséder pas ce pokemon")
        else:
            print("Vous ne pouvez pas combatre sans pokemon")

    @staticmethod
    def IdentityCard(self):
        print("#############################################")
        print("#         Carte d'identite du joueur        #")
        print("#############################################")
        print("# - Nom : {name}".format(name=self.name))
        print("#-------------------------------------------")
        print(
            "# - Nombre de pokemon : {nbPokemon}".format(nbPokemon=len(self.pokemonsList)))
        print("#-------------------------------------------")
        print(
            "# - monaie : {money}".format(money=self.money))
        print("#-------------------------------------------")
        print(
            "# - score : {score}".format(score=self.score))
        print("#############################################")
