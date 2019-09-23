from math import *
import numpy as np

x1 = 4 
x2 = np.array([1,3,5,7,9])

y1 = 19
y2 = np.array([2,4,6,8,10])

z1 = x1 + y1
z2 = x2 + y2

h1 = np.cos(x1)
h2 = np.cos(x2)


g1 = np.exp(2*pi*x1*1j)
g2 = np.exp(2*pi*x2*1j)

print ('datos :\n\n' + 'x1 = ' + str(x1) +'\n'+ 'x2 = '+str(x2)+'\n')
print ('y1 = '+str(y1)+'\n'+'y2 = '+str(y2)+' \n')
print ('z1 = x1 + y1 = ' + str(z1))
print ('z2 = x2 + y2 = ' + str(z2)+' \n')
print ('h1 = cos(x1) = ' + str(h1))
print ('h2 = cos(x2) = ' + str(h2)+' \n')
print ('g1 = exp(2*pi*x1*1j) = ' + str(g1))
print ('g2 = exp(2*pi*x2*1j) = ' + str(g2)+' \n')
print ('finish'+'\n')
