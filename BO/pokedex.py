from DataHolder import DataHolder
from BO.pokemonInfo import PokemonInfo


class Pokedex:

    pokemons = {}

    def __init__(self):
        pokemonGen1Data = DataHolder.get(
            "https://pokeapi.co/api/v2/generation/1/")

        for spiece in pokemonGen1Data["pokemon_species"]:
            pokemon = PokemonInfo(spiece["url"])
            self.pokemons[str(pokemon.getPokedexId())] = {
                "discover": False,
                "caught": False,
                "pokemon": pokemon
            }
