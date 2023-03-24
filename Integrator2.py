import scipy.integrate as integrate
import scipy.special as special
from scipy import optimize
import pygame

from numpy import sqrt

t = 1


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

xparams = [53,28,24,156]
yparams = [141,0,5,2]


goog = sqrt((xparams[3])**2+(yparams[3])**2)
length = 0

xprev = xparams[0]
yprev = yparams[0]

for i in range(round(goog)*50):
	t=i/(round(goog)*50)
	x = ((1-t)**3*(xparams[0]))+(3*(1-t)**2*t*(xparams[1]+xparams[0]))+(3*(1-t)*t**2*(xparams[2]+xparams[0]))+(t**3*(xparams[3]+xparams[0]))
	y = ((1-t)**3*(yparams[0]))+(3*(1-t)**2*t*(yparams[1]+yparams[0]))+(3*(1-t)*t**2*(yparams[2]+yparams[0]))+(t**3*(yparams[3]+yparams[0]))
	

	length += sqrt((x-xprev)**2+(y-yprev)**2)

	xprev = x
	yprev = y

	pygame.draw.circle(gameDisplay, black, (round(x*scale), round(y*scale)), 2)
print(length)

# xfunc = -3*(1-t)**2*xparams[0]+3*(xparams[1]+xparams[0])*(1-4*t+3*t**2)+3*(xparams[2]+xparams[0])*(6*t-9*t**2)+3*t**2*(xparams[3]+xparams[0])
# yfunc = -3*(1-t)**2*yparams[0]+3*(yparams[1]+yparams[0])*(1-4*t+3*t**2)+3*(yparams[2]+yparams[0])*(6*t-9*t**2)+3*t**2*(yparams[3]+yparams[0])

# xfunc = ((1-t)**3*(self.start[0]))+(3*(1-t)**2*t*(self.stroke[0][0]+self.start[0]))+(3*(1-t)*t**2*(self.stroke[1][0]+self.start[0]))+(t**3*(self.stroke[2][0]+self.start[0]))
# yfunc = ((1-t)**3*(self.start[1]))+(3*(1-t)**2*t*(self.stroke[0][1]+self.start[1]))+(3*(1-t)*t**2*(self.stroke[1][1]+self.start[1]))+(t**3*(self.stroke[2][1]+self.start[1]))

# xfunc = -3*(1-t)**2*(xparams[0])-6*(1-t)*t*(xparams[1]+xparams[0])+3*(1-t)**2*(xparams[1]+xparams[0])+6*t*(xparams[2]+xparams[0])-9*t**2*(xparams[2]+xparams[0])+3*t**2*(xparams[3]+xparams[0])
# yfunc = -3*(1-t)**2*(yparams[0])-6*(1-t)*t*(yparams[1]+yparams[0])+3*(1-t)**2*(yparams[1]+yparams[0])+6*t*(yparams[2]+yparams[0])-9*t**2*(yparams[2]+yparams[0])+3*t**2*(yparams[3]+yparams[0])

xfunc = 3*(1-t)**2*(xparams[1])+6*(1-t)*t*(xparams[2]-xparams[1])+3*t**2*(xparams[3]-xparams[2])
yfunc = 3*(1-t)**2*(yparams[1])+6*(1-t)*t*(yparams[2]-yparams[1])+3*t**2*(yparams[3]-yparams[2])


def integrand(t):
	return sqrt(xfunc**2+yfunc**2)

def integrater(t):
	return abs(integrate.quad(integrand,0,t,args=())[0])-ideal2

def length(ideal):
	global ideal2

	ideal2 = ideal 
	return optimize.newton(integrater, 1.5, fprime2=lambda x: 6 * x)

def integrater2(t):
	return integrate.quad(integrand,0,t,args=())[0]

def totlength():

 
	return integrater2(0.25)


# print(totlength())
# print(length(totlength()))
# print(integrate.quad(integrand,0,0.1,args=())[0])


pygame.draw.line(gameDisplay, green, (xparams[0]*scale,yparams[0]*scale), ((xparams[3]+xparams[0])*scale,(yparams[3]+yparams[0])*scale))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
			pygame.quit()
			quit()
	pygame.display.update()
	clock.tick(1)