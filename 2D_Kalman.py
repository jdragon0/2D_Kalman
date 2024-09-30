import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interp

x = np.array([0,1,2,4,7,7,6,7,8,9,10,9,6,4])*10
y = np.array([0,2,5,7,6,4,2,0,1,3,4,3,2,2])*10
t = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13])

num = 1000

tt = np.linspace(0,t[-1],num)
dt = tt[1] - tt[0]

fx = interp.interp1d(t,x,kind='quadratic')
xx = fx(tt)

fy = interp.interp1d(t,y,kind='quadratic')
yy = fy(tt)


A = np.matrix([[1,dt,dt*dt/2],[0,1,dt],[0,0,1]])
H = np.matrix([1,0,0])
P = np.eye(A.shape[0])

v_rho = 6
w_rho = 0.01

R = 6 # measurement noise covariance
Q = np.matrix([[dt**4/4,dt**3/2,dt**2/2],[dt**3/2,dt**2,dt],[dt**2/2,dt,1]])*2
# Q = np.matrix([[dt,0,0],[0,dt,0],[0,0,1]])*1

initx = np.matrix([[0, 0],[0, 0],[0.1, 0.1]])
xh = initx

xxx = np.zeros(num)
yyy = np.zeros(num)
ex = np.zeros(num)
ey = np.zeros(num)
for k in range(num):
    w = np.matrix(np.random.randn(3,2)) * w_rho
    xh = A@xh + w
    Pp = A@P@A.transpose()+Q
    K = Pp@H.transpose()@np.linalg.inv(H@Pp@H.transpose()+R)

    v = np.matrix(np.random.randn(1,2)) * v_rho
    z = np.matrix([xx[k],yy[k]]) + v

    xh = xh+K@(z-H@xh)
    P = Pp-K@H@Pp

    xxx[k] = xh.item(0)
    yyy[k] = xh.item(1)

    ex[k] = z.item(0)
    ey[k] = z.item(1)

plt.plot(ex,ey,'o',color='darkorange')
plt.plot(xxx,yyy,'x',color='g')
plt.plot(xx,yy,linestyle='dashed',color='k',linewidth=3)
plt.grid()
plt.show()
