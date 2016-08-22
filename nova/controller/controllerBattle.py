# libraries
from random import randint

from view.character import Mage
from view.character import Paladin
from view.character import Warrior


def make_oponent(player):
    oponentType = (randint(1, 2) + player.type) % 3
    if oponentType == 1:
        oponent = Mage("Oponent", player.lvl)
    elif oponentType == 2:
        oponent = Paladin("Oponent", player.lvl)
    elif oponentType == 0:
        oponent = Warrior("Oponent", player.lvl)
    return oponent


def attack_phase(player, oponent, attackPlayer, bNumber):

    attackOponent = randint(0, 2)
    if attackPlayer == 1:
        oponent.hp -= player.attack1()
    elif attackPlayer == 2:
        oponent.hp -= player.attack2()
    elif attackPlayer == 3:
        oponent.hp -= player.attack3()
    if oponent.hp < 1:
        if bNumber != -1:
            player.bossHide[bNumber] = 1

        player.lvl += 1
        player.hp = int(player.lvl * player.hpConst)
        player.win = True
        player.position[0] -= player.lastMove[0]
        player.position[1] -= player.lastMove[1]
        return 0

    if attackOponent == 0:
        player.hp -= oponent.attack1()
    elif attackOponent == 1:
        player.hp -= oponent.attack2()
    elif attackOponent == 2:
        player.hp -= oponent.attack3()
    if player.hp < 1:
        player.hp = int(player.lvl * player.hpConst)
        player.position[0] -= player.lastMove[0]
        player.position[1] -= player.lastMove[1]
        return 0
    return 1
