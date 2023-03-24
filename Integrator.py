import scipy.integrate as integrate
import scipy.special as special
from scipy import optimize
# import pygame

from numpy import sqrt

t = 1


# pygame.init()

# scale = 3
# display_width = 16*25*scale
# display_height = 9*25*scale

# gameDisplay = pygame.display.set_mode((display_width, display_height))
# pygame.display.set_caption('yessir')

# black = (0, 0, 0)
# white = (255, 255, 255)
# red = (255,0,0)
# green = (0,255,0)

# gameDisplay.fill(white)
# clock = pygame.time.Clock()

xparams = [53,128,24,156]
yparams = [141,-125,25,2]



# 	pygame.draw.circle(gameDisplay, black, (round(x*scale), round(y*scale)), 2)
# print(length)

# xfunc = -3*(1-t)**2*xparams[0]+3*(xparams[1]+xparams[0])*(1-4*t+3*t**2)+3*(xparams[2]+xparams[0])*(6*t-9*t**2)+3*t**2*(xparams[3]+xparams[0])
# yfunc = -3*(1-t)**2*yparams[0]+3*(yparams[1]+yparams[0])*(1-4*t+3*t**2)+3*(yparams[2]+yparams[0])*(6*t-9*t**2)+3*t**2*(yparams[3]+yparams[0])

# xfunc = ((1-t)**3*(self.start[0]))+(3*(1-t)**2*t*(self.stroke[0][0]+self.start[0]))+(3*(1-t)*t**2*(self.stroke[1][0]+self.start[0]))+(t**3*(self.stroke[2][0]+self.start[0]))
# yfunc = ((1-t)**3*(self.start[1]))+(3*(1-t)**2*t*(self.stroke[0][1]+self.start[1]))+(3*(1-t)*t**2*(self.stroke[1][1]+self.start[1]))+(t**3*(self.stroke[2][1]+self.start[1]))

# xfunc = -3*(1-t)**2*(xparams[0])-6*(1-t)*t*(xparams[1]+xparams[0])+3*(1-t)**2*(xparams[1]+xparams[0])+6*t*(xparams[2]+xparams[0])-9*t**2*(xparams[2]+xparams[0])+3*t**2*(xparams[3]+xparams[0])
# yfunc = -3*(1-t)**2*(yparams[0])-6*(1-t)*t*(yparams[1]+yparams[0])+3*(1-t)**2*(yparams[1]+yparams[0])+6*t*(yparams[2]+yparams[0])-9*t**2*(yparams[2]+yparams[0])+3*t**2*(yparams[3]+yparams[0])

xfunc = 3*(1-t)**2*(xparams[1])+6*(1-t)*t*(xparams[2]-xparams[1])+3*t**2*(xparams[3]-xparams[2])
yfunc = 3*(1-t)**2*(yparams[1])+6*(1-t)*t*(yparams[2]-yparams[1])+3*t**2*(yparams[3]-yparams[2])




def length(ideal,xparams,yparams,t1):
	goog = sqrt((xparams[3])**2+(yparams[3])**2)
	length = 0

	xprev = ((1-t1)**3*(xparams[0]))+(3*(1-t1)**2*t1*(xparams[1]+xparams[0]))+(3*(1-t1)*t1**2*(xparams[2]+xparams[0]))+(t1**3*(xparams[3]+xparams[0]))
	yprev = ((1-t1)**3*(yparams[0]))+(3*(1-t1)**2*t1*(yparams[1]+yparams[0]))+(3*(1-t1)*t1**2*(yparams[2]+yparams[0]))+(t1**3*(yparams[3]+yparams[0]))
	t=0

	t = t1
	# print(t1)
	for i in range(int(round(goog)*50*(1-t1))):
		# print(length)
		# print(ideal)
		if length >= ideal:
			return t

		t += 1/(round(goog)*50)
		x = ((1-t)**3*(xparams[0]))+(3*(1-t)**2*t*(xparams[1]+xparams[0]))+(3*(1-t)*t**2*(xparams[2]+xparams[0]))+(t**3*(xparams[3]+xparams[0]))
		y = ((1-t)**3*(yparams[0]))+(3*(1-t)**2*t*(yparams[1]+yparams[0]))+(3*(1-t)*t**2*(yparams[2]+yparams[0]))+(t**3*(yparams[3]+yparams[0]))

		length += sqrt((x-xprev)**2+(y-yprev)**2)

		xprev = x
		yprev = y
	return 1




def totlength(xparams,yparams):
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

	return length


# print(totlength())
# print(length(totlength()))
# print(integrate.quad(integrand,0,0.1,args=())[0])



# while True:
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
# 			pygame.quit()
# 			quit()
# 	pygame.display.update()
# 	clock.tick(1)