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

#---PLAYER VARIABLES---
emuImg = pygame.image.load("emuPixelized.png")
#scale of the player, in pixels
player_scale = (80, 80)
#move speed (how much it moves (default is one grid))
player_move_speed = player_scale[0]
#starting position (top left)
startingPositionList = loadlevel.load(r"LevelOne.txt")[0]
starting_position = [(translateposition.translate(startingPositionList[0])[0] + 4) * 80, (translateposition.translate(startingPositionList[1])[1] + 4) * 80]
print(starting_position)
player = player.Player(emuImg, player_move_speed, player_scale, starting_position)
player.sprite = pygame.transform.flip(player.sprite, True, False)
#---GRID VARIABLES---
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

#open the file "LevelOne" as "read and write"
#level_one_txt = open(r"LevelOne.txt", "r+")
#loadlevel.load(r"LevelOne.txt")
walls = []
blockImg = pygame.image.load("block.png")
wallPositionList = loadlevel.load(r"LevelOne.txt")[1]
for x in wallPositionList:
    walls.append(wallblock.Wall_Block(blockImg, translateposition.translate(x)))


# walls = []
# for x in range(5):
#     walls.append(wallblock.Wall_Block(blockImg, (200 + (x * 80), 200)))
# #test_block = wallblock.Wall_Block(blockImg, (200, 200))


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.move("north")
            if event.key == pygame.K_a:
                player.move("west")
            if event.key == pygame.K_s:
                player.move("south")
            if event.key == pygame.K_d:
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
    #screen.blit(test_block.sprite, test_block.blockRect)
    for x in walls:
        screen.blit(x.sprite, x.blockRect)
    # draw
    pygame.display.flip()
    # fps
    clock.tick(60)
