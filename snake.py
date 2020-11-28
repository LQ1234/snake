class Snake():
    
    def __init__(self, initial_position):
        self.body = [initial_position] #store position as tuple of x, y

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
