import pygame


class Food(pygame.sprite.Sprite):
    def __init__(self, position, ui=None):
        self.position=position
        if ui is not None:
            self.ui = ui
            self.groups = ui.sprites, ui.food
            pygame.sprite.Sprite.__init__(self, ui.groups)
