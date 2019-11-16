import BO, random, math
from BO.pokemons import Pokemon
from BO.gameCtx import GameCtx

class Fight:

    playerTeam = []
    enemyTeam = []
    playerCursor = 0
    enemyCursor = 0
    isRandomEncounter = True
    done = False

    playerAttack = None
    enemyAttack = None

    FIGHT = 0
    BAG = 1
    POKEMON = 2
    ESCAPE = 3

    SELECTED_POKEMON = "selected-pokemon"
    SPECIFIC_MOVE = "specific-move"
    SELECTED_POKEMON_ME_FIRST = "selected-pokemon-me-first"
    ALLY = "ally"
    USERS_FIELD = "users-field"
    USER_OR_ALLY = "user-or-ally"
    OPPONENTS_FIELD = "opponents-field"
    USER = "user"
    RANDOM_OPPONENT = "random-opponent"
    ALL_OTHER_POKEMON = "all-other-pokemon"
    SELECTED_POKEMON = "selected-pokemon"
    ALL_OPPONENTS = "all-opponents"
    ENTIRE_FIELD = "entire-field"
    USER_AND_ALLIES = "user-and-allies"
    ALL_POKEMON = "all-pokemon"

    ON_ENEMY = [SELECTED_POKEMON, ALL_OPPONENTS, ALL_OTHER_POKEMON, SELECTED_POKEMON_ME_FIRST, RANDOM_OPPONENT]
    ON_ME = [USER, USER_OR_ALLY]
    ON_ALL = [ALL_POKEMON]

    def __init__(self, playerTeam, enemyTeam = None):
        self.playerTeam = playerTeam
        if enemyTeam == None:
            self.enemyTeam.append(Pokemon(GameCtx.getRandomPokemonId()))
        else:
            self.isRandomEncounter = False
            self.enemyTeam = enemyTeam
        while not self.done:
            self.makePlayerChooseFightOption()
            if not self.done:
                self.makeComputerChooseFightOption()
                self.applyChoices()
                if self.playerTeam[self.playerCursor].getHp() <= 0:
                    print(self.playerTeam[self.playerCursor].getDisplayName() + " est KO.")
                    allTeamDown = True
                    for pokemon in self.playerTeam:
                        if pokemon.getHp() > 0:
                            allTeamDown = False
                    if allTeamDown:
                        print("Vous n'avez plus de pokemon en état de combattre.")
                        self.done = True
                    else:
                        self.playerCursor = (self.playerCursor + 1) % len(self.playerTeam)
                        while self.playerTeam[self.playerCursor].getHp() <= 0:
                            # ask for a pokemon
                            self.playerCursor = (self.playerCursor + 1) % len(self.playerTeam)
                if self.enemyTeam[self.enemyCursor].getHp() <= 0:
                    print(self.enemyTeam[self.enemyCursor].getDisplayName() + " est KO.")
                    allTeamDown = True
                    for pokemon in self.enemyTeam:
                        if pokemon.getHp() > 0:
                            allTeamDown = False
                    self.done = allTeamDown
                    if not allTeamDown:
                        self.enemyCursor = (self.enemyCursor + 1) % len(self.enemyTeam)
                        while self.enemyTeam[self.enemyCursor].getHp() <= 0:
                            # ask for a pokemon
                            self.enemyCursor = (self.enemyCursor + 1) % len(self.enemyTeam)

    def makePlayerChooseFightOption(self):
        # ask for player choice
        playerChoice = Fight.FIGHT
        if playerChoice == Fight.FIGHT:
            self.makePlayerChooseAttack()
        elif playerChoice == Fight.BAG:
            self.makePlayerChooseItem()
        elif playerChoice == Fight.POKEMON:
            self.makePlayerChoosePokemon()
        elif playerChoice == Fight.ESCAPE:
            if True: # always escape
                self.done = True

    def makePlayerChooseAttack(self):
        # ask for player attack choice
        self.playerAttack = 0

    def makePlayerChooseItem(self):
        pass

    def makePlayerChoosePokemon(self):
        # ask for a pokemon
        playerChoice = (self.playerCursor + 1) % len(self.playerTeam)
        while self.playerTeam[playerChoice].getHp() <= 0:
            # ask for a pokemon
            playerChoice = (self.playerCursor + 1) % len(self.playerTeam)

    def makeComputerChooseFightOption(self):
        if self.isRandomEncounter:
            self.makeComputerChooseAttack()

    def makeComputerChooseAttack(self):
        self.enemyAttack = random.choice(range(4)) # random attack

    def applyChoices(self):
        if self.playerTeam[self.playerCursor].getSpeed() >= self.enemyTeam[self.enemyCursor].getSpeed():
            self.applyDamage(self.playerTeam[self.playerCursor],
                             self.enemyTeam[self.enemyCursor],
                             self.playerTeam[self.playerCursor].getMoves()[self.playerAttack])
            if self.enemyTeam[self.enemyCursor].getHp() > 0:
                self.applyDamage(self.enemyTeam[self.enemyCursor],
                                 self.playerTeam[self.playerCursor],
                                 self.enemyTeam[self.enemyCursor].getMoves()[self.enemyAttack])
        else:
            self.applyDamage(self.enemyTeam[self.enemyCursor],
                             self.playerTeam[self.playerCursor],
                             self.enemyTeam[self.enemyCursor].getMoves()[self.enemyAttack])
            if self.playerTeam[self.playerCursor].getHp() > 0:
                self.applyDamage(self.playerTeam[self.playerCursor],
                                 self.enemyTeam[self.enemyCursor],
                                 self.playerTeam[self.playerCursor].getMoves()[self.playerAttack])

    def applyDamage(self, sender, target, skill):
        skill.addPP(-1)

        stab = 1.5 if target.getType1().getName() == skill.getType().getName() or target.getType2().getName() == skill.getType().getName() else 1
        efficiency = skill.getType().ratioAgainst(target.getType1()) * skill.getType().ratioAgainst(target.getType2())
        speedMod = sender.getSpeed() % 2
        critRate = (sender.getSpeed() + (-speedMod if speedMod < 1 else 2-speedMod) / 256) + skill.getCritRate
        crit = 1 if random.randint(0, 100) / 100 < critRate else (2 * sender.getLevel() + 5) / (sender.getLevel() + 5)
        attackDamageModifier = random.randint(85, 100) / 100

        skillDamage = (((sender.getLevel() * 0.4 + 2) * sender.getAttack() * skill.getPower()) / (target.getDefense() * 50)) * stab * efficiency * crit * attackDamageModifier

        if skill.getTarget() in Fight.ON_ENEMY:
            target.addHP(-skillDamage)
        elif skill.getTarget() in Fight.ON_ME:
            sender.addHP(-skillDamage)
        elif skill.getTarget() in Fight.ON_ALL:
            target.addHP(-skillDamage)
            sender.addHP(-skillDamage)