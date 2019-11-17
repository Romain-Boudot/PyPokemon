import random
import math
import os
from BO.pokemons import Pokemon
from BO.gameCtx import GameCtx
import BO.menu


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

    ON_ENEMY = [SELECTED_POKEMON, ALL_OPPONENTS, ALL_OTHER_POKEMON,
                SELECTED_POKEMON_ME_FIRST, RANDOM_OPPONENT]
    ON_ME = [USER, USER_OR_ALLY]
    ON_ALL = [ALL_POKEMON]

    def __init__(self, playerTeam, enemyTeam=None):
        self.playerTeam = playerTeam
        if enemyTeam == None:
            self.enemyTeam.append(Pokemon(GameCtx.getRandomPokemonId()))
        else:
            self.isRandomEncounter = False
            self.enemyTeam = enemyTeam

        enemyPokemon = self.enemyTeam[self.enemyCursor]
        BO.menu.Menu.display("[p]{pokemon}[] de niveau {level} apparait".format(
            pokemon=enemyPokemon.getDisplayName(), level=enemyPokemon.getLevel()))

        while not self.done:
            self.makePlayerChooseFightOption()
            if not self.done:
                self.makeComputerChooseFightOption()
                self.applyChoices()
                if self.playerTeam[self.playerCursor].getHp() <= 0:
                    BO.menu.Menu.display("\n[y]{name} est KO.[]".format(
                        name=self.playerTeam[self.playerCursor].getDisplayName()))
                    allTeamDown = True
                    for pokemon in self.playerTeam:
                        if pokemon.getHp() > 0:
                            allTeamDown = False
                    if allTeamDown:
                        BO.menu.Menu.display(
                            "\n[y]Vous n'avez plus de pokemon en état de combattre.[]")
                        self.done = True
                    else:
                        self.playerCursor = (
                            self.playerCursor + 1) % len(self.playerTeam)
                        while self.playerTeam[self.playerCursor].getHp() <= 0:
                            # ask for a pokemon
                            self.playerCursor = (
                                self.playerCursor + 1) % len(self.playerTeam)
                if self.enemyTeam[self.enemyCursor].getHp() <= 0:
                    BO.menu.Menu.display("\n[y]{name} est KO.[]".format(
                        name=self.enemyTeam[self.enemyCursor].getDisplayName()))
                    allTeamDown = True
                    for pokemon in self.enemyTeam:
                        if pokemon.getHp() > 0:
                            allTeamDown = False
                    self.done = allTeamDown
                    if not allTeamDown:
                        self.enemyCursor = (
                            self.enemyCursor + 1) % len(self.enemyTeam)
                        while self.enemyTeam[self.enemyCursor].getHp() <= 0:
                            # ask for a pokemon
                            self.enemyCursor = (
                                self.enemyCursor + 1) % len(self.enemyTeam)

    def printField(self):
        # os.system("cls")
        enemyPokemon = self.enemyTeam[self.enemyCursor]
        playerPokemon = self.playerTeam[self.playerCursor]
        BO.menu.Menu.display("\n[y]{name}[] Lv{level} [{hpcolor}]{hp}[]/{maxHp}        [b]vs[]        [{enemyhpcolor}]{enemyhp}[]/{enemymaxHp} [y]{enemyname}[] Lv{enemylevel} \n".format(
            hpcolor="r" if playerPokemon.getHp() <= playerPokemon.getMaxHp() /
            4 else "y" if playerPokemon.getHp() <= playerPokemon.getMaxHp() / 2 else "g",
            enemyhpcolor="r" if enemyPokemon.getHp() <= enemyPokemon.getMaxHp(
            ) / 4 else "y" if enemyPokemon.getHp() <= enemyPokemon.getMaxHp() / 2 else "g",
            name=playerPokemon.getDisplayName(),
            level=playerPokemon.getLevel(),
            hp=playerPokemon.getHp(),
            enemyname=enemyPokemon.getDisplayName(),
            enemylevel=enemyPokemon.getLevel(),
            enemyhp=enemyPokemon.getHp(),
            enemymaxHp=enemyPokemon.getMaxHp(),
            maxHp=playerPokemon.getMaxHp()))

    def makePlayerChooseFightOption(self):
        self.printField()
        playerChoice = BO.menu.Menu.ShowQuestion("Que va faire %s ?" % self.playerTeam[self.playerCursor].getDisplayName(), [
            "Attaquer", "Sac", "Pokemon", "Fuite"])
        if playerChoice == Fight.FIGHT:
            self.makePlayerChooseAttack()
        elif playerChoice == Fight.BAG:
            self.makePlayerChooseItem()
        elif playerChoice == Fight.POKEMON:
            self.makePlayerChoosePokemon()
        elif playerChoice == Fight.ESCAPE:
            if True:  # always escape
                BO.menu.Menu.display("\nVous prenez la fuite\n")
                self.done = True

    def makePlayerChooseAttack(self):
        self.printField()
        self.playerAttack = BO.menu.Menu.ShowQuestion(
            "Choisissez une attaque",
            list(map(lambda move: "{move}  -  {pp}/{maxpp}  -  [{type}]{typename}[]".format(
                move=move.getDisplayName(),
                pp=move.getPP(),
                maxpp=move.getMaxPP(),
                type=move.getType().getName(),
                typename=move.getType().getDisplayName()),
                self.playerTeam[self.playerCursor].getMoves())))

    def makePlayerChooseItem(self):
        pass

    def makePlayerChoosePokemon(self):
        self.printField()
        playerChoice = BO.menu.Menu.ShowQuestion(
            "Choisissez un pokemon",
            list(map(lambda pokemon: pokemon.getDisplayName(),
                     self.playerTeam)))
        while self.playerTeam[playerChoice].getHp() <= 0:
            # ask for a pokemon
            playerChoice = (self.playerCursor + 1) % len(self.playerTeam)

    def makeComputerChooseFightOption(self):
        # if self.isRandomEncounter:
        self.makeComputerChooseAttack()

    def makeComputerChooseAttack(self):
        self.enemyAttack = random.choice(
            range(len(self.enemyTeam[self.enemyCursor].getMoves())))  # random attack

    def applyChoices(self):
        if self.playerAttack == None and self.enemyAttack != None:
            self.applyDamage(self.enemyTeam[self.enemyCursor],
                             self.playerTeam[self.playerCursor],
                             self.enemyTeam[self.enemyCursor].getMoves()[self.enemyAttack])
        elif self.playerAttack != None and self.enemyAttack == None:
            self.applyDamage(self.playerTeam[self.playerCursor],
                             self.enemyTeam[self.enemyCursor],
                             self.playerTeam[self.playerCursor].getMoves()[self.playerAttack])
        else:
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
        self.playerAttack = None
        self.enemyAttack = None

    def applyDamage(self, sender, target, skill):
        skill.addPP(-1)

        type1 = target.getType1().getName()
        type2 = target.getType2().getName() if target.getType2() != None else None
        stab = 1.5 if type1 == skill.getType().getName(
        ) or type2 == skill.getType().getName() else 1
        efficiency = skill.getType().ratioAgainst(target.getType1()) * (1 if type2 ==
                                                                        None else skill.getType().ratioAgainst(target.getType2()))
        speedMod = sender.getSpeed() % 2
        critRate = (
            (sender.getSpeed() + (-speedMod if speedMod < 1 else 2-speedMod)) / 256)
        randomCrit = (random.randint(0, 100) / 100)
        crit = 1 if randomCrit > critRate else (
            2 * sender.getLevel() + 5) / (sender.getLevel() + 5)
        attackDamageModifier = random.randint(85, 100) / 100

        print("crit rate : %f" % critRate)
        print("randomCrit : %f" % randomCrit)

        skillDamage = (((sender.getLevel() * 0.4 + 2) * sender.getAttack() * skill.getPower()) /
                       (target.getDefense() * 50)) * stab * efficiency * crit * attackDamageModifier
        skillDamage = math.floor(skillDamage)

        BO.menu.Menu.display("\n{name} utilise {move}".format(
            name=sender.getDisplayName(), move=skill.getDisplayName()))
        if crit > 1 and skillDamage != 0:
            BO.menu.Menu.display("[y]coup critique ![]")
        if efficiency == 0:
            BO.menu.Menu.display("mais cela n'a aucun effet")
        if efficiency < 1 and efficiency > 0 and skillDamage != 0:
            BO.menu.Menu.display("mais ce n'est pas très efficace")
        if efficiency >= 2 and skillDamage != 0:
            BO.menu.Menu.display("c'est très efficace !")

        if skill.getTarget() in Fight.ON_ENEMY:
            target.addHP(-skillDamage)
        elif skill.getTarget() in Fight.ON_ME:
            sender.addHP(-skillDamage)
        elif skill.getTarget() in Fight.ON_ALL:
            target.addHP(-skillDamage)
            sender.addHP(-skillDamage)
