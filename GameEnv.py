<<<<<<< Updated upstream
import locale
import Env


class Env:
    loc = ""

    @staticmethod
    def init(self):
        match = re.search(r"\(\'(.+)_.*\',.*\)",
                          str(locale.getdefaultlocale()))
        if (match != None):
            self.loc = match.group(1)
        else:
            self.loc = 'fr'
=======
class env:
    loc = 'fr'
>>>>>>> Stashed changes
