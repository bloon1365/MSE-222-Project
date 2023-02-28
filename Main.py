import os



#line
#circle
#ellipse
#path (bezier and everything)
#poly line

names = ['line', 'circle', 'ellipse', 'path', 'polyline']

path = os.path.dirname(__file__)
filename = path + "/test2.txt"


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

def pathinside()

class line():
	def __init__ (self,string):
		self.x1 = inside(string,string.find('x1'))
		self.y1 = inside(string,string.find('y1'))
		self.x2 = inside(string,string.find('x2'))
		self.y2 = inside(string,string.find('y2'))
		print(self.x1,self.y1,self.x2,self.y2)

class circle():
	def __init__ (self,string):
		self.cx = inside(string,string.find('cx'))
		self.cy = inside(string,string.find('cy'))
		self.r = inside(string,string.find('r'))
		print(self.cx,self.cy,self.r)

class ellipse():
	def __init__ (self,string):
		self.cx = inside(string,string.find('cx'))
		self.cy = inside(string,string.find('cy'))
		self.rx = inside(string,string.find('rx'))
		self.ry = inside(string,string.find('ry'))
		print(self.cx,self.cy,self.rx,self.ry)

class path():
	def __init__ (self,string):
		self.points = []
		self.stuff = inside(string,string.find('d'))
		print(self.stuff)
		inside






f = open(filename,"r")

file = f.read()
print(file, '\n\n')
strokes = []




for name in names:
	if name in file:
		short = file
		t = file.count(name)
		print(f'{t} {name} in svg')
		for i in range(t):
			short = short[short.find(name):-1]
			print(name)
			# print(short)
			if name == 'line':
				strokes.append(line(short))	
			if name == 'circle':
				strokes.append(circle(short))	
			if name == 'ellipse':
				strokes.append(ellipse(short))	
			if name == 'path':
				strokes.append(path(short))	
			short = short[2:-1]
	print('\n')
	
			







