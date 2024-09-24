import numpy as np
import sympy
import matplotlib.pyplot as plt


def wait():
    input("Press Enter to continue...")
    
    
def trajectory(a0,v0,x0,t):
    return a0*pow(t,2)+v0*t+x0
Duration = 10 #s
N = 100 #number of point
dt = Duration/N #Time increment
t = np.linspace(0,10,num=100)
print(t)
x01 = 30
x02 = 0
x03 = -60
v01 = 15
v02 = 10
v03 = 5
a01 = 0
a02 = 2
a03 = 3
a12 = -4

t_Banana = 7 #s

x1 = trajectory(a01,v01,x01,t)
x2 = trajectory(a02,v02,x02,t)
x3 = trajectory(a03,v03,x03,t)
#wait()
t12 = t_Banana
i_Banana = t_Banana/N
v12 = v02
x12 = a02*t12**2+v02*t12+x02
xx = x2 + trajectory(a12,v02,x12,t)
for i in range(N):
    tt = i*dt
    if tt>=t_Banana:
        x2[i] = trajectory(a12,v02,x12,(tt-t12))
    else:
        x2[i] = x2[i]
    
plt.plot(t, x1, label='Mario')
plt.plot(t, x2, label='Toad')
#plt.plot(t, x3, label='Wario')
# Add labels and title
plt.xlabel('Time [s]')
plt.ylabel('Trajectory [m]')
plt.title('Mario Kart Race')
plt.legend()

from sympy.solvers import solve
from sympy import Symbol
x = Symbol('x')
intercept=solve(a02*x**2+v02*x+x02-a01*x**2-v01*x-x01, x)
t_intercept=intercept[1]
x_intercept=v01*t_intercept+x01
print(x_intercept)

plt.axhline(y=x_intercept, color='black', linestyle='--')
plt.axvline(x=t_intercept, color='black', linestyle='--')
plt.text(6, 0,'t = {} s'.format(round(float(t_intercept),2)))
plt.text(0,120,'x = {} m'.format(round(float(x_intercept),2)))
plt.xlim(0,7)
plt.show()
#wait()

plt.plot(t, x1, label='Mario')
plt.plot(t, x2, label='Toad')
plt.plot(t, x3, label='Wario')
# Add labels and title
plt.xlabel('Time [s]')
plt.ylabel('Trajectory [m]')
plt.title('Mario Kart Race')
plt.legend()


#Winner
i = 0 
X = max(x1[i],x2[i],x3[i])
while X<=250:
    if X==x1[i]:
        Winner = 'Mario'
    elif X==x2[i]:
        Winner = 'Toad'
    else:
        Winner = 'Wario'
    i=i+1
    X = max(x1[i],x2[i],x3[i])
iMax = i-1

#Finish Line
tMax = t[iMax]
plt.axvline(x=tMax, color='green', linestyle='--')
plt.axhline(y=250, color='black', linestyle='--')
plt.text(3,150,'And the winner is ... {}\nTatatata!!!\nBest Time: {} s'.format(Winner,round(tMax,2)))

plt.xlim(0,10)
plt.show()
plt.savefig("MarioKart.png")
