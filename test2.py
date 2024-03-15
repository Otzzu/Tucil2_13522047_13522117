import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Divide and conquer implementation to calculate Bezier curve points
def bezier_curve(control_points, t, ax=None):
    if len(control_points) == 1:
        return [control_points[0][0]], [control_points[0][1]]  # Return x and y separately

    new_points = []
    for i in range(len(control_points) - 1):
        x = (1 - t) * control_points[i][0] + t * control_points[i + 1][0]
        y = (1 - t) * control_points[i][1] + t * control_points[i + 1][1]
        new_points.append((x, y))
    
    if ax is not None:  # If an axis is provided, draw the intermediate lines
        x_vals, y_vals = zip(*new_points)
        ax.plot(x_vals, y_vals, 'go-', alpha=0.3)  # Draw intermediate lines
    
    # Recursively call bezier_curve and concatenate the x and y coordinates
    x_points, y_points = zip(*new_points)
    next_x, next_y = bezier_curve(new_points, t, ax)
    return [control_points[0][0]] + list(next_x), [control_points[0][1]] + list(next_y)


# Initialize the plot
fig, ax = plt.subplots()
control_points = [(-2, -3), (-3, -2) , (0, -2), (1,-3), (2,1)]
curve, = ax.plot([], [], 'r-')  # The Bezier curve
points, = ax.plot([], [], 'bo')  # The control points
ax.set_xlim(0, 400)
ax.set_ylim(0, 300)

# Initialize the animation
def init():
    points.set_data([], [])
    curve.set_data([], [])
    return points, curve

# The animation function, called for each frame
def animate(t):
    ax.clear()  # Clear previous intermediate lines
    ax.plot(*zip(*control_points), 'bo-')  # Plot control points and lines
    
    # Calculate the points on the curve
    x_points, y_points = bezier_curve(control_points, t, ax)
    print(x_points, y_points)
    curve.set_data(x_points, y_points)
    return points, curve


# Create the animation
ani = FuncAnimation(fig, animate, frames=np.linspace(0, 1, 17), init_func=init, blit=False, repeat=False)

plt.show()
