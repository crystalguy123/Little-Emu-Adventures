import pygame
import player
import wallblock
import loadlevel, translateposition

pygame.init()
pygame.display.set_caption("LITTLE MAN ADVENTURES")
screen_size = (1280, 720)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
running = True
centerX = screen.get_width() / 2
centerY = screen.get_height() / 2
center = (centerX, centerY)

# ---PLAYER VARIABLES---
#image
emuImg = pygame.image.load("emuPixelized.png")
# scale of the player, in pixels
player_scale = (80, 80)
# move speed (how much it moves (default is one grid))
player_move_speed = player_scale[0]
# starting position, as a list
startingPositionList = loadlevel.load(r"LevelOne.txt")[0]
#translate the list's numbers into coordinates
starting_position = [(translateposition.translate(startingPositionList[0])[0] + 4) * 80,
                     (translateposition.translate(startingPositionList[1])[1] + 4) * 80]
#initialize the player object
player = player.Player(emuImg, player_move_speed, player_scale, starting_position)
# ---GRID VARIABLES---
# amount of left and right cells
grid_x_count = 9
# amount of up and down cells
grid_y_count = 15
# size of the cells (square, in pixels)
grid_cell_size = 80
# color of the lines
grid_color = (255, 255, 255)
# thickness of the lines
grid_thickness = 3

walls = []
blockImg = pygame.image.load("block.png")
wallPositionList = loadlevel.load(r"LevelOne.txt")[1]
for x in wallPositionList:
    walls.append(wallblock.Wall_Block(blockImg, translateposition.translate(x)))


def checkCollision(direction):
    #reset the player bounding box to the player's position
    playerBoundingBox = pygame.Rect(player.playerRect)
    match direction:
        case "north":
            #move bounding box up
            playerBoundingBox.y -= 80
        case "east":
            #move bounding box right
            playerBoundingBox.x += 80
        case "south":
            #move bounding box down
            playerBoundingBox.y += 80
        case "west":
            #move bounding box left
            playerBoundingBox.x -= 80

    #---CHECK EVERY WALL FOR COLLISION---
    for wall in walls:
        collide = pygame.Rect.colliderect(wall.blockRect, playerBoundingBox)
        if collide:
            #if colliding, return True
            return True
    #if no collision is happening, return False
    return False


while running:
    for event in pygame.event.get():
        #if hit the x
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            exit()
        #look for key presses
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    #if not going to collide above, then move up
                    if not checkCollision("north"):
                        player.move("north")
                if event.key == pygame.K_a:
                    # if not going to collide to left, then move left
                    if not checkCollision("west"):
                        player.move("west")
                if event.key == pygame.K_s:
                    # if not going to collide below, then move down
                    if not checkCollision("south"):
                        player.move("south")
                if event.key == pygame.K_d:
                    # if not going to collide to right, then move right
                    if not checkCollision("east"):
                        player.move("east")

    # wipe previous frame
    screen.fill("pink")

    # draw grid lines
    for i in range(grid_x_count + 1):
        pygame.draw.line(screen, grid_color, (0, i * grid_cell_size), (screen_size[0], i * grid_cell_size),
                         grid_thickness)
    for i in range(grid_y_count + 1):
        pygame.draw.line(screen, grid_color, (i * grid_cell_size, 0), (i * grid_cell_size, screen_size[1]),
                         grid_thickness)

    # blit some stuff
    screen.blit(player.sprite, player.playerRect)
    #blit all the walls
    for x in walls:
        screen.blit(x.sprite, x.blockRect)

    # draw
    pygame.display.flip()
    # fps
    clock.tick(60)
