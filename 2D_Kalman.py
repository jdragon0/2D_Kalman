import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interp

x = np.array([0,1,2,4,7,7,6,7,8,9,10,11,11,11])
y = np.array([0,2,5,7,6,4,2,0,1,3,4,3,2,2])
t = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13])

num = 50

tt = np.linspace(0,13,num)

fx = interp.interp1d(t,x,kind='quadratic')
xx = fx(tt)

fy = interp.interp1d(t,y,kind='quadratic')
yy = fy(tt)

w = np.random.randn(1,np.size(tt))*0.01
v = np.random.randn(1,np.size(tt))*0.01

A = np.array([[1, tt[1]],[0,1]])
H = np.array([1,0])[np.newaxis]
P = np.array([[1 ,0],[0,1]])

R = 0.01 
Q = 0.01 * np.array([[1 ,0],[0,1]]) 

initx = np.array([[0, 0],[xx[1],yy[1]]])
xh = initx

xxx = np.zeros(num)
yyy = np.zeros(num)

for k in range(num):
    xhp = A@xh+w[0][k]
    Pp = A@P@A.transpose()+Q
    K = Pp@H.transpose()/(H@Pp@H.transpose()+R)

    z = np.array([xx[k],yy[k]])+v[0][k]

    xh = xhp+K@(z-H@xhp)
    P = Pp-K@H@Pp

    xxx[k] = xh[0][0]
    yyy[k] = xh[0][1]

plt.plot(xxx,yyy,'x')
plt.plot(xx,yy,'o')
plt.grid()
plt.show()
