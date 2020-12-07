from snake import Snake
from food import Food
from random import randrange

class GameLogic:
    def __init__(self, width, height):

        self.width=width
        self.height=height
        self.game_over=False

        self.next_direction = "right" #possibly change to ints or something else

        self.food = None # can we also have random start position for food?
        self.snake = Snake(self.generate_random_position()) # need to get starting position in ui

        self.add_new_food()

    def change_direction(self, direction):
        if (self.direction_is_legal(direction)):
            self.next_direction=direction

    def direction_is_legal(self, direction):
        if (direction == "up"):
            return False if (self.next_direction == "down") else True
        if (direction == "down"):
            return False if (self.next_direction == "up") else True
        if (direction == "right"):
            return False if (self.next_direction == "left") else True
        if (direction == "left"):
            return False if (self.next_direction == "right") else True


    def check_collision(self, position):
        return(self.check_self_collision(position) or self.check_borderposition(position))

    def check_self_collision(self, position):
        return(position in self.snake.body)

    def check_borderposition(self, position):
        return(
            position[0]<0 or
            position[1]<0 or
            position[0]>=self.width or
            position[1]>=self.height
        )

    def check_food_collision(self,position):

        if(self.food is None):
            return(False)
        return self.food.position==position

    def is_game_over(self):
        return(self.game_over)

    def do_turn(self):
        next_position=self.snake.get_head().copy()
        if (self.next_direction == "up"):
            next_position[1]-=1
        elif(self.next_direction == "down"):
            next_position[1]+=1
        elif(self.next_direction == "left"):
            next_position[0]-=1
        elif(self.next_direction == "right"):
            next_position[0]+=1

        if(self.check_collision(next_position)): #it hit a border
            self.game_over=True
            return

        remove_tail=True

        if(self.check_food_collision(next_position)):#do not remove tail - it ate a food
            remove_tail=False
            self.food=None
        self.snake.add_segment(next_position)

        if(remove_tail):
            self.snake.remove_segment()

        if(self.food is None):# food was eaten, add a new one
            self.add_new_food()


    def generate_random_position(self): #helper
        return([randrange(self.width),randrange(self.height)])

    def add_new_food(self):
        canidate_position=self.generate_random_position()
        while (self.check_self_collision(canidate_position)): #make sure that the food is not in the snake
            canidate_position=self.generate_random_position()

        self.food=Food(canidate_position)

    def debug_draw_board(self):
        board=[[" "]*self.width for _ in range(self.height)]

        for pos in self.snake.body:
            board[pos[1]][pos[0]]="*"
        board[self.snake.body[0][1]][self.snake.body[0][0]]="H"
        board[self.food.position[1]][self.food.position[0]]="F"

        for lin in board:
            print("| "+" ".join(lin)+" |")

if __name__ == '__main__':
    gl = GameLogic(5,5)
    while(True):
        gl.debug_draw_board()
        gl.next_direction=input()
        gl.do_turn()
        if(gl.game_over):
            break
