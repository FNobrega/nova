# This file contains the classes
# Libraries
from PPlay.sprite import *
from random import randint


# Father class character
class Character(object):
    # Class constructor
    def __init__(self, name, lvl):
        self.hpConst = 5
        self.attackConst = 1
        self.name = name
        self.lvl = lvl
        self.hp = int(lvl*self.hpConst)
        self.attack = int(lvl*self.attackConst)
        self.atk = 1
        self.type = 4
        self.local = 1
        self.weapon = 0
        self.item = 0
        self.position = [0, 0]
        self.frame = 1
        self.lastMoviment = 0
        self.bossHide = [0]*4
        self.itemHide = [0]*4
        self.weaponHide = [0]*4
        self.win = False
        self.getWeapon = False
        self.getItem = False
        self.lastMove = [0, 0]
        self.text = 0


def make_character(name, lvl):
        character = Character(name, lvl)
        return character


# Child classes from Character:
# Warrior
class Warrior(Character):

    def __init__(self, name, lvl):
        Character.__init__(self, name, lvl)

        # load functions
        self.charImageBattle = [Sprite("view/Sprites/battle/character/warriorFrontTransparent.png"),
                                Sprite("view/Sprites/battle/character/warriorBackTransparent.png")]
        self.charImageWorld = [Sprite("view/Sprites/map/warriorRunBack.png", 3),
                               Sprite("view/Sprites/map/warriorRunFront.png", 3),
                               Sprite("view/Sprites/map/warriorRunLeft.png", 3),
                               Sprite("view/Sprites/map/warriorRunRight.png", 3),
                               Sprite("view/Sprites/map/warriorRunFront.png", 3)]
        self.type = 2
        self.attackConst = 3

    def attack1(self):
        return int(self.attack*self.attackConst)

    def attack2(self):
        atk = self.attack1() + self.item
        self.item = 0
        return int(atk)

    def attack3(self):
        atk = self.attack1() + self.weapon*self.attackConst
        self.weapon -= 1
        if self.weapon < 0:
            self.weapon = 0
        return int(atk)


# Paladin
class Paladin(Character):

    def __init__(self, name, lvl):
        Character.__init__(self, name, lvl)

        self.charImageBattle = [Sprite("view/Sprites/battle/character/paladinFrontTransparent.png"),
                                Sprite("view/Sprites/battle/character/paladinBackTransparent.png")]
        self.charImageWorld = [Sprite("view/Sprites/map/paladinRunBack.png", 3), Sprite("view/Sprites/map/paladinRunFront.png",3),
                               Sprite("view/Sprites/map/paladinRunLeft.png", 3), Sprite("view/Sprites/map/paladinRunRight.png",3),
                               Sprite("view/Sprites/map/paladinRunFront.png", 3)]
        self.type = 1
        self.attackConst = 2

    def attack1(self):
        self.hp += self.lvl//self.attackConst
        if self.hp > int(self.lvl*self.hpConst):
            self.hp = int(self.lvl*self.hpConst)
        return int(self.attack)

    def attack2(self):
        atk = self.attack1() + self.item
        self.hp += int(self.item*self.attackConst)
        if self.hp > int(self.lvl*self.hpConst):
            self.hp = int(self.lvl*self.hpConst)
        self.item = 0
        return int(atk)

    def attack3(self):
        atk = self.attack1() + self.weapon*self.attackConst
        self.weapon -= 1
        if self.weapon < 0:
            self.weapon = 0
        return int(atk)


# Madge
class Mage(Character):

    def __init__(self, name, lvl):
        Character.__init__(self, name, lvl)
        self.charImageBattle = [Sprite("view/Sprites/battle/character/mageFrontTransparent.png"),
                                Sprite("view/Sprites/battle/character/mageBackTransparent.png")]
        self.charImageWorld = [Sprite("view/Sprites/map/mageRunBack.png", 3), Sprite("view/Sprites/map/mageRunFront.png", 3),
                               Sprite("view/Sprites/map/mageRunLeft.png", 3), Sprite("view/Sprites/map/mageRunRight.png", 3),
                               Sprite("view/Sprites/map/mageRunFront.png"), 3]
        self.type = 0
        self.attackConst = 1

    def attack1(self):
        return randint(self.attackConst, int(self.lvl*3))
        # randint can only receive one variable, the other must be a constant
        # Ex.: c = a + b  "\n"    randint(d,c)

    def attack2(self):
        atk = self.attack1() + self.item
        self.item = 0
        return int(atk)

    def attack3(self):
        atk = self.attack1() + self.weapon
        self.weapon -= 1
        if self.weapon < 0:
            self.weapon = 0
        return int(atk)
