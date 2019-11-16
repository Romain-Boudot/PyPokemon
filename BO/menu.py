# from BO.players import players

import time


class Menu:
    @staticmethod
    def ShowQuestion(sentance, responses):
        answer = 0
        while answer < 1 or answer > len(responses) or answer != int(answer):
            for i in range(len(responses)):
                print("{index}  {data}".format(index=i+1, data=responses[i]))
            print(sentance)
            answer = int(input())
        return answer - 1

    @staticmethod
    def switch(argument):
        switcher = {
            1: "1",
            2: "2",
            3: "3",
            4: ShowPlayerMenu(),
        }
        return switcher.get(argument)

    @staticmethod
    def ShowMenu():
        choice = 0

        while choice < 1 or choice > 5:
            print("# ----------MENU-----------")
            print("# 1 - Hautes Herbes")
            print("# 2 - magasin")
            print("# 3 - Pokedex")
            print("# 4 - A propos de moi")
            print("# 5 - Quitter")
            print("Veuiller entrer votre choix :")
            choice = int(input())

        if choice == 1:
            print("1")
        elif choice == 2:
            print("2")
        elif choice == 3:
            print("3")
        elif choice == 4:
            print("4")
        elif choice == 5:
            print("A bientôt")
        else:
            switch(choice)

    @staticmethod
    def ShowPlayerMenu():
        choice = 0
        while choice < 1 or choice > 3:
            print("# ----------Plus d'infos sur moi-----------")
            print("# 1 - Mes pokemons")
            print("# 2 - mon identite")
            print("# 3 - retour")
            print("Veuiller entrer votre choix :")
            choice = int(input())

        if choice == 1:
            print("1")
        elif choice == 2:
            print("2")
        else:
            ShowMenu()

    @staticmethod
    def IdentityCard():

        # player = players()

        name = "camille"
        nbPokemon = 15
        money = 500
        score = 100

        print("#############################################")
        print("#         Carte d'identite du joueur        #")
        print("#############################################")
        print("# - Nom : {name}".format(name=name))
        print("#-------------------------------------------")
        print(
            "# - Nombre de pokemon : {nbPokemon}".format(nbPokemon=nbPokemon))
        print("#-------------------------------------------")
        print(
            "# - monaie : {money}".format(money=money))
        print("#-------------------------------------------")
        print(
            "# - score : {score}".format(score=score))
        print("#############################################")


# player = players()
Menu.IdentityCard()
print("Bonjour, je suis le professeur pokemon je m'appelle docteur Chen qui êtes vous ? :")
print()
name = input()
# player.setName(name)
print()
print("Enchantés {name}, bienvenue à Pokeland, un monde remplit de pokemon et de leurs drésseur, dans ce monde vous pourrez capturer toutes sortes de pokemons.".format(
    name=name))
print()
print("Je suppose que tu es venu pour choisir ton pokemon, tu es en retard .... suis-moi les pokemons sont à l'intérieur")
time.sleep(7)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")
time.sleep(2)
print()
print("Voici les pokeballs, laquelle prendras tu ?")
print()
data = ["bulbizard", "salamèche", "carapuce"]
Menu.ShowQuestion("", data)
print()
print("Très bon choix ! Maintenant, tu es prêt pour l'aventure !")
print()
Menu.ShowMenu()
