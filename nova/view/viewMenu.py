from PPlay.gameimage import *
from time import sleep
from model.menu import *


def loadMenu(x, y, mousePosition, screenMenu):
    backgroundMenu = GameImage("Sprites/menu/backgroundMenu.png")
    title = GameImage("Sprites/menu/titleMenu.png")
    loadImage = GameImage("Sprites/menu/load.png")
    newGameImage = GameImage("Sprites/menu/newGame.png")
    title.set_position(x/16,y/15)
    loadImage.set_position(x/4-(loadImage.width/2), y/2 - (loadImage.height/2))
    newGameImage.set_position(x/1.3-(newGameImage.width/2), y/2 - (newGameImage.height/2))
    # Draw
    backgroundMenu.draw()
    title.draw()
    loadImage.draw()
    newGameImage.draw()
    #Controler Menu

    # Load Game
    if (mousePosition[0] > loadImage.x and mousePosition[0] < loadImage.x+loadImage.width) and\
            (mousePosition[1] > loadImage.y and mousePosition[1] < loadImage.y+loadImage.height):
        return 2
    # New Game
    elif (mousePosition[0] > newGameImage.x and mousePosition[0] < newGameImage.x+newGameImage.width) and\
            (mousePosition[1] > newGameImage.y and mousePosition[1] < newGameImage.y+newGameImage.height):
        sleep(0.2)
        return -1
    return 0


def loadMenuNewGame(x, y, mousePosition, screenMenu):
    backgroundMenu = GameImage("Sprites/menu/backgroundClass.png")
    warriorImage = GameImage("Sprites/menu/warriorMenu.png")
    paladinImage = GameImage("Sprites/menu/paladinMenu.png")
    mageImage = GameImage("Sprites/menu/mageMenu.png")

    startText = "To start, select your character:"


    warriorImage.set_position(x/4.5-(warriorImage.width/2), y/2 - (warriorImage.height/2))
    paladinImage.set_position(x/2-(paladinImage.width/2), y/2 - (paladinImage.height/2))
    mageImage.set_position(x/1.29-(mageImage.width/2), y/2 - (mageImage.height/2))
    # Draw
    backgroundMenu.draw()
    warriorImage.draw()
    paladinImage.draw()
    mageImage.draw()
    screenMenu.draw_text(startText, screenMenu.width/40, screenMenu.height/7,
                            size=25, color=(100, 100, 100))

    # Controller Menu
    charType = 4
    # User Warrior
    if (mousePosition[0] > warriorImage.x and mousePosition[0] < warriorImage.x+warriorImage.width) and\
            (mousePosition[1] > warriorImage.y and mousePosition[1] < warriorImage.y+warriorImage.height):
        charType = 3
    # User Paladin
    if (mousePosition[0] > paladinImage.x and mousePosition[0] < paladinImage.x+paladinImage.width) and\
            (mousePosition[1] > paladinImage.y and mousePosition[1] < paladinImage.y+paladinImage.height):
        charType = 2
    # User Mage
    if (mousePosition[0] > mageImage.x and mousePosition[0] < mageImage.x+mageImage.width) and\
            (mousePosition[1] > mageImage.y and mousePosition[1] < mageImage.y+mageImage.height):
        charType = 1
    return charType


def loadHistoryMenu(x, y, mousePosition, screenMenu):
    textPositionY = 1
    backgroundHistoryMenu = GameImage("Sprites/menu/backgroundHistory.png")
    click = GameImage("Sprites/menu/clickHereToContinue.png")
    click.set_position(x/2-click.width/2, y-click.height)

    if (mousePosition[0] > click.x and mousePosition[0] < click.x + click.width) and\
            (mousePosition[1] > click.y and mousePosition[1] < click.y + click.height):
      screenMenu = 1
      return screenMenu
    history = readHistory("data_base/text/menu/initialText.txt")
    backgroundHistoryMenu.draw()
    for i in range(len(history)):
        screenMenu.draw_text(history[i], screenMenu.width/40, screenMenu.height/7*textPositionY, size=25, color=(240, 240, 240))
        textPositionY += 0.5
    click.draw()
    return -1


def winMenu():
    backgroundWin = GameImage("Sprites/menu/backgroundWin.png")
    backgroundWin.draw()
    return 6