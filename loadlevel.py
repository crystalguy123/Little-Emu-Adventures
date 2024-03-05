def load(level):
    file = open(level, "r+")
    levelData = file.read().split(",")
    #print(levelData)
    playerPosition = []
    walls = []
    #print(len(levelData) + 1)
    for x in range(len(levelData) - 1):
        # player x starting point
        if x == 0:
            playerPosition.append(int(levelData[0]))
        # player y starting point
        if x == 1:
            playerPosition.append(int(levelData[1]))
        # start saving data, ignoring player starting point
        if x % 2 == 0 and not x == 0:
            #save position for object every second number
            #print(x)
            position = levelData[x]
            #check if object is a wall, then append to walls list
            if levelData[x + 1] == "1":
                walls.append(int(position))
    return playerPosition, walls