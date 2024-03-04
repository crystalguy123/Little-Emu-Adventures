import pygame


class Wall_Block:

    def __init__(self, sprite, position):
        self.position = position
        self.sprite = pygame.transform.scale(sprite, (77, 77))
        #print("position", (position[0] * 80, position[1] * 80))
        self.blockRect = sprite.get_rect(center=(position[0] * 80 + 40, position[1] * 80 + 40))