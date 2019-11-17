from BO.players import Player
from BO.menu import Menu

import time


class Game:

    print("Bonjour, je suis le professeur pokemon je m'appelle docteur Chen comment vous appelez-vous ? :")
    print()
    name = input()
    player = Player()
    player.setName(name)
    print()
    print("Enchantés {name}, bienvenue à Pokeland, un monde remplit de pokemon et de leurs drésseur, dans ce monde vous pourrez capturer toutes sortes de pokemons.".format(
        name=name))
    print()
    print("Je suppose que tu es venu pour choisir ton pokemon, tu es en retard .... suis-moi les pokemons sont à l'intérieur")
    time.sleep(4)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(2)
    print()
    print("Voici les pokeballs, laquelle prendras tu ?")
    print()
    data = ["bulbizarre", "salamèche", "carapuce"]
    choice = Menu.ShowQuestion("", data)

    if choice == 0:
        player.addPokemon("bulbizarre")
    elif choice == 1:
        player.addPokemon("salamèche")
    elif choice == 2:
        player.addPokemon("carapuce")

    print()
    print("Très bon choix ! Maintenant, tu es prêt pour l'aventure !")
    print()
    Menu.ShowMenu()
