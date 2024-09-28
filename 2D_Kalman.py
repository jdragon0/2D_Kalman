import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interp

x = np.array([0,1,2,4,7,7,6,7,8,9,10,9,6,4])
y = np.array([0,2,5,7,6,4,2,0,1,3,4,3,2,2])
t = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13])

num = 50

tt = np.linspace(0,t[-1],num)
dt = tt[1] - tt[0]

fx = interp.interp1d(t,x,kind='quadratic')
xx = fx(tt)

fy = interp.interp1d(t,y,kind='quadratic')
yy = fy(tt)


A = np.matrix([[1,dt,dt*dt/2],[0,1,dt],[0,0,1]])
H = np.matrix([1,0,0])
P = np.eye(A.shape[0])

R = 0.1
Q = np.eye(3)*0.1 

initx = np.matrix([[0, 0],[0, 0],[0.1, 0.1]])
xh = initx

xxx = np.zeros(num)
yyy = np.zeros(num)
ex = np.zeros(num)
ey = np.zeros(num)
for k in range(num):
    w = np.matrix(np.random.randn(3,2))* 0.1
    xh = A@xh + w
    Pp = A@P@A.transpose()+Q
    K = Pp@H.transpose()@np.linalg.inv(H@Pp@H.transpose()+R)

    v = np.matrix(np.random.randn(1,2)) *0.1
    z = np.matrix([xx[k],yy[k]]) + v

    xh = xh+K@(z-H@xh)
    P = Pp-K@H@Pp

    xxx[k] = xh.item(0)
    yyy[k] = xh.item(1)

    ex[k] = z.item(0)
    ey[k] = z.item(1)

plt.plot(xx,yy)
plt.plot(ex,ey,'o')
plt.plot(xxx,yyy,'x')
plt.grid()
plt.show()
