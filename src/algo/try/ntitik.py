import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import timeit

class BezierCurve:
    def __init__(self, control_points, num_iterate):
        self.control_points = control_points
        self.num_iterate = num_iterate
        self.bezier_points = []
        # self.all_helper_lines = []

    def mid_point(self, point1, point2):
        mid_x = (point1[0] + point2[0]) / 2
        mid_y = (point1[1] + point2[1]) / 2
        return mid_x, mid_y

    def calculate_bezier_points(self, points, current_iteration):
        if current_iteration < self.num_iterate:
            all = []
            
            all.append(points)
            for j in range(0, len(points) - 1):
                mid_points = []
                for i in range(0, len(all[j]) - 1):
                    mid_point = self.mid_point(all[j][i], all[j][i+1])
                    mid_points.append(mid_point)
                
                all.append(mid_points)
            
            left = [all[i][0] for i in range(len(all))]
            right = [all[len(all) - i - 1][-1] for i in range(len(all))]
            
            
            self.calculate_bezier_points(left, current_iteration + 1)
            self.bezier_points.append(all[-1][0])
            self.calculate_bezier_points(right, current_iteration + 1)
    
    def calc(self):
        start = timeit.default_timer()
        
        self.bezier_points.append(self.control_points[0])
        self.calculate_bezier_points(self.control_points, 0)
        self.bezier_points.append(self.control_points[-1])
        end = timeit.default_timer()
        print(f"Time:  {(end - start):.5f}")
    
    def draw(self):
        ctrl_x, ctrl_y = zip(*self.control_points)
        fig, ax = plt.subplots(figsize=(8, 6))

        # Initialize main curve line and control points line
        line, = ax.plot([], [], 'b-', label='Bezier Curve')
        ax.plot(ctrl_x, ctrl_y, 'ro-', label='Control Points')
        
        moving_point, = ax.plot([], [], 'go', ms=4)
        
        many_mov = 2
        for i in range(3, len(self.control_points) + 1):
            many_mov = many_mov + i
        
        # print(many_mov)
        
        mov_points = [ax.plot([], [], 'go', ms=4) for _ in range(many_mov)]

        # Axis settings
        ax.set_xlim(min(ctrl_x) - 10, max(ctrl_x) + 10)
        ax.set_ylim(min(ctrl_y) - 10, max(ctrl_y) + 10)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Bezier Curve Animation')
        ax.legend()
        ax.grid(True)
        
        total_duration = 4000 # Total animation duration in milliseconds
        interval = total_duration / len(self.bezier_points)
        
        def animate(i):
            # Update main curve line
            line.set_data(*zip(*self.bezier_points[:i+1]))
            moving_point.set_data([self.bezier_points[i][0]], [self.bezier_points[i][1]])
            
            return [line, moving_point]

        # Create the animation
        anim = FuncAnimation(fig, animate, frames=len(self.bezier_points), interval=interval, blit=True)

        # return anim
        # plt.show()
        # canvas.draw()
        # 0,100;100,200;150,50;300,100

def main():
    # This can now be any number of control points
    # control_points = [(0, 100), (100, 200) , (300, 100)]
    control_points = [(0, 100), (100, 200) , (300, 100)]
    num_iterate = 20
    bezier_curve = BezierCurve(control_points, num_iterate)
    bezier_curve.calc()
    
    # print(bezier_curve.bezier_points)
    
    # bezier_curve.draw()

main()
