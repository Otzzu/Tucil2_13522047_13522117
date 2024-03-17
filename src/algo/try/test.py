import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def divide_and_conquer_bezier(control_points, t):
    if len(control_points) == 1:
        return control_points[0]

    new_points = []
    for i in range(len(control_points) - 1):
        x = (1 - t) * control_points[i][0] + t * control_points[i + 1][0]
        y = (1 - t) * control_points[i][1] + t * control_points[i + 1][1]
        new_points.append((x, y))

    return divide_and_conquer_bezier(new_points, t)

# Persiapan plot
fig, ax = plt.subplots()
control_points = [(-2, -3), (-3, -2) , (0, -2), (1,-3), (2,1)]
x_values, y_values = zip(*control_points)
line, = ax.plot([], [], 'ro-')  # Kurva Bezier
points, = ax.plot([], [], 'bo')  # Titik kontrol
ax.plot(x_values, y_values, 'k--')  # Garis antara titik kontrol
ax.axis('equal')

# Inisialisasi fungsi untuk animasi
def init():
    line.set_data([], [])
    points.set_data(x_values, y_values)
    return line, points

# Fungsi untuk menggambar kurva berdasarkan jumlah iterasi
def draw_bezier(iterations):
    t_values = np.linspace(0, 1, iterations)
    curve_points = [divide_and_conquer_bezier(control_points, t) for t in t_values]
    if (iterations == 9): print(curve_points); print(len(curve_points))
    return zip(*curve_points)

# Fungsi animasi untuk memperbarui kurva
def animate(i):
    x, y = draw_bezier((i + 1))  # i+2 agar ada minimal 2 iterasi (titik awal dan akhir)
    line.set_data(x, y)
    return line, points

# Jumlah frame sesuai dengan jumlah iterasi yang diinginkan
num_iterations = 17  # Contoh: 50 iterasi

# Buat animasi
ani = FuncAnimation(fig, animate, frames=num_iterations, init_func=init, blit=True, interval=200, repeat = False)

plt.show()
