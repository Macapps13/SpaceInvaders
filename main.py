import pygame, sys

class Game:
	def __innit__(self):
		pass

	def run(self):
		pass
		#update and draw all sprite groups



if __name__ == '__main__':
	pygame.init()
	screen_width = 600
	screen_height = 600
	screen = pygame.display.set_mode((screen_width,screen_height))
	clock = pygame.time.Clock()
	game = Game()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit(0)
		
		screen.fill((30,30,30))
		game.run()

		pygame.display.flip()
		clock.tick(60)
