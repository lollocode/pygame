import pygame, sys

pygame.init()

screen = pygame.display.set_mode((640, 480))

screen.fill([0,0,0])
pygame.draw.rect(screen,[255,255,255],(200,150,100,50))
pygame.display.set_caption("First Pygame Application")


while True:

	clock = pygame.time.Clock()

	clock.tick(50)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
	  		sys.exit()
	pygame.display.flip()