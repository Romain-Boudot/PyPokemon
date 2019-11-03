import locale
from GameEnv import Env
from DataHolder import DataHolder


class Items:

    data = {}

    attributes = []

    def __init__(self, url):
        """
            initializes the constructor

            :param data: an url
        """
        self.data = DataHolder.get(url)

    def getId(self):
        """
            Returns the id of the item.

            return type: id.
        """
        return self.data["id"]

    def getName(self):
        """
            Returns the name of the item.

            return type: string.
        """
        return self.data["name"]

    def getCost(self):
        """
            returns the price of the item.

            return type: int.
        """
        return self.data["cost"]

    def getDisplayName(self):
        """
            Returns the name of the item according to language.

            return type: string.
        """
        for lang in self.data['names']:
            if lang["language"]["name"] == Env().loc:
                return lang["name"]

    def getSprite(self):
        """
            Returns the sprite of the item.

            return type: string.
        """
        return self.data["sprites"]["default"]

    def getCategory(self):
        """
            returns the category of the item.

            return type: string.
        """
        return self.data["category"]["name"]

    def getAttributes(self):
        """
            returns the attributes of the item.

            return type: string.
        """
        for item in self.data["attributes"]:
            self.attributes.append(item["name"])

        return self.attributes

    def isHoldable(self):
        """
            returns true if the item is holdable false otherwise.

            return type: bollean.
        """
        return 'holdable' in self.attributes

    def isUnderground(self):
        """
            returns true if the item is Underground false otherwise.

            return type: bollean.
        """
        return 'underground' in self.attributes

    def isHoldablePassive(self):
        """
            returns true if the item is hodable passive false otherwise.

            return type: bollean.
        """
        return 'holdable-passive' in self.attributes

    def isHoldableActive(self):
        """
            returns true if the item is hodable active false otherwise.

            return type: bollean.
        """
        return 'holdable-active' in self.attributes

    def isUsableInBattle(self):
        """
            returns true if the item is usable in battle false otherwise.

            return type: bollean.
        """
        return 'usable-in-battle' in self.attributes

    def isUsableOverworld(self):
        """
            returns true if the item is usable Overworld false otherwise.

            return type: bollean.
        """
        return 'usable-overworld' in self.attributes

    def isConsumable(self):
        """
            returns true if the item is consumable false otherwise.

            return type: bollean.
        """
        return 'consumable' in self.attributes

    def isCountable(self):
        """
            returns true if the item is countable false otherwise.

            return type: bollean.
        """
        return 'countable' in self.attributes

    def getDisplayDescription(self):
        """
            returns the description according to language.

            return type: string.
        """
        for text in self.data['flavor_text_entries']:
            if text["language"]["name"] == Env().loc:
                return text["text"]
