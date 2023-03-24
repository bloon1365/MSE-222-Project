import scipy.integrate as integrate
import scipy.special as special
from scipy import optimize


from numpy import sqrt

t = 0

xfunc = -3*(1-t)**2*1+3*1*(1-4*t+3*t**2)+3*1*(6*t-9*t**2)+3*t**2*1
yfunc = -3*(1-t)**2*1+3*1*(1-4*t+3*t**2)+3*1*(6*t-9*t**2)+3*t**2*1

def integrand(t):
	return sqrt(xfunc**2+yfunc**2)

def integrater(t):
	return abs(integrate.quad(integrand,0,t,args=())[0])-ideal2

def length(ideal,xparams,yparams,):
	global ideal2
	global xfunc
	global yfunc

	xfunc = -3*(1-t)**2*xparams[0]+3*xparams[1]*(1-4*t+3*t**2)+3*xparams[2]*(6*t-9*t**2)+3*t**2*xparams[3]
	yfunc = -3*(1-t)**2*yparams[0]+3*yparams[1]*(1-4*t+3*t**2)+3*yparams[2]*(6*t-9*t**2)+3*t**2*yparams[3]

	ideal2 = ideal 
	return optimize.newton(integrater, 1.5, fprime2=lambda x: 6 * x)

def integrater2(t):
	return integrate.quad(integrand,0,t,args=())[0]

def totlength(xparams,yparams,t=1):
	global xfunc
	global yfunc

	xfunc = -3*(1-t)**2*xparams[0]+3*xparams[1]*(1-4*t+3*t**2)+3*xparams[2]*(6*t-9*t**2)+3*t**2*xparams[3]
	yfunc = -3*(1-t)**2*yparams[0]+3*yparams[1]*(1-4*t+3*t**2)+3*yparams[2]*(6*t-9*t**2)+3*t**2*yparams[3]
 
	return integrater2(1)-integrater2(1)


print(totlength([5,4,2,10],[11,2,3,4]))
print(length(19, [5,4,2,10],[11,2,3,4]))
