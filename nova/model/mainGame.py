# Libraries


# Function
def openBossFile(n):
    location = "view/data_base/boss/boss"+str(n)+".txt"
    file = open(location, "r")
    array = [0, "Boss", 0, "sprite 1", 0, 0]
    # lvl, name, type, image location, item, weapon
    i = 0
    for line in file:
        array[i] = line
        i += 1
    file.close()
    # print(array)#Debug
    return array


def saveState(object):
    file = open("player", "w")
    file.write(object.name+"\n")
    file.write(str(object.type)+"\n")
    file.write(str(object.lvl)+"\n")
    file.write(str(object.item)+"\n")
    file.write(str(object.weapon)+"\n")
    file.write(str(object.position[0])+"\n")
    file.write(str(object.position[1])+"\n")
    for i in range(len(object.bossHide)):
        file.write(str(object.bossHide[i])+"\n")
    for j in range(len(object.itemHide)):
        file.write(str(object.itemHide[j])+"\n")
    for k in range(len(object.weaponHide)):
        file.write(str(object.weaponHide[k])+"\n")
    file.close()
    return None


def loadState():
    location = "player"
    file = open(location, "r")
    array = ["Player Name", 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # playerName,
    # type(1-mage, 2-paladin, 3-warrior)
    # lvl
    # item
    # weapon
    # position[x,y],
    # bossHide[0]*4,
    # itemHide[0]*4,
    # weaponHide[0]*4,
    i = 0
    for line in file:
        if i == 0:
            array[i] = line.strip()
        elif i > 4 and i < 7:
            array[i] = float(line)
        else:
            array[i] = int(line)
        i += 1
    file.close()
    # print(array) # Debug
    return array