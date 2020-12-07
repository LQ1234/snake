import pygame



class Snake(pygame.sprite.Sprite):

    def __init__(self, initial_position, ui=None):
        self.body = [initial_position] #store position as tuple of x, ys
        if ui is not None:
            self.ui = ui
            pygame.sprite.Sprite.__init__(ui.sprites, ui.snake_segment)

    def move(self, position):
        pass

    def add_segment(self, position):#adds to beginning
        self.body.insert(0, position)

    def remove_segment(self):#removes from end
        self.body.pop(len(self.body) - 1)

    def size_of_snake(self):
        return len(self.body)

    def get_head(self):
        return self.body[0]
