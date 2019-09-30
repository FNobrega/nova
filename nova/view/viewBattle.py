# libraries
from PPlay.gameimage import *
from controller.controllerBattle import *
from time import sleep
count = 0
backgroundBattle = GameImage("view/background/fundoBatalha1.png")
win = GameImage("view/Sprites/battle/winner.png")


# main Project
def loadBattle(player, oponent, screenBattle, movement,bossNumb):
    if player.atk == 1:
        defineAtk = ["=>", "  ", "  "]
    elif player.atk == 2:
        defineAtk = ["  ", "=>", "  "]
    elif player.atk == 3:
        defineAtk = ["  ", "  ", "=>"]
    if movement == 1:
        if player.atk == 2:
            defineAtk = ["=>", "  ", "  "]
            player.atk = 1
        elif player.atk == 3:
            defineAtk = ["  ", "=>", "  "]
            player.atk = 2
    elif movement == 2:
        if player.atk == 1:
             defineAtk = ["  ", "=>", "  "]
             player.atk = 2
        elif player.atk == 2:
             defineAtk = ["  ", "  ", "=>"]
             player.atk = 3
    if movement == 5:
        player.local = int(attack_phase(player, oponent, player.atk, bossNumb))

    player.charImageBattle[1].set_position(screenBattle.width / 16, screenBattle.height / 3)
    oponent.charImageBattle[0].set_position(screenBattle.width * 3 / 4, screenBattle.height / 18)
    backgroundText = GameImage("view/Sprites/battle/backgroundText.png")
    backgroundText.set_position(screenBattle.width/3, screenBattle.height*18/28)
    backgroundTextOp = GameImage("view/Sprites/battle/backgroundTextOp.png")
    backgroundTextOp.set_position(screenBattle.width/16, screenBattle.height*2/28)
    # Draw
    backgroundBattle.draw()# First draw
    backgroundText.draw()
    backgroundTextOp.draw()

    name = "nome: "+str(player.name)
    screenBattle.draw_text(name, screenBattle.width/3, screenBattle.height*18/28,
                            size=18, color=(0, 0, 0))
    lvl = "level: "+str(player.lvl)
    screenBattle.draw_text(lvl, screenBattle.width/3, screenBattle.height*19/28,
                            size=18, color=(0, 0, 0))
    life = "HP : "+str(player.hp)
    screenBattle.draw_text(life, screenBattle.width/3, screenBattle.height*20/28,
                size=18, color=(0, 0, 0))

    attack = [str(defineAtk[0]) +"Ataque basico", str(defineAtk[1]) + "Ataque com item, valor do item: " +
              str(player.item), str(defineAtk[2]) + "Ataque com arma, valor da arma: " + str(player.weapon)]
    screenBattle.draw_text(attack[0], screenBattle.width/3, screenBattle.height*21/28,
                            size=18, color=(0, 0, 0))
    screenBattle.draw_text(attack[1], screenBattle.width/3, screenBattle.height*22/28,
                            size=18, color=(0, 0, 0))
    screenBattle.draw_text(attack[2], screenBattle.width/3, screenBattle.height*23/28,
                            size=18, color=(0, 0, 0))
    # Oponent information
    nameOp = "nome: "+str(oponent.name)
    screenBattle.draw_text(nameOp, screenBattle.width/16, screenBattle.height*4/28,
                            size=18, color=(0, 0, 0))
    lvlOp = "level: "+str(oponent.lvl)
    screenBattle.draw_text(lvlOp, screenBattle.width/16, screenBattle.height*3/28,
                            size=18, color=(0, 0, 0))
    lifeOp = "HP : "+str(oponent.hp)
    screenBattle.draw_text(lifeOp, screenBattle.width/16, screenBattle.height*2/28,
                size=18, color=(0, 0, 0))

    oponent.charImageBattle[0].draw()
    player.charImageBattle[1].draw()
    return None
