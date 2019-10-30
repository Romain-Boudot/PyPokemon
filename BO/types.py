from DataHolder import DataHolder
from GameEnv import env

class Type:

    data = {}

    def __init__(self, id: int):
        self.data = DataHolder.get("https://pokeapi.co/api/v2/type/%d/" % id)

    def __init__(self, url: str):
        self.data = DataHolder.get(url)

    def getName(self):
        return self.data['name']

    def getDisplayName(self):
        for name in self.data['names']:
            if name['language']['name'] == env.loc:
                return name['name']

    def ratioAgainst(self, type):
        for h in self.data['damage_relations']['half_damage_to']:
            if h["name"] == type.getName(): return 0.5
        for d in self.data['damage_relations']['double_damage_to']:
            if d["name"] == type.getName(): return 2
        for n in self.data['damage_relations']['no_damage_to']:
            if n["name"] == type.getName(): return 0
        return 0

    def getSprite(self):
        return {
            "file": "types.png",
            # 0     32
            # 16
        }