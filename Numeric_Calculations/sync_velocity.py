"""
    (c) MSU_Space Team
"""

# Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import copy

def polar(x, y):
    r = np.sqrt(x**2 + y**2)
    if y >= 0 and r != 0:
        phi = np.arccos(x/r)
    elif y < 0:
        phi = (-1)*np.arccos(x/r)
    else:
        phi = 0

    return (r, phi)

# Constants
G = 8.644e-10
L2_Distance = 1.5e6

# Mass of objects
Mass_Of_Sun = 1.98892e27
Mass_Of_Moon = 7.0349e19
Mass_Of_Earth = 5.9742e21
Mass_Of_JW = 6.2

# Mass of objects
GM = G * Mass_Of_Moon
GE = G * Mass_Of_Earth
GJW = G * Mass_Of_JW
GS = G * Mass_Of_Sun

# Earth
x_earth_0 = 152098238.0
y_earth_0 = 0.0
vx_earth_0 = 0.0
vy_earth_0 = 105372.0

# James Webb
x_JW_0 = 153598238.0
y_JW_0 = 0.0
vx_JW_0 = 0
vy_JW_0 = 1160.4152844 + vy_earth_0 # 1160.4153 + vy_earth_0

# Addition constants
t_0 = 0
T = 365 * 24
M = 5000
tau = (T - t_0) / M
t = t_0
S = 4
b = [1/6, 1/3, 1/3, 1/6]


# JW, Moon, Earth (x, y, vx, vy)
u_0 = np.array([x_JW_0, y_JW_0, vx_JW_0, vy_JW_0, x_earth_0, y_earth_0, vx_earth_0, vy_earth_0])
u = [np.copy(u_0)]

# James Webb
dot_x_JW = lambda U: U[2]
dot_y_JW = lambda U: U[3]
dot_vx_JW = lambda U: (-1)*(GS*U[0])/((U[0]**2 + U[1]**2)**(3/2)) - (GE*(U[0] - U[4]))/(((U[0] - U[4])**2 + (U[1] - U[5])**2)**(3/2))
dot_vy_JW = lambda U: (-1)*(GS*U[1])/((U[0]**2 + U[1]**2)**(3/2)) - (GE*(U[1] - U[5]))/(((U[0] - U[4])**2 + (U[1] - U[5])**2)**(3/2))


# Earth
dot_x_earth = lambda U: U[6]
dot_y_earth = lambda U: U[7]
dot_vx_earth = lambda U: (-1)*(GS*U[4])/((U[4]**2 + U[5]**2)**(3/2)) + (GJW*(U[0] - U[4]))/(((U[0] - U[4])**2 + (U[1] - U[5])**2)**(3/2))
dot_vy_earth = lambda U: (-1)*(GS*U[5])/((U[4]**2 + U[5]**2)**(3/2)) + (GJW*(U[1] - U[5]))/(((U[0] - U[4])**2 + (U[1] - U[5])**2)**(3/2))


# Function for system of differential equations
function = lambda U: np.array([dot_x_JW(U), dot_y_JW(U), dot_vx_JW(U), dot_vy_JW(U), dot_x_earth(U), dot_y_earth(U), dot_vx_earth(U), dot_vy_earth(U)])



def summa(k, omega):
    if k == 1:
        return 0
    elif k == 2:
        return 0.5 * np.copy(np.array(omega[0]))
    elif k == 3:
        return 0.5 * np.copy(np.array(omega[1]))
    elif k == 4:
        return np.copy(np.array(omega[2]))


def summa_2(omega):
    summa = b[0] * omega[0]
    for i in range(1, S):
        summa += b[i] * np.copy(omega[i])
    return summa



for m in range(M):

    omega = []
    for k in range(1, S+1):
    
        p = np.copy(u[m]) + tau * np.copy(summa(k, omega))

        omega.append(function([p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7]]))

    u.append(np.copy(u[m]) + tau * np.copy(summa_2(omega)))


X_JW = []
Y_JW = []
VX_JW = []
VY_JW = []
X_Earth = []
Y_Earth = []
# 0 1 JW
# 4 5 earth
for i in range(len(u)):
    X_JW.append(u[i][0])
    Y_JW.append(u[i][1])
    VX_JW.append(u[i][2])
    VY_JW.append(u[i][3])
    X_Earth.append(u[i][4])
    Y_Earth.append(u[i][5])





L2_X = 0
L2_Y = 0

L2_X_list = []
L2_Y_list = []

def L2(x, y):
    if x < 0:
        tmp_x = - np.sqrt(L2_Distance**2 / (1 + (y/x) ** 2))    
    else:
        tmp_x = np.sqrt(L2_Distance**2 / (1 + (y/x) ** 2))
    tmp_y = tmp_x * (y/x)
    
    L2_X = tmp_x + x
    L2_Y = tmp_y + y

    return (L2_X, L2_Y)

for i in range(len(X_Earth)):
    if X_Earth[i] < 0:
        tmp_x = - np.sqrt(L2_Distance**2 / (1 + (Y_Earth[i]/X_Earth[i]) ** 2))    
    else:
        tmp_x = np.sqrt(L2_Distance**2 / (1 + (Y_Earth[i]/X_Earth[i]) ** 2))
    tmp_y = tmp_x * (Y_Earth[i]/X_Earth[i])
    
    L2_X = tmp_x + X_Earth[i]
    L2_Y = tmp_y + Y_Earth[i]

    L2_X_list.append(L2_X)
    L2_Y_list.append(L2_Y)






# Visualising
plt.scatter(X_JW, Y_JW, color = 'red', label = 'JW', s = 1)
plt.scatter(X_Earth, Y_Earth, color = 'green', label = 'Earth', s = 1)

plt.scatter(L2_X_list, L2_Y_list, color = 'yellow', label = 'L2', s = 1)

plt.title('Space Apps Azerbaijan 2019 - MSU_Space')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()



# Printing values

Velocity_Values = open('DATA.csv', 'w')
Velocity_Values.write('vx_JW,vy_JW,rad\n')
for i in range(len(VX_JW)):
    Velocity_Values.write(f'{X_JW[i]},{Y_JW[i]},{(polar(X_JW[i], Y_JW[i])[1])}\n')
Velocity_Values.close()
