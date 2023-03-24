import os
import pygame
import math
from Integrator import *


#line
#circle
#ellipse
#path (bezier and everything)
#poly line

names = ['<line', '<circle', '<ellipse', '<path']

path = os.path.dirname(__file__)
# filename = path + "/test2.svg"
filename = path + "/test3.svg"


def inside(string, value):
	flag = False
	num = ''
	for i in string[value:-1]:
		if flag == False:
			if i == '"':
				flag = True
		else:
			if i == '"':
				return num
			num += i

def point(string):
	global chicken 
	chicken = 0
	num1 = ''
	num2 = ''
	flag = False
	# print(string)
	for i in string:
		# print(i)
		# print(num1,num2)
		if i == ' ' or i == ',':
			if flag == True:
				return (float(num1),float(num2))
			flag = True
		else:
			if flag == False:
				num1 += i
			else:
				num2 += i
		chicken += 1

def points(string):
	yup = [1,2,3,4,5,6,7,8,9,0,'-']
	pointslist = []
	while True:
		if len(string) < 3:
			return pointslist
		pointslist.append(point(string))


		string = string[chicken+1:]

def pointsabs(string):
	yup = [1,2,3,4,5,6,7,8,9,0,'-']
	pointslist = []
	while True:
		if len(string) < 3:
			pointslist[1] = (pointslist[1][0]-pointslist[0][0],pointslist[1][1]-pointslist[0][1])
			pointslist[2] = (pointslist[2][0]-pointslist[3][0],pointslist[2][1]-pointslist[3][1])
			return pointslist
		pointslist.append(point(string))


		string = string[chicken+1:]
		



def pathinside(string):
	strokes = []
	value = 0
	goose = ['m','c','s','z']
	for i in string:
		if i == 'm' or i == 'M':
			strokes.append(point(string[value+2:]))
		if i == 'c':
			strokes.append(points(string[value+2:]+' '))
		if i == 'C'	:	
			strokes.append(points(string[value+2:]+' '))
			strokes[-1][-3] = (strokes[-1][-3][0]-strokes[0][0],strokes[-1][-3][1]-strokes[0][1])
			strokes[-1][-2] = (strokes[-1][-2][0]-strokes[0][0],strokes[-1][-2][1]-strokes[0][1])
			strokes[-1][-1] = (strokes[-1][-1][0]-strokes[0][0],strokes[-1][-1][1]-strokes[0][1])

		value +=1
	return strokes


class line():
	def __init__ (self,string):
		self.x1 = float(inside(string,string.find('x1')))
		self.y1 = float(inside(string,string.find('y1')))
		self.x2 = float(inside(string,string.find('x2')))
		self.y2 = float(inside(string,string.find('y2')))
		# print(self.x1,self.y1,self.x2,self.y2)

		self.slope = (self.x2-self.x1)/(self.y2-self.y1)
		self.intercept = self.y1 - self.slope*self.x1

	def draw(self):
		slopex = self.x2-self.x1
		slopey = self.y2-self.y1
		length = math.sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)
		x=self.x1*scale
		y=self.y1*scale
		for i in range(round(length)*scale):
			x+=slopex/length
			y+=slopey/length
			pygame.draw.circle(gameDisplay, black, (round(x), round(y)), 2)


class circle():
	def __init__ (self,string):
		self.cx = inside(string,string.find('cx'))
		self.cy = inside(string,string.find('cy'))
		self.r = inside(string,string.find('r'))
		# print(self.cx,self.cy,self.r)

class ellipse():
	def __init__ (self,string):
		self.cx = inside(string,string.find('cx'))
		self.cy = inside(string,string.find('cy'))
		self.rx = inside(string,string.find('rx'))
		self.ry = inside(string,string.find('ry'))
		# print(self.cx,self.cy,self.rx,self.ry)

class path():
	def __init__ (self,string):
		self.stuff = inside(string,string.find('d'))
		# print(self.stuff)
		temp = pathinside(self.stuff)
		self.start = temp[0]
		self.stroke = temp[1]
		# print(self.stroke)

	def draw(self):
		length= math.sqrt((self.stroke[0][0]-self.stroke[-1][0])**2+(self.stroke[0][1]-self.stroke[-1][1])**2)

		for i in range(round(length)*scale*5):
			t=i/(round(length)*scale*5)
			x = ((1-t)**3*(self.start[0]))+(3*(1-t)**2*t*(self.stroke[0][0]+self.start[0]))+(3*(1-t)*t**2*(self.stroke[1][0]+self.start[0]))+(t**3*(self.stroke[2][0]+self.start[0]))
			y = ((1-t)**3*(self.start[1]))+(3*(1-t)**2*t*(self.stroke[0][1]+self.start[1]))+(3*(1-t)*t**2*(self.stroke[1][1]+self.start[1]))+(t**3*(self.stroke[2][1]+self.start[1]))
			pygame.draw.circle(gameDisplay, black, (round(x*scale), round(y*scale)), 2)

	def accelpoints(self):
		slope1x = (3*(self.stroke[2][0]-self.stroke[1][0]))
		slope1y = (3*(self.stroke[2][1]-self.stroke[1][1]))
		try:
			slope1 = slope1y/slope1x #t=1
		except:
			slope1 = 0


		xdist1 = math.sqrt((accelerationdist**2)/(1+slope1**2))*conversion 
		try:
			ydist1 = math.sqrt((accelerationdist**2)/(1+(1/slope1)**2))*conversion
		except:
			ydist1 = math.sqrt((accelerationdist**2)/(1+(99999999)**2))*conversion


		slope2x = (3*(self.stroke[0][0]))
		slope2y = (3*(self.stroke[0][1]))

		try:
			slope2 = slope2y/slope2x #t=0
		except:
			slope2 = 0
		
		xdist2 = math.sqrt((accelerationdist**2)/(1+slope2**2))*conversion
		try:
			ydist2 = math.sqrt((accelerationdist**2)/(1+(1/slope2)**2))*conversion
		except:
			ydist2 = math.sqrt((accelerationdist**2)/(1+(999999999)**2))*conversion


		
		if slope1x >= 0 and slope1y >= 0:
			pygame.draw.circle(gameDisplay, red, (round((self.stroke[2][0]+self.start[0]+xdist1)*scale), round((self.stroke[2][1]+self.start[1]+ydist1)*scale)), 4)
			self.accelpoint1 = ((self.stroke[2][0]+self.start[0]+xdist1), (self.stroke[2][1]+self.start[1]+ydist1))
		if slope1x <= 0 and slope1y >= 0:
			pygame.draw.circle(gameDisplay, red, (round((self.stroke[2][0]+self.start[0]-xdist1)*scale), round((self.stroke[2][1]+self.start[1]+ydist1)*scale)), 4)
			self.accelpoint1 = ((self.stroke[2][0]+self.start[0]-xdist1), (self.stroke[2][1]+self.start[1]+ydist1))
		if slope1x <= 0 and slope1y <= 0:
			pygame.draw.circle(gameDisplay, red, (round((self.stroke[2][0]+self.start[0]-xdist1)*scale), round((self.stroke[2][1]+self.start[1]-ydist1)*scale)), 4)
			self.accelpoint1 = ((self.stroke[2][0]+self.start[0]-xdist1), (self.stroke[2][1]+self.start[1]-ydist1))
		if slope1x >= 0 and slope1y <= 0:
			pygame.draw.circle(gameDisplay, red, (round((self.stroke[2][0]+self.start[0]+xdist1)*scale), round((self.stroke[2][1]+self.start[1]-ydist1)*scale)), 4)
			self.accelpoint1 = ((self.stroke[2][0]+self.start[0]+xdist1), (self.stroke[2][1]+self.start[1]-ydist1))

		if slope2x >= 0 and slope2y >= 0:
			pygame.draw.circle(gameDisplay, red, (round((self.start[0]-xdist2)*scale), round((self.start[1]-ydist2)*scale)), 4)
			self.accelpoint2 = ((self.start[0]-xdist2), (self.start[1]-ydist2))
		if slope2x <= 0 and slope2y >= 0:
			pygame.draw.circle(gameDisplay, red, (round((self.start[0]+xdist2)*scale), round((self.start[1]-ydist2)*scale)), 4)
			self.accelpoint2 = ((self.start[0]+xdist2), (self.start[1]-ydist2))
		if slope2x <= 0 and slope2y <= 0:
			pygame.draw.circle(gameDisplay, red, (round((self.start[0]+xdist2)*scale), round((self.start[1]+ydist2)*scale)), 4)
			self.accelpoint2 = ((self.start[0]+xdist2), (self.start[1]+ydist2))
		if slope2x >= 0 and slope2y <= 0:
			pygame.draw.circle(gameDisplay, red, (round((self.start[0]-xdist2)*scale), round((self.start[1]+ydist2)*scale)), 4)
			self.accelpoint2 = ((self.start[0]-xdist2), (self.start[1]+ydist2))
		# self.accelpoint2 = (0, 0)

	def points(self):
		self.drawlist = []	



		xdist = self.stroke[2][0]+self.start[0]-self.accelpoint1[0] 
		ydist = self.stroke[2][1]+self.start[1]-self.accelpoint1[1]

		for t in range(int(accelerationtime*frames)+1):	
			self.drawlist.append(((self.accelpoint1[0]+xdist*(t/(frames*accelerationtime))**2),(self.accelpoint1[1]+ydist*(t/(frames*accelerationtime))**2)))



		xdist = self.start[0]-self.accelpoint2[0]
		ydist = self.start[1]-self.accelpoint2[1]

		for t in range(int(accelerationtime*frames)+1):	
			self.drawlist.append(((self.accelpoint2[0]+xdist*(t/(frames*accelerationtime))**2),(self.accelpoint2[1]+ydist*(t/(frames*accelerationtime))**2)))

		xparams = [self.start[0], self.stroke[0][0], self.stroke[1][0], self.stroke[2][0]]
		yparams = [self.start[1], self.stroke[0][1], self.stroke[1][1], self.stroke[2][1]]

		tot = totlength(xparams,yparams)
		cuts = math.ceil(tot/(conversion*speed)*frames)

		t1 = 0
		for i in range(cuts):	
			# print(i)
			# print(tot/(conversion*speed)*frames)
			t=i/cuts
			# print(t)
			ideal = tot/cuts
			# print('\n\n\n\n')
			# print(tot)
			# print(ideal)
			# print('\n\n\n\n')
			t1 = length(ideal,xparams,yparams,t1)
			# print(t1)
			# print('')

			x = ((1-t1)**3*(xparams[0]))+(3*(1-t1)**2*t1*(xparams[1]+xparams[0]))+(3*(1-t1)*t1**2*(xparams[2]+xparams[0]))+(t1**3*(xparams[3]+xparams[0]))
			y = ((1-t1)**3*(yparams[0]))+(3*(1-t1)**2*t1*(yparams[1]+yparams[0]))+(3*(1-t1)*t1**2*(yparams[2]+yparams[0]))+(t1**3*(yparams[3]+yparams[0]))
			self.drawlist.append((x, y))
			# print(t1)





		for point in self.drawlist:
			pygame.draw.circle(gameDisplay, (50,255,0), (round(point[0]*scale), round(point[1]*scale)), 2)
			






class line2():
	def __init__ (self,string):
		self.stuff = inside(string,string.find('d'))
		self.start = points(self.stuff[2:]+' ')
		# print(self.start)

		self.slope = (self.start[1][1]-self.start[0][1])/(self.start[1][0]-self.start[0][0])

	def draw(self):
		slopex = self.start[1][0]-self.start[0][0]
		slopey = self.start[1][1]-self.start[0][1]
		length = math.sqrt((self.start[1][0]-self.start[0][0])**2+(self.start[1][1]-self.start[0][1])**2)

		x=self.start[0][0]*scale
		y=self.start[0][1]*scale
		for i in range(round(length)*scale):
			x+=slopex/length
			y+=slopey/length
			pygame.draw.circle(gameDisplay, black, (round(x), round(y)), 2)

	def accelpoints(self):
		xdist = math.sqrt((accelerationdist**2)/(1+self.slope**2))*conversion
		ydist = math.sqrt((accelerationdist**2)/(1+(1/self.slope)**2))*conversion
		# print(xdist,ydist)
		if self.start[1][0] < self.start[0][0]:
			pygame.draw.circle(gameDisplay, red, (round(self.start[0][0]-xdist)*scale, round(self.start[0][1]-ydist)*scale), 4)
			pygame.draw.circle(gameDisplay, red, (round(self.start[1][0]+xdist)*scale, round(self.start[1][1]+ydist)*scale), 4)
			self.accelpoint1 = ((self.start[0][0]-xdist),(self.start[0][1]-ydist))
			self.accelpoint2 = ((self.start[1][0]+xdist),(self.start[1][1]+ydist))
		else:
			pygame.draw.circle(gameDisplay, red, (round(self.start[1][0]+xdist)*scale, round(self.start[1][1]+ydist)*scale), 4)
			pygame.draw.circle(gameDisplay, red, (round(self.start[0][0]-xdist)*scale, round(self.start[0][1]-ydist)*scale), 4)
			self.accelpoint1 = ((self.start[1][0]+xdist),(self.start[1][1]+ydist))
			self.accelpoint2 = ((self.start[0][0]-xdist),(self.start[0][1]-ydist))

	def points(self):
		pass

		






f = open(filename,"r")

file = f.read()
# print(file, '\n\n')
strokes = []




for name in names:
	if name in file:
		short = file
		t = file.count(name)
		# print(f'{t} {name} in svg')
		for i in range(t):
			short = short[short.find(name):]
			# print(name)
			# print(short)
			if name == '<line':
				strokes.append(line(short))	
			if name == '<circle':
				strokes.append(circle(short))	
			if name == '<ellipse':
				strokes.append(ellipse(short))	
			if name == '<path':
				# print(short)
				s = inside(short,short.find('d'))
				if s.__contains__('c') or s.__contains__('C'):
					strokes.append(path(short))	
				else:
					strokes.append(line2(short))	


			short = short[2:]
	# print('\n')
	
			
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



def head(point):
	pygame.draw.circle(gameDisplay, red, (round(point[0])*scale, round(point[1])*scale), 10)

def dist(thing, start):
	return (math.sqrt((thing.accelpoint1[0]-start[0])**2+(thing.accelpoint1[1]-start[1])**2), math.sqrt((thing.accelpoint2[0]-start[0])**2+(thing.accelpoint2[1]-start[1])**2))

def closest(strokes, start):
	best = 999999
	# print(start)
	for stroke in strokes:
		bestdist = dist(stroke, start)
		if bestdist[0] < best:
			best = bestdist[0]
			currstroke = stroke
			strokenum=0
			# print('better found:')
			# print(stroke.accelpoint1)
			# print(best,'\n')
		if bestdist[1] < best:
			best = bestdist[1]
			currstroke = stroke
			strokenum=1
			# print('better found:')
			# print(stroke.accelpoint2)
			# print(best,'\n','\n')

	return currstroke,strokenum


#motion profiling
conversion = 100 #px/m
acceleration = 0.1 #m/s^2 = 0.1 #m/s
speed = 0.25
accelerationtime = (speed/acceleration) #time needed to accelerate 1s
accelerationdist = (1/2)*(acceleration)*(accelerationtime)**2 #distance needed to accelerate 0.1m
frames = 4 #frames per second



start = (10,10)
head(start)

for stroke in strokes:
	stroke.draw()
	stroke.accelpoints()
	stroke.points()

# for stroke in strokes[30:40]:
# 	stroke.points()




strokeleft = strokes



while len(strokeleft)>0:
	current = closest(strokeleft, start)
	strokeleft.remove(current[0])

	if current[1] == 0:
		# current[0].points(current[0].accelpoint2,current[0].accelpoint1)
		pygame.draw.line(gameDisplay, green, (start[0]*scale,start[1]*scale), (current[0].accelpoint1[0]*scale,current[0].accelpoint1[1]*scale))
		start = current[0].accelpoint2
	else:
		pygame.draw.line(gameDisplay, green, (start[0]*scale,start[1]*scale), (current[0].accelpoint2[0]*scale,current[0].accelpoint2[1]*scale))
		# current[0].points(current[0].accelpoint1,current[0].accelpoint2)
		start = current[0].accelpoint1







# strokes[3].draw()
# strokes[3].accelpoints()


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
			pygame.quit()
			quit()
	pygame.display.update()
	clock.tick(1000/frames)