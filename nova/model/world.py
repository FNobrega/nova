def initialText(index):
    location = index
    file = open(location, "r")
    array = []
    for line in file:
        array.append(line.strip("\n"))
    file.close()
    # print(array)#Debug
    return array
