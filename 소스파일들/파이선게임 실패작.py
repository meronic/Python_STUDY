import pygame
import sys
import time
import random

from pygame.locals import *

WIDTH = 800
HEIGHT = 600

###############################
GRID = 20
GRID_WIDTH = WIDTH / GRID
GRID_HEIGHT = HEIGHT / GRID
##############################

WHITE = (255, 255, 255)
GREEN = (0, 50, 0)
ORANGE = (250, 150, 0)
##################################

UP = [0, -1]
DOWN = [0, 1]
LEFT = [-1, 0]
RIGHT = [1, 0]

#################################
class Python(object):
	def __init__(self):
		self.create()
		self.color = GREEN

	def create(self):
		self.length = 2
		self.positions = [((WIDTH/2),(HEIGHT/2))]
		self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

	def control(self, xy): ##뱀의 움직임 통제
		if (xy[0] * -1, xy[1] * -1) == self.direction : 
			return
		else : 
			self.direction == xy

	def move(self) : 
		cur = self.positions[0]
		x,y = self.direction
		new = (((cur[0] + (x * GRID)) % WIDTH) , (cur[1] + (y * GRID)) % HEIGHT)

		if new in self.positions[2:] : 
			self.create()

		else : 
			self.positions.insert(0, new)
			if len(self.positions) > self.length :
				self.positions.pop()

	def eat(self) : 
		self.length += 1

	def draw(self, surface) : 
		for p in self.positions : 
			draw_object(surface, self.color, p)



def draw_object(surface, color , pos) : 
	r = pygame.Rect((pos[0], pos[1]), (GRID, GRID))
	pygame.draw.rect(surface, color, r)

class Feed(object):
	def __init__(self) : 
		self.position = (0, 0)
		self.color = ORANGE
		self.create()	

	def create(self) : 
		self.position = (random.randint(0,GRID_WIDTH - 1)*GRID, random.randint(0,GRID_HEIGHT - 1)*GRID)

	def draw(self, surface) : 
		draw_object(surface, self.color, self.position)

def check_eat(python, feed):
	if python.positions[0] == feed.position : 
		python.eat()
		feed.create()			

if __name__ == '__main__':
	python = Python()
	feed = Feed()

	pygame.init()
	window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
	pygame.display.set_caption('First Pygame Programm My Life')

	#이해 못한 부분
	surface = pygame.Surface(window.get_size()) ##??
	surface = surface.convert() ##??
	surface.fill(WHITE)

	
	#시간 설정
	clock = pygame.time.Clock()

	#키 설정 ??
	pygame.key.set_repeat(1, 40)

	#window blit 설정 이것도 모르겠음
	window.blit(surface, (0, 0))
	

	while True : 

		

		for event in pygame.event.get() : 
			if event.type == QUIT : 
				pygame.quit()
				sys.exit()

			
			if event.type == KEYDOWN : 
				if event.key == K_UP : 
					python.control(UP)
					print("up")

				elif event.key == K_DOWN : 
					python.control(DOWN)
					print("down")

				elif event.key == K_LEFT : 
					python.control(LEFT)
					print("left")

				elif event.key == K_RIGHT : 
					python.control(RIGHT)
					print("right")





		surface.fill(WHITE)
		
		check_eat(python, feed)
		speed = (10 + python.length) / 2

		python.draw(surface)
		feed.draw(surface)
		window.blit(surface, (0, 0))
		python.move()
		pygame.display.flip()
		pygame.display.update()
		clock.tick(10)

