import pygame
import userInterface


class Snake(pygame.sprite.Sprite):

    def __init__(self, initial_position, ui=None):
        self.body = [initial_position] #store position as tuple of x, ys
        if ui is not None:
            self.ui = ui
            self.groups = ui.sprites, ui.snake_segment
            pygame.sprite.Sprite.__init__(self, self.groups)

    @property
    def rect(self):
        head=self.get_head()
        return(pygame.Rect(head[0], head[1], userInterface.x_spacing, userInterface.y_spacing))
    @property
    def position(self):
        head=self.get_head()
        return(pygame.Vector2(head[0], head[1]))


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

    def draw(self):
        pass # snake needs to have move done to do update and draw

    def update(self):
        pass
