import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

R = 2.0
a = 0.5

u = np.linspace(0, 2*np.pi, 300)
v = np.linspace(-1, 1, 50)
u, v = np.meshgrid(u, v)

x = (R + a * v * np.cos(u/2)) * np.cos(u)
y = (R + a * v * np.cos(u/2)) * np.sin(u)
z =  a * v * np.sin(u/2)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x, y, z, rstride=1, cstride=1,
                cmap='plasma', edgecolor='none')

ax.set_title("Toruso‑Möbius — model kosmosu (FIELDCORE)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()
