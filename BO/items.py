import locale
from GameEnv import Env
from DataHolder import DataHolder


class Items:

    data = {}
    attributes = []

    def __init__(self, id: int):
        self.data = DataHolder.get("https://pokeapi.co/api/v2/type/%d/" % id)
        self.init()

    def __init__(self, url: str):
        self.data = DataHolder.get(url)
        self.init()

    def init(self):
        for item in self.data["attributes"]:
            self.attributes.append(item["name"])

    def getId(self):
        return self.data["id"]

    def getName(self):
        return self.data["name"]

    def getCost(self):
        return self.data["cost"]

    def getDisplayName(self):
        for lang in self.data['names']:
            if lang["language"]["name"] == Env.loc:
                return lang["name"]

    def getSprite(self):
        return self.data["sprites"]["default"]

    def getCategory(self):
        return self.data["category"]["name"]

    def getAttributes(self):
        return self.attributes

    def isHoldable(self):
        return 'holdable' in self.attributes

    def isUnderground(self):
        return 'underground' in self.attributes

    def isHoldablePassive(self):
        return 'holdable-passive' in self.attributes

    def isHoldableActive(self):
        return 'holdable-active' in self.attributes

    def isUsableInBattle(self):
        return 'usable-in-battle' in self.attributes

    def isUsableOverworld(self):
        return 'usable-overworld' in self.attributes

    def isConsumable(self):
        return 'consumable' in self.attributes

    def isCountable(self):
        return 'countable' in self.attributes

    def getDescription(self):
        for text in self.data['flavor_text_entries']:
            if text["language"]["name"] == Env.loc:
                return text["text"]
