# from test2 import Pokemon


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
    pokemonsList = []

    # def __init__(self, id, name):
    #    self.id = id
    #    self.name = name

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getMoney(self):
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
        return self.pokemonsList[0]

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
                # print("Vous ne posséder pas ce pokemon")
        else:
            print("Vous ne pouvez pas combatre sans pokemon")

    def showMyPokemons(self):
        print("#############################################")
        print("#                Mes pokemons               #")
        print("#############################################")
        for i in range(len(self.pokemonsList)):
            print("# {index} : {pokemon}".format(
                index=i+1, pokemon=self.pokemonsList[i]))
        print("#############################################")

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
