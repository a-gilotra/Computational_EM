import numpy as np
import matplotlib.pyplot as plt
from functions import field_line

# Set the parameters
L = 1.0  # Length in x-direction
V0 = 1.0  # Potential at y=0

# Launch 50 field lines from y = 0 boundary
fig, ax = plt.subplots(figsize=(8, 6))
launch_points = np.linspace(0, L, 50)

for xi in launch_points:
    x_points, y_points = field_line(xi, 0, L, V0, N=100)
    ax.plot(x_points, y_points, "k-")

ax.set_xlim(0, L)
ax.set_ylim(0, 2 * L)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Electric Field Lines')
plt.show()

'''
1) The field lines point from the y = 0 boundary to the left and right edges of the potential box. This makes sense, as electric field lines point
from places of high potential (the y = 0 boundary) to places of low potential (the sides of the box). The sides of the box are at a lower potential 
than the y = 0 boundary because of the exponential decay term.
2) The field lines are denser near the y = 0 boundary and become sparser as they move toward the sides of the box. This is expected because the 
potential decreases exponentially with increasing y, leading to a stronger electric field near the y = 0 boundary and a weaker field further away. 
'''