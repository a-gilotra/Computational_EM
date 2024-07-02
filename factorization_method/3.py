import numpy as np
import matplotlib.pyplot as plt
from functions import potential, potential_exact
import warnings
warnings.filterwarnings("ignore")

'''
Note: the fractional error is really small (on the order of 10^-2 to 10^-16), so to get a better impression a logarithmic (base-10) scale has 
been applied.
'''
# a) (below)

# Parameters
L = 1.0
V0 = 1.0
N = 100  # Number of terms 
x = np.linspace(0, L, 100)
y = np.linspace(0, 2 * L, 100)
X, Y = np.meshgrid(x, y)

# Compute potentials
V_series = potential(X, Y, L, V0, N)
V_exact = potential_exact(X, Y, L, V0)

# Compute fractional error
fractional_error = np.abs((V_series - V_exact) / V_exact)

# Avoiding log of zero or negative values
fractional_error = np.where(fractional_error == 0, 1e-16, fractional_error)

# Plotting the fractional error
plt.figure(figsize=(10, 6))
plt.imshow(np.log10(fractional_error), extent=(0, L, 0, 2 * L), origin='lower', aspect='auto', cmap='viridis')
cbar = plt.colorbar(label='Log10 Fractional Error')
cbar.set_label('Log10 Fractional Error')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Logarithmic Fractional Error of Series Approximation to Exact Potential')
plt.show()

'''
b) The biggest fractional errors are at the y = 0 boundary. This is because it takes many, many sine & cosine terms to approximate V0 = 1 accurately.
Even with N = 100 terms, the potential across the y = 0 boundary isn't exactly 1 but some sinuisoidal function with a very small amplitude oscillating
about V = 1. 
'''