import numpy as np

# PROBLEM 1
def potential(x, y, L, V0, N):
    V = np.zeros_like(x)
    for n in range(1, N, 2):  # Only odd n values: 1, 3, 5, ..., 2N-1
        V += (4 * V0) / (n * np.pi) * np.sin(n * np.pi * x / L) * np.exp(-n * np.pi * y / L)
    return V

# PROBLEM 2
def electric_field_x(x, y, L, V0, N):
    Ex = 0
    for n in range(1, N, 2): 
        Ex -= (4 * V0 / L) * np.cos(n * np.pi * x / L) * np.exp(-n * np.pi * y / L)
    return Ex

def electric_field_y(x, y, L, V0, N):
    Ey = 0
    for n in range(1, N, 2):
        Ey += (4 * V0 / L) * np.sin(n * np.pi * x / L) * np.exp(-n * np.pi * y / L)
    return Ey

# Runge-Kutta 2nd order method for field lines
def rk2(xi, yi, Ex, Ey, h, L, V0, N):

    E_magnitude = np.hypot(Ex, Ey)
    
    xmid = xi + h / 2 * Ex / E_magnitude
    ymid = yi + h / 2 * Ey / E_magnitude

    Exmid = electric_field_x(xmid, ymid, L, V0, N)
    Eymid = electric_field_y(xmid, ymid, L, V0, N)

    E_magnitude_mid = np.hypot(Exmid, Eymid)

    xi_new = xi + h * Exmid / E_magnitude_mid
    yi_new = yi + h * Eymid / E_magnitude_mid

    return xi_new, yi_new

# Field line calculation
def field_line(x_start, y_start, L, V0, N, h=0.01, max_steps=1000):
    x, y = x_start, y_start
    x_points, y_points = [x], [y]
    
    for _ in range(max_steps):

        Ex = electric_field_x(x, y, L, V0, N)
        Ey = electric_field_y(x, y, L, V0, N)

        x, y = rk2(x, y, Ex, Ey, h, L, V0, N)
        
        x_points.append(x)
        y_points.append(y)

        if y >= 2 * L or x <= 0 or x >= L:  # Termination conditions -> stop when field lines reach boundaries
            break
    
    return np.array(x_points), np.array(y_points)

# PROBLEM 3
def potential_exact(x, y, L, V0):
    return (2 * V0 / np.pi) * np.arctan(np.sin(np.pi * x / L) / np.sinh(np.pi * y / L))


