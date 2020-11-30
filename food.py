import pygame


class Food(pygame.sprite.Sprite):
    def __init__(self, position, ui):
        self.position=position
        self.ui = ui
        pygame.sprite.Sprite.__init__(ui.sprites, ui.food)
