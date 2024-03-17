from matplotlib.animation import FuncAnimation
import timeit

class BezierCurve3:
    def __init__(self, control_points, num_iterate):
        self.control_points = control_points
        self.num_iterate = num_iterate
        self.bezier_points = []
        self.time_execution = 0
        self.num_points=0
        

    def midPoint(self,point1, point2):
        mid_x = (point1[0] + point2[0]) / 2
        mid_y = (point1[1] + point2[1]) / 2

        return mid_x, mid_y

    def calculate_bezier_points_dnc(self,point1, point2, point3, currIterations):
        if (currIterations < self.num_iterate):
            midPoint1 = self.midPoint(point1, point2)
            midPoint2 = self.midPoint(point2, point3)
            midPoint3 = self.midPoint(midPoint1, midPoint2)

            currIterations = currIterations + 1

            self.calculate_bezier_points_dnc(point1, midPoint1, midPoint3, currIterations)
            self.bezier_points.append(midPoint3)
            self.calculate_bezier_points_dnc(midPoint3, midPoint2, point3, currIterations)
    
    def calc_dnc(self):
        start_time = timeit.default_timer()
        self.bezier_points.append(self.control_points[0])
        self.calculate_bezier_points_dnc(self.control_points[0], self.control_points[1], self.control_points[2], 0)
        self.bezier_points.append(self.control_points[2])
        end_time = timeit.default_timer()
        self.time_execution = end_time - start_time
        
    def count_points(self):
        count=3
        for _ in range (1,self.num_iterate):
            count= count*2-1
        
        return count

    def calculate_bezier_points_bruteforce(self, num_points):
        curve_points = []
        
        for t in range(num_points):
            t /= num_points - 1
            x = (1 - t)**2 * self.control_points[0][0] + 2 * (1 - t) * t * self.control_points[1][0] + t**2 * self.control_points[2][0]
            y = (1 - t)**2 * self.control_points[0][1] + 2 * (1 - t) * t * self.control_points[1][1] + t**2 * self.control_points[2][1]
            curve_points.append((x, y))
            
        self.bezier_points = curve_points.copy()

    def calc_bruteforce(self):
        start_time = timeit.default_timer()
        self.num_points=self.count_points()
        self.calculate_bezier_points_bruteforce(self.num_points)
        end_time = timeit.default_timer()
        self.time_execution = end_time-start_time
    
    def draw_animate(self, fig, ax):
        ctrl_x, ctrl_y = zip(*self.control_points)
        
        x, y = zip(*[self.control_points[0], self.control_points[-1]])

        line, = ax.plot(x, y, 'bo-', label='Bezier Curve', ms=3.5)
        ax.plot(ctrl_x, ctrl_y, 'ro-', label='Control Points')
        
        delta_x = abs(max(ctrl_x) // 10) if max(ctrl_x) != 0 else min(ctrl_x) // 10
        delta_y = abs(max(ctrl_y) // 10) if max(ctrl_y) != 0 else min(ctrl_y) // 10
        
        ax.set_xlim(min(ctrl_x) - (delta_x if delta_x != 0 else 5), max(ctrl_x) + (delta_x if delta_x != 0 else 5))
        ax.set_ylim(min(ctrl_y) - (delta_y if delta_y != 0 else 5), max(ctrl_y) + (delta_y if delta_y != 0 else 5))
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Bezier Curve Animation')
        ax.legend()
        ax.grid(True)
        
        def animate(i):
            length = len(self.bezier_points)
            gap = length - 1
            for j in range(i):
                gap = gap // 2
            
            data = []
            
            if (gap != 1):
                for j in range((length // gap) + 1):
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
    
    
        delta_x = abs(max(ctrl_x) // 10) if max(ctrl_x) != 0 else min(ctrl_x) // 10
        delta_y = abs(max(ctrl_y) // 10) if max(ctrl_y) != 0 else min(ctrl_y) // 10
        
        ax.set_xlim(min(ctrl_x) - (delta_x if delta_x != 0 else 5), max(ctrl_x) + (delta_x if delta_x != 0 else 5))
        ax.set_ylim(min(ctrl_y) - (delta_y if delta_y != 0 else 5), max(ctrl_y) + (delta_y if delta_y != 0 else 5))
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Bezier Curve')
        ax.legend()
        ax.grid(True)