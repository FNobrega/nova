# Libraries
from PPlay.window import *
# Declarations
width = 800
height = 600
screen = Window(width, height)
# Game
screen.set_title('Conquer Nova')
# default values from game object
name = "Player"
classType = 4
keyboard = Window.get_keyboard()
change = 0
menuScreen = 0
# views
from view.viewBattle import*
from view.viewWorld import*
from view.viewMenu import*
# controllers
from controller.controllerBattle import*
# models
from model.mainGame import *
# Class
from view.character import Mage
from view.character import Paladin
from view.character import Warrior

bossNumber = -1

# Function
def convertFileToData(playerState, player):
    player.name = playerState[0]
    player.type = playerState[1]
    player.lvl = playerState[2]
    player.item = playerState[3]
    player.weapon = playerState[4]
    player.position[0] = playerState[5]
    player.position[1] = playerState[6]
    for i in range(len(player.bossHide)):
        player.bossHide[i] = playerState[7 + i]
    for j in range(len(player.itemHide)):
        player.itemHide[j] = playerState[11 + j]
    for k in range(len(player.weaponHide)):
        player.weaponHide[k] = playerState[15 + k]
    return None

# On Menu
while classType == 4:
    mousePosition = [0, 0]
    # Get mouse position
    mouse = Window.get_mouse()
    if mouse.is_button_pressed(1):
        mousePosition = mouse.get_position()
    if menuScreen == 0:
        menuScreen = loadMenu(width, height, mousePosition, screen)
        mousePosition = [0, 0]
    elif menuScreen == 1:
        classType = loadMenuNewGame(width, height, mousePosition, screen)
    elif menuScreen == -1:
        menuScreen = loadHistoryMenu(width, height, mousePosition, screen)
    if menuScreen == 2:
        state = loadState()
        classType = state[1]
        name = "Player 1"
        # print(classType)
        if classType == 1:
            user = Mage(name, 5)
            user.local = 0
            user.type = classType
        elif classType == 2:
            user = Paladin(name, 5)
            user.local = 0
            user.type = classType
        elif classType == 3:
            user = Warrior(name, 5)
            user.local = 0
            user.type = classType
        # Load case
        # print(user.name)
        if state[0] != "Player Name":
            convertFileToData(state, user)
    else:
        name = "Player 1"
        if classType == 1:
            user = Mage(name, 5)
            user.local = 0
            user.type = classType
        elif classType == 2:
            user = Paladin(name, 5)
            user.local = 0
            user.type = classType
        elif classType == 3:
            user = Warrior(name, 5)
            user.local = 0
            user.type = classType
    screen.update()

# Set world position
if menuScreen != 2:
    user.position = [400 + width/2 - backgroundWorld.width, 300 + height/2 - backgroundWorld.height]
image = 1
# Create a variable to define if exist an oponent
initiateOponent = 0
# Game Loop
loopState = True
while loopState:
    # move description
    # -2 n or N
    # -1 y or Y
    # 0 nothing
    # 1(Up), 2(Down), 3(Left), 4(Right)
    # 5 (Space)

    screen.set_background_color((0, 0, 0))
    move = 0

    if keyboard.key_pressed("SPACE") and change == 0:
        move = 5
        change = 5
        user.win = False
        user.getWeapon = False
        user.getItem = False
        user.text = False
    elif (keyboard.key_pressed("n") or keyboard.key_pressed("N")) and change == 0:
        move = -2
        change = 5
    elif (keyboard.key_pressed("y") or keyboard.key_pressed("Y")) and change == 0:
        move = -1
        change = 5
    elif keyboard.key_pressed("UP") and change == 0:
        move = 1
        user.lastMove = [0, 20]
        if user.local > 0:
            change = 5
    elif keyboard.key_pressed("DOWN") and change == 0:
        move = 2
        user.lastMove = [0, -20]
        if user.local > 0:
            change = 5
    elif keyboard.key_pressed("LEFT") and change == 0:
        move = 3
        user.lastMove = [20, 0]
        if user.local > 0:
            change = 5
    elif keyboard.key_pressed("RIGHT") and change == 0:
        move = 4
        user.lastMove = [-20, 0]
        if user.local > 0:
            change = 5
    # Press (q) to quit
    elif keyboard.key_pressed("q"):
        loopState = False
    else:
        change -= 1
        if change < 0:
            change = 0
    if user.local == 0:
        user.local = loadWorld(user, move, width, height, screen)
    # On battle with boss 1
    elif user.local == 2:
        if initiateOponent == 0:
            bossNumber = 0
            bossArray = openBossFile(1)
            oponent = make_oponent(user)
            oponent.lvl = int(bossArray[0].strip('\n'))
            oponent.name = bossArray[1].strip('\n')
            oponent.type = int(bossArray[2].strip('\n'))
            oponent.charImageBattle[0] = Sprite(bossArray[3].strip('\n'))
            oponent.item = int(bossArray[4])
            oponent.weapon = int(bossArray[5])
            # Initiate the oponent object, in the end of combat, transform this variable in 0
            initiateOponent = 1
        loadBattle(user, oponent, screen, move, bossNumber)
        # after win, hide boss and return win state to initial
        if user.win:
            user.bossHide[0] = 1
        if user.local == 0:
            initiateOponent = 0
    # On battle with boss 2
    elif user.local == 3:
        if initiateOponent == 0:
            bossNumber = 1
            bossArray = openBossFile(2)
            oponent = make_oponent(user)
            oponent.lvl = int(bossArray[0].strip('\n'))
            oponent.name = bossArray[1].strip('\n')
            oponent.type = int(bossArray[2].strip('\n'))
            oponent.charImageBattle[0] = Sprite(bossArray[3].strip('\n'))
            oponent.item = int(bossArray[4])
            oponent.weapon = int(bossArray[5])
            # Initiate the oponent object, in the end of combat, transform this variable in 0
            initiateOponent = 1
        loadBattle(user, oponent, screen, move, bossNumber)
        # after win, hide boss and return win state to initial
        if user.win:
            user.bossHide[1] = 1
        if user.local == 0:
            initiateOponent = 0
    # On battle with boss 3
    elif user.local == 4:
        if initiateOponent == 0:
            bossNumber = 2
            bossArray = openBossFile(3)
            oponent = make_oponent(user)
            oponent.lvl = int(bossArray[0].strip('\n'))
            oponent.name = bossArray[1].strip('\n')
            oponent.type = int(bossArray[2].strip('\n'))
            oponent.charImageBattle[0] = Sprite(bossArray[3].strip('\n'))
            oponent.item = int(bossArray[4])
            oponent.weapon = int(bossArray[5])
            # Initiate the oponent object, in the end of combat, transform this variable in 0
            initiateOponent = 1
        loadBattle(user, oponent, screen, move, bossNumber)
        # after win, hide boss and return win state to initial
        if user.win:
            user.bossHide[2] = 1
        if user.local == 0:
            initiateOponent = 0
    # On battle with boss 4
    elif user.local == 5:
        if initiateOponent == 0:
            bossNumber = 3
            bossArray = openBossFile(4)
            oponent = make_oponent(user)
            oponent.lvl = int(bossArray[0].strip('\n'))
            oponent.name = bossArray[1].strip('\n')
            oponent.type = int(bossArray[2].strip('\n'))
            oponent.charImageBattle[0] = Sprite(bossArray[3].strip('\n'))
            oponent.item = int(bossArray[4])
            oponent.weapon = int(bossArray[5])
            # Initiate the oponent object, in the end of combat, transform this variable in 0
            initiateOponent = 1
        loadBattle(user, oponent, screen, move, bossNumber)
        # after win, hide boss and return win state to initial
        if user.win:
            user.bossHide[3] = 1
            user.local = 6
        if user.local == 0:
            initiateOponent = 0
    # End Screen
    elif user.local == 6:
        winMenu()
    # On battle
    elif user.local == 1:
        #bossNumber = -1
        if initiateOponent == 0:
            bossNumber = -1
            oponent = make_oponent(user)
            # Initiate the oponent object, in the end of combat, transform this variable in 0
            initiateOponent = 1
        loadBattle(user, oponent, screen, move, bossNumber)
        if user.local == 0:
            initiateOponent = 0
    saveState(user)
    screen.update()
