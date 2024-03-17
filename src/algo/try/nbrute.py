import timeit

class BezierCurveNPoints:
    def __init__(self, points, num_iterate):
        self.points = points
        self.num_iterate=num_iterate
        self.num_points=0
        self.curve_points = []

    def _count_points(self):
        count=3
        for i in range (1,self.num_iterate):
            count= count*2-1
        
        return count

    def _quadratic_bezier_curve(self, num_points):
        curve_points = []
        
        for t in range(num_points):
            t /= num_points - 1
            data = []
            data.append(self.points)
            for i in range(len(self.points) - 1):
                value = []
                for j in range(len(data[i]) - 1):
                    x = (1-t) * data[i][j][0] + t *data[i][j+1][0]
                    y = (1-t) * data[i][j][1] + t *data[i][j+1][1]
                    value.append((x, y))
                
                data.append(value)
            curve_points.append(data[-1][0])
            
        
        return curve_points

    def calc(self):
        start = timeit.default_timer()
        self.num_points=self._count_points()
        self.curve_points = self._quadratic_bezier_curve(self.num_points)
        end = timeit.default_timer()
        print(f"Time:  {(end - start):.5f}")
        
def main():
    control_points = [(0, 100), (100, 200), (150, 50) , (300, 100), (500, 650), (200, 500), (500, 100)]
    num_iterate = 3
    b = BezierCurveNPoints(control_points, num_iterate)
    
    b.calc()
    print(b.curve_points)
    
main()
 