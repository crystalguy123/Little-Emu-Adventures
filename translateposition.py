def translate(position):
    if position < 16:
            #0 - 15
            #row 0
        coordinatePosition = [position, 0]
    elif position < 32:
            #16 - 31
            # row 1
        coordinatePosition = [position % 16, 1]
    elif position < 48:
            #32 - 47
            # row 2
        coordinatePosition = [position % 32, 2]
    elif position < 64:
            #48 - 63
            # row 3
            coordinatePosition = [position % 48, 3]
    elif position < 80:
            #64 - 79
            # row 4
            coordinatePosition = [position % 64, 4]
    elif position < 96:
            #80 - 95
            # row 5
            coordinatePosition = [position % 80, 5]
    elif position < 112:
            #96 - 111
            # row 6
            coordinatePosition = [position % 96, 6]
    elif position < 128:
            #112 - 127
            # row 7
            coordinatePosition = [position % 112, 7]
    elif position > 127:
            #set position to default (128)
            # row 8
            coordinatePosition = [position % 128, 8]
    else:
        coordinatePosition = [8, 15]
    return coordinatePosition