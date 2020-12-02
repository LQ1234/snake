import pygame


class Food(pygame.sprite.Sprite):
    def __init__(self, position, ui):
        self.position=position
        self.ui = ui
        self.groups = ui.sprites, ui.food
        pygame.sprite.Sprite.__init__(self, ui.groups)
