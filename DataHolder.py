import requests, json, re, base64

class DataHolder:
    data = {}

    @staticmethod
    def loadData():
        file = open("data", "r")
        DataHolder.data = json.loads("".join(base64.b64decode(file.readlines())))
        file.close()
    
    @staticmethod
    def saveData():
        file = open("data", "w")
        file.flush()
        file.write(base64.b64encode(json.dumps(DataHolder.data, separators=(",", ":")).encode('utf-8')).decode('utf-8'))
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
                DataHolder.saveData()
                return data
        else:
            return None