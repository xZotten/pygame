# this allows us to use code from
# the open-source pygame library
# throughout this file
from constants import *
import pygame

def main():
	pygame.init()
	print("Starting Asteroids!")
	print("Screen width:" + str(SCREEN_WIDTH))
	print("Screen height:" + str(SCREEN_HEIGHT))
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill("black")
		pygame.display.flip()

if __name__ == "__main__":
    main()
