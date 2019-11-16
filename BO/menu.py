from random import randint
from BO.players import players

import time


def ShowQuestion(data):
    answer = 0
    while answer < 1 or answer > len(data) or answer != int(answer):
        for i in range(len(data)):
            print("{index}  {data}".format(index=i+1, data=data[i]))
        print("Veuiller entrer votre choix :")
        answer = int(input())
    return answer-1


def switch(argument):
    switcher = {
        1: "1",
        2: "2",
        3: "3",
        4: ShowPlayerMenu(),
    }
    return switcher.get(argument)


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


def IdentityCard():
    print("--------------------------------------------")
    print("- Nom : {name} ")
    print("- ")
    print("-")
    print("-")
    print("-")
    print("--------------------------------------------")


class Game:

    player = players()

    print("Bonjour, je suis le professeur pokemon je m'appelle docteur Chen qui êtes vous ? :")
    print()
    name = input()
    player.setName(name)
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
    ShowQuestion(data)
    print()
    print("Très bon choix ! Maintenant, tu es prêt pour l'aventure !")
    print()
    ShowMenu()
