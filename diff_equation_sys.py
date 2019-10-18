"""
    (c) MSU_Space Team
"""

# Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import copy

# Constants
G = 8.644e-10

# Mass of objects
Mass_Of_Sun = 1.98892e27
Mass_Of_Moon = 7.0349e19
Mass_Of_Earth = 5.9742e21
Mass_Of_JW = 6.2

# Earth
x_earth_0 = 152098238.0
y_earth_0 = 0.0
vx_earth_0 = 0.0
vy_earth_0 = 105372.0

# James Webb
x_JW_0 = 152111638.0
y_JW_0 = 0.0
vx_JW_0 = 4200 * 3.6
vy_JW_0 = 40320 + vy_earth_0

# Moon
x_moon_0 = 152503934.0
y_moon_0 = 0.0
vx_moon_0 = 0.0
vy_moon_0 = 3472.56 + vy_earth_0

# Addition constants
t_0 = 0
T = 365 * 24.0
M = 5000
tau = (T - t_0) / M
t = t_0
S = 4
b = [1/6, 1/3, 1/3, 1/6]


# JW, Moon, Earth (x, y, vx, vy)
u_0 = np.array([x_JW_0, y_JW_0, vx_JW_0, vy_JW_0, x_moon_0, y_moon_0, vx_moon_0, vy_moon_0, x_earth_0, y_earth_0, vx_earth_0, vy_earth_0])
u = [np.copy(u_0)]

# James Webb
dot_x_JW = lambda U: U[2]
dot_y_JW = lambda U: U[3]
dot_vx_JW = lambda U: ((-1)*G*(Mass_Of_Sun*U[0]) / ((U[0]**2 + U[1]**2)**(3/2)) - G*(Mass_Of_Earth*(U[0] - U[8])) / (((U[0] - U[8])**2 + (U[1] - U[9])**2)**(3/2)) - G*(Mass_Of_Moon*(U[0] - U[4])) / (((U[0] - U[4])**2 + (U[1] - U[5])**2)**(3/2))) # vx_JW
dot_vy_JW = lambda U: ((-1)*G*(Mass_Of_Sun*U[1]) / ((U[0]**2 + U[1]**2)**(3/2)) - G*(Mass_Of_Earth*(U[1] - U[9])) / (((U[0] - U[8])**2 + (U[1] - U[9])**2)**(3/2)) - G*(Mass_Of_Moon*(U[1] - U[5])) / (((U[0] - U[4])**2 + (U[1] - U[5])**2)**(3/2))) # vy_JW

# Moon
dot_x_moon = lambda U: U[6]
dot_y_moon = lambda U: U[7]
dot_vx_moon = lambda U: ((-1)*G*(Mass_Of_Sun*U[4]) / ((U[4]**2 + U[5]**2)**(3/2)) + G*(Mass_Of_Earth*(U[8] - U[4])) / (((U[4] - U[8])**2 + (U[5] - U[9])**2)**(3/2)) + G*(Mass_Of_JW*(U[0] - U[4])) / (((U[0] - U[4])**2 + (U[1] - U[5])**2)**(3/2))) # vx_moon
dot_vy_moon = lambda U: ((-1)*G*(Mass_Of_Sun*U[5]) / ((U[4]**2 + U[5]**2)**(3/2)) + G*(Mass_Of_Earth*(U[9] - U[5])) / (((U[4] - U[8])**2 + (U[5] - U[9])**2)**(3/2)) + G*(Mass_Of_JW*(U[1] - U[5])) / (((U[0] - U[4])**2 + (U[1] - U[5])**2)**(3/2))) # vy_moon

# Earth
dot_x_earth = lambda U: U[10]
dot_y_earth = lambda U: U[11]
dot_vx_earth = lambda U: ((-1)*G*(Mass_Of_Sun*U[8]) / ((U[8]**2 + U[9]**2)**(3/2)) - G*(Mass_Of_Moon*(U[8] - U[4])) / (((U[4] - U[8])**2 + (U[5] - U[9])**2)**(3/2)) + G*(Mass_Of_JW*(U[0] - U[8])) / (((U[0] - U[8])**2 + (U[1] - U[9])**2)**(3/2))) # vx_earth
dot_vy_earth = lambda U: ((-1)*G*(Mass_Of_Sun*U[9]) / ((U[8]**2 + U[9]**2)**(3/2)) - G*(Mass_Of_Moon*(U[9] - U[5])) / (((U[4] - U[8])**2 + (U[5] - U[9])**2)**(3/2)) + G*(Mass_Of_JW*(U[1] - U[9])) / (((U[0] - U[8])**2 + (U[1] - U[9])**2)**(3/2))) # vy_earth

# Function for system of differential equations
function = lambda U: np.array([dot_x_JW(U), dot_y_JW(U), dot_vx_JW(U), dot_vy_JW(U), dot_x_moon(U), dot_y_moon(U), dot_vx_moon(U), dot_vy_moon(U), dot_x_earth(U), dot_y_earth(U), dot_vx_earth(U), dot_vy_earth(U)])
# function = (dot_x_JW, dot_y_JW, dot_vx_JW, dot_vy_JW, dot_x_moon, dot_y_moon, dot_vx_moon, dot_vy_moon, dot_x_earth, dot_y_earth, dot_vx_earth, dot_vy_earth)



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

        omega.append(function([p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11]]))

    u.append(np.copy(u[m]) + tau * np.copy(summa_2(omega)))






X_JW = []
Y_JW = []
X_Earth = []
Y_Earth = []
X_Moon = []
Y_Moon = []
# 0 1 JW
# 4 5 moon
# 8 9 earth
for i in range(len(u)):
    X_JW.append(u[i][0])
    Y_JW.append(u[i][1])
    X_Earth.append(u[i][8])
    Y_Earth.append(u[i][9])
    X_Moon.append(u[i][4])
    Y_Moon.append(u[i][5])


# Visualising
plt.scatter(X_JW, Y_JW, color = 'red', label = 'JW', s = 1)
plt.scatter(X_Moon, Y_Moon, color = 'blue', label = 'Moon', s = 1)
plt.scatter(X_Earth, Y_Earth, color = 'green', label = 'Earth', s = 1)
plt.title('Space Apps Azerbaijan 2019 - MSU_Space')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()


Values = open('coordinates.csv', 'w')
Values.write('x_jw,y_jw,x_moon,y_moon,x_earth,y_earth\n')
for i in range(len(X_JW)):
    Values.write(f'{X_JW[i]},{Y_JW[i]},{X_Moon[i]},{Y_Moon[i]},{X_Earth[i]},{Y_Earth[i]}\n')
Values.close()
