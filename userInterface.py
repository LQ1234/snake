import pygame
#from gamelogic import GameLogic
# don't need to worry about gamelogic, need to just print stuff out


#-----------PROPERTIES FOR THE WINDOW---------------------
# all coordinates will be stored as (x, y), top left is 0,0
window_size = (400, 400) # in pixels
board_size = (40, 40) # not in pixels, in squares

#space between each 
x_spacing = window_size[0] / board_size[0]
y_spacing = window_size[1] / board_size[1]



pygame.init()
screen = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()
#----------------------------------------------------------



class UserInterface:
	#use pygame library to set refresh rate and open window
	
	def __init__(self):
		self.snake = [] #figure out initial snake position
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
			clock.tick(10) #sets how many times per second loop will run

			screen.fill((55, 250, 10))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					loop = False

			pygame.display.flip()

a = UserInterface()
a.run_game()