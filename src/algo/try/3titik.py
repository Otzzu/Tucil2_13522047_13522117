import timeit

class BenzierCurve:
    def __init__(self, contol_points, num_iterate):
        self.control_points = contol_points
        self.num_iterate = num_iterate
        self.benzier_points = []
    
    def midPoint(self,point1, point2):
        mid_x = (point1[0] + point2[0]) / 2
        mid_y = (point1[1] + point2[1]) / 2

        return mid_x, mid_y

    def calculate_bezier_points(self,point1, point2, point3, currIterations):
        if (currIterations < self.num_iterate):
            midPoint1 = self.midPoint(point1, point2)
            midPoint2 = self.midPoint(point2, point3)
            midPoint3 = self.midPoint(midPoint1, midPoint2)

            currIterations = currIterations + 1

            self.calculate_bezier_points(point1, midPoint1, midPoint3, currIterations)
            self.benzier_points.append(midPoint3)
            self.calculate_bezier_points(midPoint3, midPoint2, point3, currIterations)
    
    def calc(self):
        start = timeit.default_timer()
        self.benzier_points.append(self.control_points[0])
        self.calculate_bezier_points(self.control_points[0], self.control_points[1], self.control_points[2], 0)
        self.benzier_points.append(self.control_points[2])
        end = timeit.default_timer()
        print(f"Time:  {(end - start):.5f}")

        

def main():
    control_points = [(0, 100), (100, 200) , (300, 100)]
    num_iterate = 20
    b = BenzierCurve(control_points, num_iterate)
    b.calc()
    
    # print(b.benzier_points)
    
main()
    