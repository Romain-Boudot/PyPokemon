from BO.players import Player
from BO.menu import Menu

import time


print("Bonjour, je suis le professeur pokemon je m'appelle docteur Chen qui êtes vous ? :")
print()
name = input()
player = Player(1, name)
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
