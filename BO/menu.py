from BO.players import Player
from BO.fights import Fight
from BO.pokemons import Pokemon
from BO.pokemonInfo import PokemonInfo

import time


class Menu:

    @staticmethod
    def ShowQuestion(sentance, responses):
        answer = 0
        while answer < 1 or answer > len(responses) or answer != int(answer):
            # os clear
            Menu.display(sentance)
            for i in range(len(responses)):
                Menu.display("{index}  {data}".format(
                    index=i+1, data=responses[i]))
            answer = int(input())
        return answer - 1

    @staticmethod
    def display(string):
        string = str(string)
        string = string.replace("[normal]", "\033[38;2;168;167;122m")
        string = string.replace("[fire]", "\033[38;2;238;129;48m")
        string = string.replace("[water]", "\033[38;2;99;144;240m")
        string = string.replace("[electric]", "\033[38;2;247;208;44m")
        string = string.replace("[grass]", "\033[38;2;122;199;76m")
        string = string.replace("[ice]", "\033[38;2;150;217;214m")
        string = string.replace("[fighting]", "\033[38;2;194;46;40m")
        string = string.replace("[poison]", "\033[38;2;163;62;161m")
        string = string.replace("[ground]", "\033[38;2;226;191;101m")
        string = string.replace("[flying]", "\033[38;2;169;143;243m")
        string = string.replace("[psychic]", "\033[38;2;249;85;135m")
        string = string.replace("[bug]", "\033[38;2;166;185;26m")
        string = string.replace("[rock]", "\033[38;2;182;161;54m")
        string = string.replace("[ghost]", "\033[38;2;115;87;151m")
        string = string.replace("[dragon]", "\033[38;2;111;53;252m")
        string = string.replace("[dark]", "\033[38;2;112;87;70m")
        string = string.replace("[steel]", "\033[38;2;183;183;206m")
        string = string.replace("[fairy]", "\033[38;2;214;133;173m")
        string = string.replace("[r]", "\033[31m")
        string = string.replace("[g]", "\033[32m")
        string = string.replace("[y]", "\033[33m")
        string = string.replace("[b]", "\033[34m")
        string = string.replace("[p]", "\033[35m")
        string = string.replace("[]", "\033[0m")
        print(string)

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
            player = Player()
            # bulbizare 1
            # salameche 4
            # carapuce 7
            pokemon = player.getMyPokemons()
            if pokemon == "bulbizarre":
                Fight([Pokemon(1)])
            elif pokemon == "salamèche":
                Fight([Pokemon(4)])
            else:
                Fight([Pokemon(7)])
        elif choice == 2:
            print("non fonctionelle")
            Menu.ShowMenu()
        elif choice == 3:
            Menu.ShowInfoPokemon()
        elif choice == 4:
            Menu.ShowPlayerMenu()
        else:
            print("A bientôt")

    @staticmethod
    def ShowInfoPokemon():
        choice = 0
        while choice < 1 or choice > 3:
            print("# ----------Infos sur un pokemon-----------")
            print()
            print(
                "Pour avoir des informations sur un pokemon vous devez rentrer sont id")
            print(
                "ou sont nom en anglais en minuscule exemple bulbizarre = bulbasaur")
            print()
            print("Veuiller entrer votre choix :")
            choice = input()

            try:
                infoPokemon = PokemonInfo(
                    "https://pokeapi.co/api/v2/pokemon/{data}".format(data=choice))
                infoPokemon.DisplayInfoPokemon()
            except:
                print("données incorecte !!")
            print()
            choice = Menu.ShowQuestion("", ["retour"])
            if choice == 0:
                Menu.ShowMenu()

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
            player = Player()
            player.showMyPokemons()
            print()
            choice = Menu.ShowQuestion("", ["retour"])
            if choice == 0:
                Menu.ShowPlayerMenu()
        elif choice == 2:
            player = Player()
            player.IdentityCard()
            print()
            choice = Menu.ShowQuestion("", ["retour"])
            if choice == 0:
                Menu.ShowPlayerMenu()
        else:
            Menu.ShowMenu()
