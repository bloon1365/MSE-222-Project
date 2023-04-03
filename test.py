import pygame
import math

def drawarms(x,y):
	arm1 = 2*100
	arm2 = 2*100
	origin = (150,150)
	x = x - origin[0]
	y = y - origin[1]

	# Calculate the angle theta2
	ceb = (x**2 + y**2 - arm1**2 - arm2**2) / (2 * arm1 * arm2)

	theta2 = math.acos(ceb)

	# Calculate the angle theta1
	k1 = y*(arm2*math.cos(theta2)+arm1)-x*arm2*math.sin(theta2)
	k2 = x*(arm2*math.cos(theta2)+arm1)+y*arm2*math.sin(theta2)
	theta1 = math.atan(k1/k2)

	point1 = (origin[0]+arm1*math.cos(theta1),origin[1]-arm1*math.sin(theta1))
	point2 = (point1[0]+arm2*math.cos(theta2+theta1),point1[1]-arm2*math.sin(theta2+theta1))


	pygame.draw.line(gameDisplay, green, (origin[0]*scale,origin[1]*scale), (point1[0]*scale,point1[1]*scale))
	pygame.draw.line(gameDisplay, green, (point1[0]*scale,point1[1]*scale), (point2[0]*scale,point2[1]*scale))


pygame.init()

scale = 3
display_width = 16*25*scale
display_height = 9*25*scale

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('yessir')

black = (0, 0, 0)
white = (255, 255, 255)
red = (255,0,0)
green = (0,255,0)

gameDisplay.fill(white)
clock = pygame.time.Clock()
scale = 3

point = (150,50)
drawarms(point[0],point[1])
pygame.draw.circle(gameDisplay, (255,0,0), (point[0]*scale, point[1]*scale), 5)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
			pygame.quit()
			quit()

	pygame.display.update()
	clock.tick(1)