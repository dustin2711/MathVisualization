"""
Renders the scalar field ln(x + y) and its derivative.
"""

from numpy import linspace, meshgrid, log, sqrt
import matplotlib.pyplot as plt

number_of_steps = 20
starting_xy = -2
ending_xy = 2

# Rendering
alpha = 0.75


# Define the function
def f(x, y):
    return log(x + y)


# Define the derivative
def fʹ(x, y):
    return 1 / (x + y)


# Create a grid of x and y values
x = linspace(starting_xy, ending_xy, number_of_steps)
y = linspace(starting_xy, ending_xy, number_of_steps)
X, Y = meshgrid(x, y)
Z = f(X, Y)
Zʹ = fʹ(X, Y)

# Create the plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")
surf1 = ax.plot_surface(X, Y, Z, cmap="copper", alpha=alpha, zorder=2)
# surf2 = ax.plot_surface(X, Y, Zʹ, cmap="Wistia", alpha=alpha, zorder=1)

# Add a color bar which maps values to colors
# fig.colorbar(surf1, ax=ax, shrink=0.5, aspect=10)
# fig.colorbar(surf2, ax=ax, shrink=0.5, aspect=10)

# Set plot titles and labels
ax.set_title("f(x, y) = ln(x + y)        f'(x, y) = 1 / (x + y)")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_zlabel("$z$")
ax.set_zlim(-3, 3)

ax.quiver(1, 0, 0, 2.0 / sqrt(5), 1.0 / sqrt(5), 0)

plt.show()
