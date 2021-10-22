# =============================================================================
#  ***** num_derivatives.py *****
#  Python script to plot numerical derivative information.
#
#  Author:     Ryan Clement
#  Created:    July 2021
#
#  Change Log:
#  Who:
#  Date:       MM/DD/YYY
#  What:
#
#  Who:
#  Date:       MM/DD/YYYY
#  What:
# =============================================================================

import numpy as np
from matplotlib import pyplot as plt

### Functions
def parabola(x):
    return 10*x - x**2
def paraDeriv(x):
    return 10 - 2*x
def slope(xa,xb,ya,yb):
    return (yb-ya)/(xb-xa)
def getYN(xa,xb,xd,ya,yb,yd,x):
    return yd + slope(xa,xb,ya,yb)*(x-xd)
def getYE(xd,yd,x):
    return yd + paraDeriv(xd)*(x-xd)
def nD(xo,dx):
    return (np.sin(xo+dx) - np.sin(xo))/dx
def nD2(xo,dx):
    return (np.sin(xo+dx) - np.sin(xo-dx))/(2.0*dx)

a = 0
b = 10
xPoints = np.linspace(a,b,11)
yPoints = parabola(xPoints)
xSmooth = np.linspace(a,b,101)
ySmooth = parabola(xSmooth)
x3 = xPoints[3]
x4 = xPoints[4]
x5 = xPoints[5]
x6 = xPoints[6]
x7 = xPoints[7]
y3 = yPoints[3]
y4 = yPoints[4]
y5 = yPoints[5]
y6 = yPoints[6]
y7 = yPoints[7]
xDers = np.array([x3,x7])

# Exact
ya = getYE(x5,y5,x3)
yb = getYE(x5,y5,x7)
yExact = np.array([ya,yb])

# Centered
ya = getYN(x4,x6,x5,y4,y4,y5,x3)
yb = getYN(x4,x6,x5,y4,y4,y5,x7)
yCent = np.array([ya,yb])
# print('Centered: ',(yb-ya)/(x6-x4))

# Left
ya = getYN(x4,x5,x5,y4,y5,y5,x3)
yb = getYN(x4,x5,x5,y4,y5,y5,x7)
yLeft = np.array([ya,yb])
# print('Left: ',(yb-ya)/(x5-x4))

# Right
ya = getYN(x5,x6,x5,y5,y4,y5,x3)
yb = getYN(x5,x6,x5,y5,y4,y5,x7)
yRight = np.array([ya,yb])
# print('Right: ',(yb-ya)/(x6-x5))

# Plot
figP, axP = plt.subplots()
axP.set_title(r'Parabola: $y = 10x - x^2$')
axP.set_xlabel('x')
axP.set_ylabel('y')
axP.set_xticks(xPoints)
axP.plot(xSmooth, ySmooth, 'k')
axP.plot(xPoints, yPoints, 'ko')
axP.plot([x4,x4],[0,y4],'--b')
axP.plot([x5,x5],[0,y5],'--',color='purple')
axP.plot([x6,x6],[0,y6],'--r')
axP.plot(xDers,yCent,'y',label='Centered')
axP.plot(xDers,yLeft,'b',label='Left')
axP.plot(xDers,yRight,'r',label='Right')
axP.plot(xDers,yExact,'--k',label='Exact')
axP.legend()
# figP.savefig('parabola_derivative.png')

### Sine Error
x0 = 1.0
exact = np.cos(x0)
dx = np.logspace(-16,-1,1000)
diff = np.abs(nD(x0,dx) - exact)
# Plot
figC, axC = plt.subplots()
axC.set_xlabel(r'$\Delta x$')
axC.set_ylabel('Error')
# axC.set_xlim([1e-16,1e-1])
axC.loglog(dx,diff,'r')
# figC.savefig('sine_derivative.png')

### Sine Order
dx = np.logspace(-9,-1,1000)
diffFO = np.abs(nD(x0,dx) - exact)
diffSO = np.abs(nD2(x0,dx) - exact)
# Plot
figS, axS = plt.subplots()
axS.set_xlabel(r'$\Delta x$')
axS.set_ylabel('Error')
axS.loglog(dx,diffFO,'b',label=r'$O(\Delta x)$')
axS.loglog(dx,diffSO,'r',label=r'$O(\Delta x^2)$')
axS.legend()
# figS.savefig('sine_derivative_order.png')

