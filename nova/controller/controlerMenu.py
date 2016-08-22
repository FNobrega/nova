from PPlay.window import *


def chooseYourDestiny(warrior, paladin, mage):
    mouse = Window.get_mouse()
    if mouse.is_button_pressed(1):
        mousePosition = mouse.get_position()
        if (mousePosition[0] > warrior.x and mousePosition[0] < warrior.x+warrior.width) and \
                (mousePosition[1] > warrior.y and mousePosition[1] < warrior.y+warrior.height):
            return 1
        if (mousePosition[0] > paladin.x and mousePosition[0] < paladin.x+paladin.width) and \
                (mousePosition[1] > paladin.y and mousePosition[1] < paladin.y+paladin.height):
            return 2
        if (mousePosition[0] > mage.x and mousePosition[0] < mage.x+mage.width) and \
                (mousePosition[1] > mage.y and mousePosition[1] < mage.y+mage.height):
            return 3