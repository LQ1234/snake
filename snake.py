class ClassName(object):
    """docstring for ."""

    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg

class Snake():
    
    def __init__(self, initial_position)
        self.body = [initial_position] #we are not using linked list anymore


    def move(self, position):
        pass

    def add_segment(position):#adds to beginning
        body.insert(0, position)

    def remove_segment():#removes from end
        body.pop(len(body) - 1)

    def size_of_snake():
        return len(body)

    def get_head():
        return body[0]
