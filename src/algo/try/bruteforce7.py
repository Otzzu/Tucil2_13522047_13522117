import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class BezierCurve7Points:
    def __init__(self, P0, P1, P2, P3, P4, P5, P6, num_iterate):
        self.P0 = P0
        self.P1 = P1
        self.P2 = P2
        self.P3 = P3
        self.P4 = P4
        self.P5 = P5
        self.P6 = P6
        self.num_iterate = num_iterate
        self.num_points = self._count_points()
        self.curve_points = self._bezier_curve(self.num_points)

    def _count_points(self):
        count=3
        for i in range (1,self.num_iterate):
            count= count*2-1
        
        return count

    def _bezier_curve(self, num_points):
        curve_points = []
        for t in range(num_points):
            t /= num_points - 1
            x = (1 - t)**6 * self.P0[0] + 6 * t * (1 - t)**5 * self.P1[0] + 15 * t**2 * (1 - t)**4 * self.P2[0] + 20 * t**3 * (1 - t)**3 * self.P3[0] + 15 * t**4 * (1 - t)**2 * self.P4[0] + 6 * t**5 * (1 - t) * self.P5[0] + t**6 * self.P6[0]
            y = (1 - t)**6 * self.P0[1] + 6 * t * (1 - t)**5 * self.P1[1] + 15 * t**2 * (1 - t)**4 * self.P2[1] + 20 * t**3 * (1 - t)**3 * self.P3[1] + 15 * t**4 * (1 - t)**2 * self.P4[1] + 6 * t**5 * (1 - t) * self.P5[1] + t**6 * self.P6[1]
            curve_points.append((x, y))
        return curve_points

    def draw_animation_curve(self, fig, ax):
        line_P0_P1, = ax.plot([], [], color='red')
        line_P1_P2, = ax.plot([], [], color='red')
        line_P2_P3, = ax.plot([], [], color='red')
        line_P3_P4, = ax.plot([], [], color='red')
        line_P4_P5, = ax.plot([], [], color='red')
        line_P5_P6, = ax.plot([], [], color='red')
        ax.scatter([self.P0[0], self.P1[0], self.P2[0], self.P3[0], self.P4[0], self.P5[0], self.P6[0]], [self.P0[1], self.P1[1], self.P2[1], self.P3[1], self.P4[1], self.P5[1], self.P6[1]], color='red')
        ax.plot([self.P0[0], self.P1[0], self.P2[0], self.P3[0], self.P4[0], self.P5[0], self.P6[0]], [self.P0[1], self.P1[1], self.P2[1], self.P3[1], self.P4[1], self.P5[1], self.P6[1]], '-ro', label='Control Points')
        line_curve, = ax.plot([], [], 'bo-', label='Curve Points', ms=3.5)
        
        ax.set_title('Brute Force Bezier Curve Animation')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.legend()
        ax.grid(True)

        def animate_curve(i):
            if i < len(self.curve_points):
                data = self.curve_points[:i]
            else:
                data = self.curve_points
            if not data:
                new_x, new_y = [], []
            else:
                new_x, new_y = zip(*data)
            line_curve.set_data(new_x, new_y)
            line_P0_P1.set_data([self.P0[0], self.P1[0]], [self.P0[1], self.P1[1]])
            line_P1_P2.set_data([self.P1[0], self.P2[0]], [self.P1[1], self.P2[1]])
            line_P2_P3.set_data([self.P2[0], self.P3[0]], [self.P2[1], self.P3[1]])
            line_P3_P4.set_data([self.P3[0], self.P4[0]], [self.P3[1], self.P4[1]])
            line_P4_P5.set_data([self.P4[0], self.P5[0]], [self.P4[1], self.P5[1]])
            line_P5_P6.set_data([self.P5[0], self.P6[0]], [self.P5[1], self.P6[1]])
            return line_curve, line_P0_P1, line_P1_P2, line_P2_P3, line_P3_P4, line_P4_P5, line_P5_P6

        anim = FuncAnimation(fig, animate_curve, frames=len(self.curve_points) + self.num_points, interval=1000 / self.num_points, blit=True)

        return anim
    
    def draw_curve(self, ax):
        ctrl_x = [self.P0[0], self.P1[0], self.P2[0], self.P3[0], self.P4[0], self.P5[0], self.P6[0]]
        ctrl_y = [self.P0[1], self.P1[1], self.P2[1], self.P3[1], self.P4[1], self.P5[1], self.P6[1]]

        ax.plot(ctrl_x, ctrl_y, 'ro-', label='Control Points')
        ax.plot(*zip(*self.curve_points), 'bo-', label='Curve Points', ms=3.5)

        ax.set_xlim(min(ctrl_x) - min(ctrl_x) // 10, max(ctrl_x) + max(ctrl_x) // 10)
        ax.set_ylim(min(ctrl_y) - min(ctrl_y) // 10, max(ctrl_y) + max(ctrl_y) // 10)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Brute Force Bezier Curve')
        ax.legend()
        ax.grid(True)