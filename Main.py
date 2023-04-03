import os
import pygame
import math
from Integratorfast import *
import matplotlib.pyplot as plt


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
			pygame.draw.circle(gameDisplay, black, (x*scale, y*scale), 2)

		pygame.draw.circle(gameDisplay, red, (self.accelpoint1[0]*scale, self.accelpoint1[1]*scale), 4)
		pygame.draw.circle(gameDisplay, red, (self.accelpoint2[0]*scale, self.accelpoint2[1]*scale), 4)

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
			self.accelpoint1 = ((self.stroke[2][0]+self.start[0]+xdist1), (self.stroke[2][1]+self.start[1]+ydist1))
		if slope1x <= 0 and slope1y >= 0:
			self.accelpoint1 = ((self.stroke[2][0]+self.start[0]-xdist1), (self.stroke[2][1]+self.start[1]+ydist1))
		if slope1x <= 0 and slope1y <= 0:
			self.accelpoint1 = ((self.stroke[2][0]+self.start[0]-xdist1), (self.stroke[2][1]+self.start[1]-ydist1))
		if slope1x >= 0 and slope1y <= 0:
			self.accelpoint1 = ((self.stroke[2][0]+self.start[0]+xdist1), (self.stroke[2][1]+self.start[1]-ydist1))

		if slope2x >= 0 and slope2y >= 0:
			self.accelpoint2 = ((self.start[0]-xdist2), (self.start[1]-ydist2))
		if slope2x <= 0 and slope2y >= 0:
			self.accelpoint2 = ((self.start[0]+xdist2), (self.start[1]-ydist2))
		if slope2x <= 0 and slope2y <= 0:
			self.accelpoint2 = ((self.start[0]+xdist2), (self.start[1]+ydist2))
		if slope2x >= 0 and slope2y <= 0:
			self.accelpoint2 = ((self.start[0]-xdist2), (self.start[1]+ydist2))
		# self.accelpoint2 = (0, 0)

	def points(self, num):
		self.drawlist = []	


		if num == 1:
			xdist = self.stroke[2][0]+self.start[0]-self.accelpoint1[0] 
			ydist = self.stroke[2][1]+self.start[1]-self.accelpoint1[1]

			for t in range(int(accelerationtime*frames)+1):	
				self.drawlist.append(((self.accelpoint1[0]+xdist*(t/(frames*accelerationtime))**2),(self.accelpoint1[1]+ydist*(t/(frames*accelerationtime))**2)))
		else:
			xdist = self.start[0]-self.accelpoint2[0]
			ydist = self.start[1]-self.accelpoint2[1]

			for t in range(int(accelerationtime*frames)+1):	
				self.drawlist.append(((self.accelpoint2[0]+xdist*(t/(frames*accelerationtime))**2),(self.accelpoint2[1]+ydist*(t/(frames*accelerationtime))**2)))


		self.drawlist.append((None,None))

		xparams = [self.start[0], self.stroke[0][0], self.stroke[1][0], self.stroke[2][0]]
		yparams = [self.start[1], self.stroke[0][1], self.stroke[1][1], self.stroke[2][1]]

		tot = totlength(xparams,yparams)
		cuts = math.ceil(tot/(conversion*speed)*frames)

		t1 = 0
		rev = []
		
		if num == 1:
			for i in range(cuts-1):
				t=i/(cuts)

				ideal = tot/(cuts)

				t1 = length(ideal,xparams,yparams,t1,tot)

				x = ((1-t1)**3*(xparams[0]))+(3*(1-t1)**2*t1*(xparams[1]+xparams[0]))+(3*(1-t1)*t1**2*(xparams[2]+xparams[0]))+(t1**3*(xparams[3]+xparams[0]))
				y = ((1-t1)**3*(yparams[0]))+(3*(1-t1)**2*t1*(yparams[1]+yparams[0]))+(3*(1-t1)*t1**2*(yparams[2]+yparams[0]))+(t1**3*(yparams[3]+yparams[0]))
				rev.append((x, y))
			rev.reverse()
		else:
			for i in range(cuts-1):
				t=i/(cuts)

				ideal = tot/(cuts)

				t1 = length(ideal,xparams,yparams,t1,tot)

				x = ((1-t1)**3*(xparams[0]))+(3*(1-t1)**2*t1*(xparams[1]+xparams[0]))+(3*(1-t1)*t1**2*(xparams[2]+xparams[0]))+(t1**3*(xparams[3]+xparams[0]))
				y = ((1-t1)**3*(yparams[0]))+(3*(1-t1)**2*t1*(yparams[1]+yparams[0]))+(3*(1-t1)*t1**2*(yparams[2]+yparams[0]))+(t1**3*(yparams[3]+yparams[0]))
				rev.append((x, y))

		self.drawlist += rev

		self.drawlist.append((None,None))

		rev = []
		if num == 2:
			xdist = self.stroke[2][0]+self.start[0]-self.accelpoint1[0] 
			ydist = self.stroke[2][1]+self.start[1]-self.accelpoint1[1]

			for t in range(int(accelerationtime*frames)+1):	
				rev.append(((self.accelpoint1[0]+xdist*(t/(frames*accelerationtime))**2),(self.accelpoint1[1]+ydist*(t/(frames*accelerationtime))**2)))
			rev.reverse()
			self.drawlist += rev
			return self.drawlist
		else:
			xdist = self.start[0]-self.accelpoint2[0]
			ydist = self.start[1]-self.accelpoint2[1]

			for t in range(int(accelerationtime*frames)+1):	
				rev.append(((self.accelpoint2[0]+xdist*(t/(frames*accelerationtime))**2),(self.accelpoint2[1]+ydist*(t/(frames*accelerationtime))**2)))
			rev.reverse()
			self.drawlist += rev
			return self.drawlist



		# for point in self.drawlist:
		# 	pygame.draw.circle(gameDisplay, (50,255,0), (round(point[0]*scale), round(point[1]*scale)), 2)

		
			






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

		pygame.draw.circle(gameDisplay, red, (self.accelpoint1[0]*scale, self.accelpoint1[1]*scale), 4)
		pygame.draw.circle(gameDisplay, red, (self.accelpoint2[0]*scale, self.accelpoint2[1]*scale), 4)

	def accelpoints(self):
		xdist = math.sqrt((accelerationdist**2)/(1+self.slope**2))*conversion
		ydist = math.sqrt((accelerationdist**2)/(1+(1/self.slope)**2))*conversion



		if self.slope > 0:
			if self.start[1][0]>self.start[0][0]:
				self.accelpoint1 = ((self.start[0][0]-xdist),(self.start[0][1]-ydist))
				self.accelpoint2 = ((self.start[1][0]+xdist),(self.start[1][1]+ydist))
			else:
				self.accelpoint1 = ((self.start[0][0]+xdist),(self.start[0][1]+ydist))
				self.accelpoint2 = ((self.start[1][0]-xdist),(self.start[1][1]-ydist))
		else:
			if self.start[1][0]<self.start[0][0]:
				self.accelpoint2 = ((self.start[1][0]-xdist),(self.start[1][1]+ydist))
				self.accelpoint1 = ((self.start[0][0]+xdist),(self.start[0][1]-ydist))
			else:
				self.accelpoint2 = ((self.start[1][0]+xdist),(self.start[1][1]-ydist))
				self.accelpoint1 = ((self.start[0][0]-xdist),(self.start[0][1]+ydist))

	def points(self,num):
		self.drawlist = []	


		if num == 2:
			xdist = -self.start[1][0]+self.accelpoint2[0]
			ydist = -self.start[1][1]+self.accelpoint2[1]

			for t in range(int(accelerationtime*frames)+1):	
				self.drawlist.append(((self.accelpoint2[0]-xdist*(t/(frames*accelerationtime))**2),(self.accelpoint2[1]-ydist*(t/(frames*accelerationtime))**2)))
		else:
			xdist = self.start[0][0]-self.accelpoint1[0]
			ydist = self.start[0][1]-self.accelpoint1[1]

			for t in range(int(accelerationtime*frames)):	
				self.drawlist.append(((self.accelpoint1[0]+xdist*(t/(frames*accelerationtime))**2),(self.accelpoint1[1]+ydist*(t/(frames*accelerationtime))**2)))
				pass

		self.drawlist.append((None,None))

		if num == 2:
			xdist = self.start[1][0]-self.start[0][0]
			ydist = self.start[1][1]-self.start[0][1]
			x = self.start[0][0]
			y = self.start[0][1]
		else:
			xdist = self.start[1][0]-self.start[0][0]
			ydist = self.start[1][1]-self.start[0][1]
			x = self.start[0][0]
			y = self.start[0][1]

		rev = []
		length = math.sqrt((xdist)**2+(ydist)**2)
		cuts = math.ceil(length/(conversion*speed)*frames)
		stepx = xdist/cuts
		stepy = ydist/cuts


		for t in range(cuts):
			rev.append((x,y))
			x += stepx
			y += stepy

		if num == 2:
			rev.reverse()

		self.drawlist += rev

		self.drawlist.append((None,None))

		rev = []
		if num == 1:
			xdist = self.start[1][0]-self.accelpoint2[0]
			ydist = self.start[1][1]-self.accelpoint2[1]
			
			for t in range(int(accelerationtime*frames)+1):	
				rev.append(((self.accelpoint2[0]+xdist*(t/(frames*accelerationtime))**2),(self.accelpoint2[1]+ydist*(t/(frames*accelerationtime))**2)))
		else:
			xdist = self.start[0][0]-self.accelpoint1[0]
			ydist = self.start[0][1]-self.accelpoint1[1]

			for t in range(int(accelerationtime*frames)):	
				rev.append(((self.accelpoint1[0]+xdist*(t/(frames*accelerationtime))**2),(self.accelpoint1[1]+ydist*(t/(frames*accelerationtime))**2)))
			
		rev.reverse()
		self.drawlist += rev
		return self.drawlist
		






f = open(filename,"r")

file = f.read()

strokes = []




for name in names:
	if name in file:
		short = file
		t = file.count(name)
		for i in range(t):
			short = short[short.find(name):]
			if name == '<line':
				strokes.append(line(short))	
			if name == '<circle':
				strokes.append(circle(short))	
			if name == '<ellipse':
				strokes.append(ellipse(short))	
			if name == '<path':
				s = inside(short,short.find('     d'))
				if s.__contains__('c') or s.__contains__('C'):
					strokes.append(path(short))	
				else:
					strokes.append(line2(short))	


			short = short[2:]


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
	for stroke in strokes:
		bestdist = dist(stroke, start)
		if bestdist[0] < best:
			best = bestdist[0]
			currstroke = stroke
			strokenum=0
		if bestdist[1] < best:
			best = bestdist[1]
			currstroke = stroke
			strokenum=1

	return currstroke,strokenum

def connect(start, end):
	grrr=[]
	length = math.sqrt((end[0]-start[0])**2+(end[1]-start[1])**2)
	time = math.sqrt(length/(acceleration*conversion))

	cuts = math.ceil(time*frames)
	xdist = (end[0]-start[0])/2
	ydist = (end[1]-start[1])/2



	for t in range(cuts):
		x = start[0] + xdist*(t/(cuts))**2
		y = start[1] + ydist*(t/(cuts))**2
		grrr.append((x,y))
	rev = []
	for t in range(cuts):
		x = end[0] - xdist*(1-(t/(cuts)))**2
		y = end[1] - ydist*(1-(t/(cuts)))**2
		grrr.append((x,y))

	return grrr

correction = 0
prevangle = 0
def drawarms(x,y):
	global correction
	global prevangle
	arm1 = 0.75*conversion
	arm2 = 0.75*conversion
	origin = (150,100)
	x = x - origin[0]
	y = y - origin[1]

	# Calculate the angle theta2
	ceb = (x**2 + y**2 - arm1**2 - arm2**2) / (2 * arm1 * arm2)

	theta2 = math.acos(ceb)

	# Calculate the angle theta1	
	k1 = y*(arm2*math.cos(theta2)+arm1)-x*arm2*math.sin(theta2)
	k2 = x*(arm2*math.cos(theta2)+arm1)+y*arm2*math.sin(theta2)
	theta1 = math.atan(k1/k2)

	#jump detector **VERY BAD**
	theta1 += correction
	if abs(theta1-prevangle) > math.pi - 0.5:
		correction -= math.pi
		theta1 -= math.pi

	prevangle = theta1


	point1 = (origin[0]-arm1*math.cos(theta1),origin[1]-arm1*math.sin(theta1))
	point2 = (point1[0]-arm2*math.cos(theta2+theta1),point1[1]-arm2*math.sin(theta2+theta1))




	pygame.draw.line(gameDisplay, green, (origin[0]*scale,origin[1]*scale), (point1[0]*scale,point1[1]*scale))
	pygame.draw.line(gameDisplay, green, (point1[0]*scale,point1[1]*scale), (point2[0]*scale,point2[1]*scale))




#motion profiling
conversion = 100 #px/m
acceleration = 0.75 #m/s^2 = 0.1 #m/s
speed = 0.25
accelerationtime = (speed/acceleration) #time needed to accelerate 1s
accelerationdist = (1/2)*(acceleration)*(accelerationtime)**2 #distance needed to accelerate 0.1m
frames = 24 #frames per second



start = (100,100)
head(start)

for stroke in strokes:
	stroke.accelpoints()
	# stroke.draw()
	





number = len(strokes)
strokeleft = strokes

t=0
pointslist = []
while len(strokeleft)>0:
	t+=1
	current = closest(strokeleft, start)
	strokeleft.remove(current[0])


	if current[1] == 0:
		# pygame.draw.line(gameDisplay, green, (start[0]*scale,start[1]*scale), (current[0].accelpoint1[0]*scale,current[0].accelpoint1[1]*scale))
		pointslist += connect(start, current[0].accelpoint1)
		start = current[0].accelpoint2
		pointslist += current[0].points(1)
	else:
		# pygame.draw.line(gameDisplay, green, (start[0]*scale,start[1]*scale), (current[0].accelpoint2[0]*scale,current[0].accelpoint2[1]*scale))
		pointslist += connect(start, current[0].accelpoint2)
		start = current[0].accelpoint1
		pointslist += current[0].points(2)
	print(f'{t}/{number}')







putlist = []
flag = False
for point in pointslist:
	if point == (None,None):
		if flag == True:
			flag = False
		else:
			flag = True
		continue
	if flag == True:
		putlist.append(point)
	pygame.draw.circle(gameDisplay, (0,0,0), (point[0]*scale, point[1]*scale), 8)
	drawarms(point[0],point[1])

	for t in putlist:
		pygame.draw.circle(gameDisplay, (50,255,0), (t[0]*scale, t[1]*scale), 2)

	for event in pygame.event.get():
		if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
			pygame.quit()
			quit()

	pygame.display.update()
	clock.tick(frames)
	gameDisplay.fill(white)




def pythag(point1,point2):
	return math.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)

speed = []
velocity = []
acceler = []
prev = pointslist[0]
for x in pointslist[1:]:
	if x == (None, None):
		continue
	speed.append(abs(pythag(x,prev)/conversion*frames))
	velocity.append(((x[0]-prev[0]),(x[1]-prev[1])))
	prev = x

prev = velocity[0]
for x in velocity[1:]:
	acceler.append(abs(pythag(x,prev)/conversion*frames**2))
	prev = x


# plt.plot(pointslist, 'b')
plt.plot(speed, 'g')
plt.plot(acceler, 'r')
plt.show()