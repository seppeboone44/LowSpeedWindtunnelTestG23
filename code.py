import math
import numpy as np
import matplotlib.pyplot as plt

#airfoil data
airfoil = np.stack(
    list(filter(
        lambda x : len(x) > 1, 
        [
            list(filter(len, x.split(" "))) for x in open("C:/Users/seppe/OneDrive - Delft University of Technology/Documents/0 - University/Bcs AE/Bsc AE2/AE2130-II Low Speed Windtunnel Test/GitHub/Code/airfoil.dat", "r").read().split("\n")
        ]
    ))
).astype(float)

#sensor values
data = np.stack([
    x.split(", ") for x in open("C:/Users/seppe/OneDrive - Delft University of Technology/Documents/0 - University/Bcs AE/Bsc AE2/AE2130-II Low Speed Windtunnel Test/GitHub/Code/data.txt", "r").read().split(",\n")
]).astype(float)

#sensor location
sensors = np.stack([
    x.split("\t") for x in open("C:/Users/seppe/OneDrive - Delft University of Technology/Documents/0 - University/Bcs AE/Bsc AE2/AE2130-II Low Speed Windtunnel Test/GitHub/Code/sensors.txt", "r").read().split("\n")
]).astype(float)


areas = airfoil[1:] - airfoil[:-1]
normals = [[x[1] / (x[0]**2 + x[1]**2) ** 0.5, -x[0]/ (x[0]**2 + x[1]**2) ** 0.5] for x in areas]

#function for finding which sensor correpsonds to the correct datapoint
def interpolate(point, sensors):
    for x in range(1, len(sensors)):
        if (sensors[x, 1] < 0 and point[1] > 0) or (sensors[x, 1] > 0 and point[1] < 0):
            continue
        if sensors[x - 1, 0]* 0.01 <= point[0] and sensors[x, 0] * 0.01 >= point[0]:
            return x
    return -1
#aoa values
lt = [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12.5, 
 13, 13.5, 14, 14.5, 14.2, 13.8, 13.6, 13.4, 13.2, 13, 12.8, 12.6, 12.4, 
 12.2, 12, 11.5, 11, 10.5, 10, 9.5, 9, 8.5, 7.5, 6.5] #aoa
ltrad = []
for i in lt:
    i = math.pi * i / 180
    ltrad.append(i)
DRAG = []
LIFT = []

#drag curve generation
for y in range(0, len(lt)):
    force = np.stack([0.0,  0.0])
    for x in range(len(airfoil) - 1):
        index = interpolate(airfoil[x], sensors)
        if index == -1: continue
        force -= np.array(normals[x]) * data[y, index] * (areas[x, 0] ** 2 + areas[x, 1] ** 2) ** 0.5
    LIFT.append(force[1] / 247) #247 is q here
    DRAG.append(abs(force[0]) / 247)

pressuresalpha1 = data[17]
cpalpha1top =[]
for i in range(25):
    new = (pressuresalpha1[i])/(pressuresalpha1[96]-pressuresalpha1[109])
    cpalpha1top.append(new)

cpalpha1bottom =[]
for i in range(24):
    new = (pressuresalpha1[i+25])/(pressuresalpha1[96]-pressuresalpha1[109])
    cpalpha1bottom.append(new)

sensorxtop = []
for i in range(25):
    xloc = sensors[i,0]
    sensorxtop.append(xloc)

sensorxbottom = []
for i in range(24):
    xloc = sensors[i+25,0]
    sensorxbottom.append(xloc)

# Angles to chose: negative(-3), normal (4deg), clmax(approx)(11deg)

plt.xlabel(r'Chord $(x/c)$')
plt.ylabel(r'$C_p$')
plt.gca().invert_yaxis()  # Inverts the y-axis
plt.plot(sensorxtop, cpalpha1top, marker = '^', color = 'blue', label = r'$C_p$ Top Surface')
plt.plot(sensorxbottom, cpalpha1bottom, marker = '^', color = 'orange', label = r'$C_p$ Bottom Surface')
plt.legend()
plt.show()




# plt.title(r'$C_l$ $\alpha$ for the 2D test')
# plt.xlabel(r'Angle of Attack ($\alpha$) [rad]')
# plt.ylabel(r'Lift coefficient ($C_l$) [-]')
# plt.grid()
# # Add a symbol for each data point
# plt.axhline(linewidth = 1, color = "black")
# plt.axvline(linewidth = 1, color = "black")
# plt.plot(ltrad, LIFT, marker = 'D')
# plt.show()