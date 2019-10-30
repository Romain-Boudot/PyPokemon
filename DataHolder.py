import requests, json, re

class DataHolder:
    data = {}

    @staticmethod
    def loadData():
        file = open("data", "r")
        DataHolder.data = json.loads("".join(file.readlines()))
        file.close()
    
    @staticmethod
    def saveData():
        file = open("data", "w")
        file.flush()
        file.write(json.dumps(DataHolder.data))
        file.close

    @staticmethod
    def get(url):
        uri = re.search(r"https://pokeapi\.co/api/v2/(.+)", url)
        if uri != None:
            uri = uri.group(1)
            if uri in DataHolder.data:
                return DataHolder.data[uri]
            else:
                data = json.loads(requests.get(url).text)
                DataHolder.data[uri] = data
                return data
        else:
            return None