import pygame


class Food(pygame.sprite.Sprite):
    def __init__(self, pos, ui=None):
        self.pos=pos
        if ui is not None:
            self.ui = ui
            self.groups = ui.sprites, ui.food
            pygame.sprite.Sprite.__init__(self, ui.groups)
    @property
    def position(self):
        return(pygame.Vector2(self.pos[0], self.pos[1]))
