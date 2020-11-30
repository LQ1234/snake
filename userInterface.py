import pygame
#from gamelogic import GameLogic
# don't need to worry about gamelogic, need to just print stuff out


#-----------PROPERTIES FOR THE WINDOW---------------------
# all coordinates will be stored as (x, y), top left is 0,0
WINDOW_WIDTH, WINDOW_HEIGHT = 400, 400

BOARD_WIDTH, BOARD_HEIGHT = 40, 40


window_size = (WINDOW_WIDTH, WINDOW_HEIGHT) # in pixels
board_size = (BOARD_WIDTH, BOARD_HEIGHT) # not in pixels, in squares


#not final here
"""
window_size = pygame.Vector2(WINDOW_WIDTH, WINDOW_HEIGHT)
board_size = pygame.Vectro2(BOARD_WIDTH, BOARD_HEIGHT)
"""

#space between each
x_spacing = window_size[0] / board_size[0]
y_spacing = window_size[1] / board_size[1]


#-------------TILE CONSTANTS --------------




#----------CONSTANTS--------------

BOARD_COLOR = (55, 250, 10) # default board color in RGB

FRAMERATE = 10



pygame.init()
screen = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()
#----------------------------------------------------------



class UserInterface:
	#use pygame library to set refresh rate and open window

	def __init__(self):
		self.snake = [] #figure out initial snake position

		self.food = pygame.sprite.Group()
		self.snake_segments = pygame.sprite.Group()
		self.sprites = pygame.sprite.Group()
		#self.logic = GameLogic()


	def get_keyboard_input(self): #give game_logic key input
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT or event.key == ord('a'):
				return ("left")
			if event.key == pygame.K_RIGHT or event.key == ord('d'):
				return ("right")
			if event.key == pygame.K_UP or event.key == ord('w'):
				return ("up")
			if event.key == pygame.K_DOWN or event.key == ord('s'):
				return ("down")

	def blit_screen(self): #use blit method for pygame to display objects
		pass

	def run_game(self):
		loop = True
		while loop: #main game loop
			clock.tick(FRAMERATE) #sets how many times per second loop will run

			screen.fill(BOARD_COLOR)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					loop = False

			pygame.display.flip()

a = UserInterface()
a.run_game()
