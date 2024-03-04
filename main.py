import pygame
import player

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
emuImg = pygame.image.load("emu.png")
#scale of the player, in pixels
player_scale = (80, 80)
#move speed (how much it moves (default is one grid))
player_move_speed = player_scale[0]
#starting position (top left)
starting_position = 320, 320 - 4  # "- 4" is to center it
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
            #print((player.playerRect.x, player.playerRect.y + 4))
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
    # draw
    pygame.display.flip()
    # fps
    clock.tick(60)
