import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def bezier_curve(control_points, iterations):
    if len(control_points) == 1:
        return control_points[0]

    # Divide
    left_points = control_points[:len(control_points)//2]
    right_points = control_points[len(control_points)//2:]

    # Conquer
    left_curve = bezier_curve(left_points, iterations)
    right_curve = bezier_curve(right_points, iterations)

    # Combine
    x = (1 - iterations) * left_curve[0] + iterations * right_curve[0]
    y = (1 - iterations) * left_curve[1] + iterations * right_curve[1]

    return (x, y)

def calc_bezier(control_points, num_points):
    points = []
    for i in range(num_points + 1):
        t = i / num_points
        point = bezier_curve(control_points, t)
        points.append(point)
    return points

# Set up the figure, the axis, and the plot elements
fig, ax = plt.subplots()
control_points = [(-2, -3), (-3, -2) , (0, -2), (1,-3), (2,1)]
x_control, y_control = zip(*control_points)

curve, = ax.plot([], [], 'r-')
points, = ax.plot(x_control, y_control, 'bo-')
helper_lines = [ax.plot([], [], 'g--')[0] for _ in range(len(control_points)-1)]

def init():
    curve.set_data([], [])
    for line in helper_lines:
        line.set_data([], [])
    return [curve] + helper_lines

# The main animation function
def animate(i):
    bezier, inter_points = calc_bezier(control_points, i)
    x_bezier, y_bezier = zip(*bezier)
    curve.set_data(x_bezier, y_bezier)
    
    for j, line in enumerate(helper_lines):
        x_inter, y_inter = zip(*[pt[j] for pt in inter_points])
        line.set_data(x_inter, y_inter)

    return [curve] + helper_lines

# Create the animation
ani = FuncAnimation(fig, animate, frames=np.linspace(1, 100, 17), init_func=init, blit=True)


# Set the axis limits
ax.set_xlim(min(x_control) - 10, max(x_control) + 10)
ax.set_ylim(min(y_control) - 10, max(y_control) + 10)

# Show the animation
plt.show()
