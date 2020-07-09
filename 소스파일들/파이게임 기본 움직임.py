import pygame

import time


pygame.init()

size = [400, 300]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("First Game in My Life")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

x = 50
y = 50
vel = 10


done = False
clock = pygame.time.Clock()

while not done : 



	clock.tick(60)

	for event in pygame.event.get():

		if event.type == pygame.QUIT : 
			done = True

	## key option ##############
	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] :
		x -= vel

	if keys[pygame.K_RIGHT] :
		x += vel

	if keys[pygame.K_UP] :
		y -= vel

	if keys[pygame.K_DOWN] :
		y += vel

	######################################3	


	screen.fill(WHITE)

	pygame.draw.circle(screen, BLACK, [x, y], 20)
	pygame.display.update()



	pygame.display.flip()



pygame.quit()