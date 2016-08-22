# Libraries


# Functions
def moviment(object,directions,speed, x, y):
    screenAjust = [(800-x)/2, (600-y)/2]
    if directions == 1:
        if object.position[1] < 310 - 32 - screenAjust[1]:
            if(object.position[1] <= -300 - screenAjust[1] or object.position[1] >= -250 - screenAjust[1] or
                object.position[0] <= -720 - screenAjust[0] and object.position[0] >= -790 - screenAjust[0] or
                object.position[0] <= 80 - screenAjust[0] and object.position[0] >= 10- screenAjust[0]):
                object.position[1] += speed
                object.charImageWorld[4].play()
        object.frame = 0
    elif directions == 2:
        if object.position[1] > -840 - screenAjust[1]:
            if(object.position[1] <= -270 - screenAjust[1] or object.position[1] >= -230 - screenAjust[1] or
                object.position[0] <= -720 - screenAjust[0] and object.position[0] >= -790 - screenAjust[0] or
                object.position[0] <= 80 - screenAjust[0] and object.position[0] >= 10 - screenAjust[0]):
                object.position[1] -= speed
                object.charImageWorld[4].play()
        object.frame = 1
    elif directions == 3:
        if object.position[0] < 350 - screenAjust[0]:
            if(object.position[0] <= -510 - screenAjust[0] or object.position[0] >= -460 - screenAjust[0] or
                (object.position[1] <= -620 - screenAjust[1] and object.position[1] >= -660 - screenAjust[1]) or
                (object.position[1] <= 100 - screenAjust[1] and object.position[1] >= 50 - screenAjust[1])):
                object.position[0] += speed
                object.charImageWorld[4].play()
        object.frame = 2
    elif directions == 4:
        if object.position[0] > -1160 - screenAjust[0]:
            if(object.position[0] <= -500 - screenAjust[0] or object.position[0] >= -450 - screenAjust[0] or
                (object.position[1] <= -620 - screenAjust[1] and object.position[1] >= -660 - screenAjust[1]) or
                (object.position[1] <= 100 - screenAjust[1] and object.position[1] >= 50 - screenAjust[1])):
                object.position[0] -= speed
                object.charImageWorld[4].play()
        object.frame = 3
    object.charImageWorld[4] = object.charImageWorld[object.frame]
    return None


def moviment1(object,directions,speed):
    if directions == 1:
        object.position[1] += speed
        object.frame = 0
    elif directions == 2:
        object.position[1] -= speed
        object.frame = 1
    elif directions == 3:
        object.position[0] += speed
        object.frame = 2
    elif directions == 4:
        object.position[0] -= speed
        object.frame = 3
    object.charImageWorld[4] = object.charImageWorld[object.frame]
    return None