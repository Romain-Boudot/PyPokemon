import locale, re

class Env:
    loc = "fr"

    @staticmethod
    def init():
        match = re.search(r"\(\"(.+)_.*\",.*\)",
                          str(locale.getdefaultlocale()))
        if (match != None):
            Env.loc = match.group(1)