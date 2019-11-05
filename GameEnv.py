import locale, re

class Env:
    loc = ""

    def __init__(self):
        match = re.search(r"\(\'(.+)_.*\',.*\)",
                          str(locale.getdefaultlocale()))
        if (match != None):
            self.loc = match.group(1)
        else:
            self.loc = 'fr'
