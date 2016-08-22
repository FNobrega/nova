# libraries
from PPlay.gameimage import *
from PPlay.sprite import *
from controller.controllerWorld import *

# Game Image(s) and Sprite(s)
enemyHide = [0]*4
speed = 5
backgroundWorld = GameImage("background/backgroundMundo.png")
playerHouse = GameImage("Sprites/map/casa1.png")
girlTent = GameImage("Sprites/map/tendaItemPorLevel2.png")
noneHouse = GameImage("Sprites/map/casa2.png")
houseInFire1 = GameImage("Sprites/map/casa3PegandoFogo.png")
houseInFire2 = GameImage("Sprites/map/casa4PegandoFogo.png")
fire1 = GameImage("Sprites/map/fogo.png")
fire2 = GameImage("Sprites/map/fogo.png")
fire3 = GameImage("Sprites/map/fogo.png")
fire4 = GameImage("Sprites/map/fogo.png")
fire5 = GameImage("Sprites/map/fogo.png")
fire6 = GameImage("Sprites/map/fogo.png")
iSeeDeadPeople = GameImage("Sprites/map/mortoMapa.png")
howOftenDoYouSeeThem = GameImage("Sprites/map/mortoMapa.png")
allTheTime = GameImage("Sprites/map/cachorroMorto.png")
trapWeapon = GameImage("Sprites/map/armaTrap.png")
tree = Sprite("Sprites/map/arvore.png")
halfTree = Sprite("Sprites/map/arvoreMetade.png")
river = Sprite("Sprites/map/rio.png")
fence = Sprite("Sprites/map/tocoCerca.png")
burnedTree = Sprite("Sprites/map/arvoreQueimada.png")
halfBurnedTree = Sprite("Sprites/map/arvoreQueimadaMetade.png")
item = [5, 10, 15, 20]
item1 = Sprite("Sprites/map/item2.png")
item2 = Sprite("Sprites/map/item2.png")
item3 = Sprite("Sprites/map/item2.png")
item0 = Sprite("Sprites/map/item2.png")

weapon = [99, 2, 3, 4]
weapon1 = Sprite("Sprites/map/arma1.png")
weapon2 = Sprite("Sprites/map/arma1.png")
weapon3 = Sprite("Sprites/map/arma1.png")
# Best weapon
weapon0 = Sprite("Sprites/map/weapon4.png")


enemy = Sprite("Sprites/map/enemy.png")
enemy1 = Sprite("Sprites/map/enemy.png")
enemy2 = Sprite("Sprites/map/enemy.png")
enemy3 = Sprite("Sprites/map/enemy.png")

boss1 = Sprite("Sprites/map/boss1.png")
boss2 = Sprite("Sprites/map/boss2.png")
boss3 = Sprite("Sprites/map/boss3.png")
boss4 = Sprite("Sprites/map/boss4.png")
# main Project


def loadWorld(object, directions, x, y, screenWorld):

    # Collisions
    if not object.charImageWorld[4].collided(noneHouse) and not\
            object.charImageWorld[4].collided(girlTent) and not\
            object.charImageWorld[4].collided(playerHouse) and not\
            object.charImageWorld[4].collided(houseInFire1) and not\
            object.charImageWorld[4].collided(houseInFire2) and not\
            (object.charImageWorld[4].collided(enemy) and enemyHide[0] == 0) and not\
            (object.charImageWorld[4].collided(enemy1) and enemyHide[1] == 0) and not\
            (object.charImageWorld[4].collided(enemy2) and enemyHide[2] == 0) and not\
            (object.charImageWorld[4].collided(enemy3) and enemyHide[3] == 0) and not\
            (object.charImageWorld[4].collided(boss1) and object.bossHide[0] == 0) and not\
            (object.charImageWorld[4].collided(boss2) and object.bossHide[1] == 0) and not\
            (object.charImageWorld[4].collided(boss3) and object.bossHide[2] == 0) and not\
            (object.charImageWorld[4].collided(boss4) and object.bossHide[3] == 0):
        movement(object, directions, speed, x, y)
        if directions > 0 and directions < 5:
            object.lastMoviment = directions
    else:
        if directions != object.lastMoviment:
            movement(object, directions, speed, x, y)

    if directions == 5:
        if (not (object.charImageWorld[4].collided(enemy)) or enemyHide[0] != 0) and (not
                (object.charImageWorld[4].collided(enemy1)) or enemyHide[1] != 0) and (not
                (object.charImageWorld[4].collided(enemy2)) or enemyHide[2] != 0) and (not
                (object.charImageWorld[4].collided(enemy3)) or enemyHide[3] != 0):
            None
        else:
            return 1
    if directions == 5:
        if not(object.charImageWorld[4].collided(boss1)) or object.bossHide[0] != 0:
            None
        else:
            return 2
    if directions == 5:
        if not(object.charImageWorld[4].collided(boss2)) or object.bossHide[1] != 0:
            None
        else:
            return 3
    if directions == 5:
        if not(object.charImageWorld[4].collided(boss3)) or object.bossHide[2] != 0:
            None
        else:
            return 4
    if directions == 5:
        if not (object.charImageWorld[4].collided(boss4)) or object.bossHide[3] != 0:
            None
        else:
            return 5

    # Set Position(s)
    object.charImageWorld[4].set_position(x/2, y/2)
    backgroundWorld.set_position(object.position[0], object.position[1])
    playerHouse.set_position(object.position[0]+backgroundWorld.width*2.8/4,
                             object.position[1]+backgroundWorld.height-playerHouse.height)
    girlTent.set_position(object.position[0]+backgroundWorld.width*3.27/4, object.position[1])
    noneHouse.set_position(object.position[0]+backgroundWorld.width*1/6.29, object.position[1])
    houseInFire1.set_position(object.position[0]+backgroundWorld.width*1/15,
                              object.position[1]+backgroundWorld.height-houseInFire1.height)
    houseInFire2.set_position(object.position[0]+backgroundWorld.width*1/4,
                              object.position[1]+backgroundWorld.height-houseInFire2.height)
    fire1.set_position(object.position[0]+backgroundWorld.width*1/13,
                       object.position[1]+backgroundWorld.height-backgroundWorld.height/6.6)
    fire2.set_position(object.position[0]+backgroundWorld.width*1/6,
                       object.position[1]+backgroundWorld.height-backgroundWorld.height/7)
    fire3.set_position(object.position[0]+backgroundWorld.width*1/3,
                       object.position[1]+backgroundWorld.height-backgroundWorld.height/7.5)
    fire4.set_position(object.position[0]+backgroundWorld.width*1/3.73,
                       object.position[1]+backgroundWorld.height-backgroundWorld.height/14)
    fire5.set_position(object.position[0]+backgroundWorld.width*1/2.55,
                       object.position[1]+backgroundWorld.height-backgroundWorld.height/11)
    fire6.set_position(object.position[0]+backgroundWorld.width*1/8,
                       object.position[1]+backgroundWorld.height-backgroundWorld.height/10)
    iSeeDeadPeople.set_position(object.position[0]+backgroundWorld.width*1/7.8,
                                object.position[1]+backgroundWorld.height-(houseInFire1.height+iSeeDeadPeople.height))
    howOftenDoYouSeeThem.set_position(object.position[0]+backgroundWorld.width*1/3,
                                      object.position[1]+backgroundWorld.height-backgroundWorld.height/4)
    allTheTime.set_position(object.position[0]+backgroundWorld.width*1/2.45,
                            object.position[1]+backgroundWorld.height-allTheTime.height-halfBurnedTree.height)
    trapWeapon.set_position(object.position[0]+backgroundWorld.width*1/3,
                            object.position[1]+backgroundWorld.height-(backgroundWorld.height/4 + trapWeapon.height))

    item1.set_position(object.position[0]+backgroundWorld.width*1/1.5,
                       object.position[1]+backgroundWorld.height-(backgroundWorld.height/4 + item1.height))
    item2.set_position(object.position[0]+backgroundWorld.width*1/1.2,
                       object.position[1]+backgroundWorld.height-(backgroundWorld.height/1.8 + item2.height))
    item3.set_position(object.position[0]+backgroundWorld.width*1/1.9,
                       object.position[1]+backgroundWorld.height-(backgroundWorld.height/1.8 + item3.height))
    item0.set_position(object.position[0]+backgroundWorld.width*1/2.5,
                       object.position[1]+backgroundWorld.height-(backgroundWorld.height/3 + item0.height))
    weapon1.set_position(object.position[0]+backgroundWorld.width*1/1.3,
                         object.position[1]+backgroundWorld.height-(backgroundWorld.height/6 + weapon1.height))
    weapon2.set_position(object.position[0]+backgroundWorld.width*1/1.5,
                         object.position[1]+backgroundWorld.height-(backgroundWorld.height/1.5 + weapon2.height))
    weapon3.set_position(object.position[0]+backgroundWorld.width*1/2.5,
                         object.position[1]+backgroundWorld.height-(backgroundWorld.height/1.1 + weapon3.height))
    weapon0.set_position(object.position[0]+backgroundWorld.width-weapon0.width,
                         object.position[1]+backgroundWorld.height-weapon0.height)

    enemy.set_position(object.position[0]+backgroundWorld.width/1.05, object.position[1]+backgroundWorld.height/1.45)
    enemy1.set_position(object.position[0]+backgroundWorld.width/1.38, object.position[1]+backgroundWorld.height/8.2)
    enemy2.set_position(object.position[0]+backgroundWorld.width/4.6, object.position[1]+backgroundWorld.height/8.2)
    enemy3.set_position(object.position[0]+backgroundWorld.width/30.0, object.position[1]+backgroundWorld.height/1.3)

    boss1.set_position(object.position[0]+backgroundWorld.width/1.38, object.position[1]+backgroundWorld.height/2.2)
    boss2.set_position(object.position[0]+backgroundWorld.width/1.8, object.position[1]+backgroundWorld.height/5.25)
    boss3.set_position(object.position[0]+backgroundWorld.width/4.6, object.position[1]+backgroundWorld.height/2.2)
    boss4.set_position(object.position[0]+backgroundWorld.width/1.85, object.position[1]+backgroundWorld.height/1.28)
    # Draw(s)
    backgroundWorld.draw()
    # Draw river
    for i in range(34):
        if i != 7 and i != 8 and i != 24 and i != 25:
            river.set_position(object.position[0]+(river.width*i),
                               object.position[1]+(backgroundWorld.height/2-river.height/2))
            river.draw()
    # Draw halfTree
    for j in range(35):
        if j != 7 and j != 8 and j != 31:
            halfTree.set_position(object.position[0]+(halfTree.width*j), object.position[1])
            halfTree.draw()
    # Draw fence
    for k in range(25):
        if k != 5 and k != 20 and k != 12:
            fence.set_position(object.position[0]+(halfTree.width*4)+halfTree.width+noneHouse.width+(halfTree.width*10),
                               object.position[1]+(fence.height*k))
            fence.draw()
    # Draw burned tree
    for l in range(6):
        burnedTree.set_position(object.position[0],
                                object.position[1]+(backgroundWorld.height/2-river.height/2)+(burnedTree.height*l))
        burnedTree.draw()
    # Draw tree
    for m in range(12):
        tree.set_position(object.position[0], object.position[1]+(tree.width*m))
        tree.draw()
    # Draw half burned tree
    for n in range(22):
        if n != 4 and n != 5 and n != 6 and n != 7 and n != 8 and n != 10 and n != 11 and n != 12 and n != 13 and\
                        n != 14 and n != 15:
            halfBurnedTree.set_position(object.position[0]+halfBurnedTree.width*n,
                                        object.position[1]+backgroundWorld.height-halfBurnedTree.height)
            halfBurnedTree.draw()
    fire1.draw()
    fire2.draw()
    fire3.draw()
    fire4.draw()
    fire5.draw()
    fire6.draw()
    iSeeDeadPeople.draw()
    howOftenDoYouSeeThem.draw()
    allTheTime.draw()
    trapWeapon.draw()
    girlTent.draw()
    noneHouse.draw()

    if object.itemHide[0] == 0:
        item0.draw()
    if object.weaponHide[1] == 0:
        item1.draw()
    if object.itemHide[2] == 0:
        item2.draw()
    if object.weaponHide[3] == 0:
        item3.draw()

    if object.weaponHide[0] == 0:
        weapon0.draw()
    if object.weaponHide[1] == 0:
        weapon1.draw()
    if object.weaponHide[2] == 0:
        weapon2.draw()
    if object.weaponHide[3] == 0:
        weapon3.draw()

    object.charImageWorld[4].set_total_duration(500)
    object.charImageWorld[4].update()
    object.charImageWorld[4].pause()
    object.charImageWorld[4].draw()

    if enemyHide[0] == 0:
        enemy.draw()
    if enemyHide[1] == 0:
        enemy1.draw()
    if enemyHide[2] == 0:
        enemy2.draw()
    if enemyHide[3] == 0:
        enemy3.draw()

    if object.bossHide[0] == 0:
        boss1.draw()
    if object.bossHide[1] == 0:
        boss2.draw()
    if object.bossHide[2] == 0:
        boss3.draw()
    if object.bossHide[3] == 0:
        boss4.draw()
    playerHouse.draw()
    houseInFire1.draw()
    houseInFire2.draw()

    lvl = "level: "+str(object.lvl)
    screenWorld.draw_text(lvl, screenWorld.width/10, screenWorld.height/10,
                            size=18, color=(255, 255, 255))
    life = "HP : "+str(object.hp)
    screenWorld.draw_text(life, screenWorld.width/10, screenWorld.height/16,
                size=18, color=(255, 255, 255))

    return int(0)
