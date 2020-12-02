import pygame
import userInterface


class Snake(pygame.sprite.Sprite):

    def __init__(self, initial_position, ui):
        self.body = [initial_position] #store position as tuple of x, ys
        self.ui = ui
        self.groups = ui.sprites, ui.snake_segment
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.rect = pygame.Rect(initial_position[0], initialPosition[1], userInterface.x_spacing, userInterface.y_spacing)
        self.position = Vector2(initialPosition[0], initialPosition[1])


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
