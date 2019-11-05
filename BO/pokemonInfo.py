from DataHolder import DataHolder
from GameEnv import Env
from BO.types import Type
from BO.moves import Move


class PokemonInfo:
    """
        This class allows you to access
        a lot of information about pokemon
    """

    pokemonData = {}
    speciesData = {}

    abilitiesData = []
    abilities = []
    types = []
    area = []
    moves = []

    def __init__(self, url):
        """
            initializes the constructor

            :param data: an url of the specie
        """
        # self.pokemonData = DataHolder.get(url)
        self.speciesData = DataHolder.get(url)
        pknmUrl = next(var for var in self.speciesData["varieties"] if var["is_default"])["pokemon"]["url"]
        self.pokemonData = DataHolder.get(pknmUrl)

    def getId(self):
        """
            Returns the id of the pokemon

            return type: id.
        """
        return self.pokemonData["id"]

    def getPokedexId(self):
        """
            Returns the pokedex id of the pokemon

            return type: id.
        """
        pokedex = next(
            pokedex for pokedex in self.speciesData["pokedex_numbers"] if pokedex["pokedex"]["name"] == "national")
        return pokedex["entry_number"]

    def getDisplayName(self):
        """
            Returns the name of the pokemon according to language.

            return type: string.
        """
        speciesData = DataHolder.get(self.pokemonData["species"]["url"])
        for name in speciesData["names"]:
            if name["language"]["name"] == Env().loc:
                return name["name"]

    def getName(self):
        """
            Returns the name of the pokemon.

            return type: string.
        """
        return self.pokemonData["name"]

    def getHeight(self):
        """
            Returns the height of this Pokemon in decimetres.

            return type : integer.
        """
        return self.pokemonData["height"]

    def getWeight(self):
        """
            Returns the weight of this pokemon in hectograms.

            return type : integer.
        """
        return self.pokemonData["weight"]

    def getOrder(self):
        """
            returns the order in which the Pokemon is displayed

            return type : integer.
        """
        return self.pokemonData["order"]

    def getDisplayAbilities(self):
        """
            returns A list of abilities this Pokémon could potentially have depending on the language of the System.

            return type : list.
        """
        for abilitie in self.pokemonData["abilities"]:
            self.abilitiesData.append(
                DataHolder.get(abilitie["ability"]["url"])["names"])

        for name in self.abilitiesData:
            for i in range(0, 10):
                if name[i]["language"]["name"] == Env().loc:
                    self.abilities.append(name[i]["name"])
        return self.abilities

    def getDisplayTypes(self):
        """
            returns a list of details showing types this Pokémon has depending on the language of the System.

            return type : list.
        """
        for kind in self.pokemonData["types"]:
            self.types.append(Type(kind["type"]["url"]).getDisplayName())

        return self.types

    def getArea(self):
        """
            returns the location area the referenced Pokémon can be encountered in.

            return type : list.
        """
        return self.area

    def getDisplayMoves(self):
        """
            returns a movement list that pokemon can learn depending on the language of the System.

            return type: list.
        """
        for move in self.pokemonData["moves"]:
            self.moves.append(Move(move["move"]["url"]).getDisplayName())

        return self.moves
