from numpy import sqrt

t = 1

xparams = [53,128,24,156]
yparams = [141,-125,25,2]


SCALE = 200*32

def length(ideal,xparams,yparams,t1,total):
	goog = total
	length = 0

	t=0

	t = t1
	for i in range(int(round(goog)*SCALE)):
		xprev = ((1-t1)**3*(xparams[0]))+(3*(1-t1)**2*t1*(xparams[1]+xparams[0]))+(3*(1-t1)*t1**2*(xparams[2]+xparams[0]))+(t1**3*(xparams[3]+xparams[0]))
		yprev = ((1-t1)**3*(yparams[0]))+(3*(1-t1)**2*t1*(yparams[1]+yparams[0]))+(3*(1-t1)*t1**2*(yparams[2]+yparams[0]))+(t1**3*(yparams[3]+yparams[0]))

		t += 1/(round(goog)*SCALE)
		x = ((1-t)**3*(xparams[0]))+(3*(1-t)**2*t*(xparams[1]+xparams[0]))+(3*(1-t)*t**2*(xparams[2]+xparams[0]))+(t**3*(xparams[3]+xparams[0]))
		y = ((1-t)**3*(yparams[0]))+(3*(1-t)**2*t*(yparams[1]+yparams[0]))+(3*(1-t)*t**2*(yparams[2]+yparams[0]))+(t**3*(yparams[3]+yparams[0]))

		currlength = sqrt((x-xprev)**2+(y-yprev)**2)

		if length + currlength >= ideal:
			if abs(length - ideal) > abs(length + currlength - ideal):
				return t
			else:
				return t - 1/(round(goog)*SCALE)

		length += currlength
		t1 = t
		xprev = x
		yprev = y
	print('reached end')
	return 1


def totlength(xparams,yparams):
	goog = sqrt((xparams[3])**2+(yparams[3])**2)
	length = 0

	xprev = xparams[0]
	yprev = yparams[0]

	for i in range(round(goog)*SCALE):
		t=i/(round(goog)*SCALE)
		x = ((1-t)**3*(xparams[0]))+(3*(1-t)**2*t*(xparams[1]+xparams[0]))+(3*(1-t)*t**2*(xparams[2]+xparams[0]))+(t**3*(xparams[3]+xparams[0]))
		y = ((1-t)**3*(yparams[0]))+(3*(1-t)**2*t*(yparams[1]+yparams[0]))+(3*(1-t)*t**2*(yparams[2]+yparams[0]))+(t**3*(yparams[3]+yparams[0]))

		length += sqrt((x-xprev)**2+(y-yprev)**2)

		xprev = x
		yprev = y


	return length

