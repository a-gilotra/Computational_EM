import numpy as np
import matplotlib.pyplot as plt
from functions import potential

# Set the parameters
L = 1.0  # Length in x-direction
V0 = 1.0  # Potential at y=0
Ns = [10, 25, 50, 100]  # List of different N values

# Create a grid of x and y values
x = np.linspace(0, L, 100)
y = np.linspace(0, 2 * L, 200)
xgrid, ygrid = np.meshgrid(x, y)

for i, N in enumerate(Ns):
    # Create a new figure for each plot
    fig = plt.figure(figsize=(8, 6))
    
    V = potential(xgrid, ygrid, L, V0, N)
    
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(xgrid, ygrid, V)
    
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('V(x, y)')
    ax.set_title('Potential V(x, y) for N = {}'.format(N))
    ax.set_aspect('equal')

    # Display the plot in a new window
    plt.show()


'''
The boundary at y = 0 gets better matched as N increases. When N is small, the series contains fewer terms and the approximation is coarser. This
approximation cannot capture the details of the boundary condition effectively (i.e. V = 1 at y = 0). As N increases, more terms are added to the 
series (more higher frequency terms are included). Adding in these terms more accurately approximates the boundary condition (i.e. it makes the 
sinusoidal edge more linear/"straight" at y = 0).
'''