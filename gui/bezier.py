from matplotlib.animation import FuncAnimation

class BezierCurve:
    def __init__(self, control_points, num_iterate):
        self.control_points = control_points
        self.num_iterate = num_iterate
        self.bezier_points = []

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
             
    #0,0;1,8;5,0;8,10;14,0;20,15;25,20;35,30;20,4;10,0
    def calc(self):
        self.bezier_points.append(self.control_points[0])
        self.calculate_bezier_points(self.control_points, 0)
        self.bezier_points.append(self.control_points[-1])
    
    def draw_animate(self, fig, ax):
        ctrl_x, ctrl_y = zip(*self.control_points)
        
        x, y = zip(*[self.control_points[0], self.control_points[-1]])

        line, = ax.plot(x, y, 'bo-', label='Bezier Curve', ms=3.5)
        ax.plot(ctrl_x, ctrl_y, 'ro-', label='Control Points')
        
        ax.set_xlim(min(ctrl_x) - min(ctrl_x) // 10, max(ctrl_x) + max(ctrl_x) // 10)
        ax.set_ylim(min(ctrl_y) - min(ctrl_y) // 10, max(ctrl_y) + max(ctrl_y) // 10)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Bezier Curve Animation')
        ax.legend()
        ax.grid(True)
        
        def animate(i):
            # print(i)
            length = len(self.bezier_points)
            gap = length - 1
            for j in range(i):
                gap = gap // 2
            
            data = []
            
            if (gap != 1):
                for j in range((length // gap) + 1):
                    # print(j*gap)
                    data.append(self.bezier_points[j * gap])
            else:
                data = self.bezier_points.copy()
            
            new_x, new_y = zip(*data)
            
            line.set_data(new_x, new_y)
            
            return [line]

        anim = FuncAnimation(fig, animate, frames=self.num_iterate + 1, interval=800, blit=True)

        return anim
        # 0,100;100,200;150,50;300,100
        # 0,100;100,200;300,100
        
    def draw(self, ax):
        ctrl_x, ctrl_y = zip(*self.control_points)
        x, y = zip(*self.bezier_points)
    
        ax.plot(x, y, 'bo-', label='Bezier Curve', ms = 3.5)
        ax.plot(ctrl_x, ctrl_y, 'ro-', label='Control Points')        

        # for i in range(len(self.bezier_points)):
        #     ax.plot([self.bezier_points[i][0]], [self.bezier_points[i][1]], 'go', ms=3.5)
    
    
        ax.set_xlim(min(ctrl_x) - min(ctrl_x) // 10, max(ctrl_x) + max(ctrl_x) // 10)
        ax.set_ylim(min(ctrl_y) - min(ctrl_y) // 10, max(ctrl_y) + max(ctrl_y) // 10)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Bezier Curve')
        ax.legend()
        ax.grid(True)
        
        

# def main():
#     # This can now be any number of control points
#     control_points = [(0, 100), (100, 200), (150, 50) , (300, 100)]
#     # control_points = [(0, 100), (100, 200), (150, 50) , (300, 100), (500, 650), (200, 500), (500, 100)]
#     num_iterate = 10
#     bezier_curve = BezierCurve(control_points, num_iterate)
#     bezier_curve.calc()
    
#     # print("res")
#     # print(bezier_curve.bezier_points)
    
#     bezier_curve.draw()

# main()
