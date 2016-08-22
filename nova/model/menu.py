def readHistory(location):
    file = open(location, "r")
    array = []
    for line in file:
        array.append(line.strip("\n"))
    file.close()
    return array
