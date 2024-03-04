import pygame


class Player:

    def __init__(self, sprite, speed, scale, position):
        self.sprite = pygame.transform.scale(sprite, scale)
        self.speed = speed
        self.scale = scale
        self.position = position
        self.playerRect = sprite.get_rect(center=position)
        self.TOP_LEFT = (0, 0)
        self.TOP_RIGHT = (1200, 0)
        self.BOTTOM_LEFT = (0, 640)
        self.BOTTOM_RIGHT = (1200, 640)
        self.position_in_grid = (int(self.playerRect.x / 80), (int(self.playerRect.y + 4) / 80))
        self.previous = "east"

    def move(self, direction):

        match direction:
            case "north":
                if self.position_in_grid[1] >= 1:
                    self.playerRect.y -= self.speed
                    self.previous = "north"
            case "east":
                if self.position_in_grid[0] <= 14:
                    if not self.previous == "east":
                        self.sprite = pygame.transform.flip(self.sprite, True, False)
                    self.playerRect.x += self.speed
                    self.previous = "east"
            case "south":
                if self.position_in_grid[1] <= 7:
                    self.playerRect.y += self.speed
                    self.previous = "south"
            case "west":
                if self.position_in_grid[0] >= 1:
                    if not self.previous == "west":
                        self.sprite = pygame.transform.flip(self.sprite, True, False)
                    self.playerRect.x -= self.speed
                    self.previous = "west"

        self.position_in_grid = (int(self.playerRect.x / 80), int((self.playerRect.y + 4) / 80))
        print(self.position_in_grid)
