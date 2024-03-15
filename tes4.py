class BezierCurveCalculator:
    def __init__(self, control_points, num_iterate):
        self.control_points = control_points
        self.num_iterate = num_iterate
        self.bezier_points = []

    def calculate_bezier_points(self, t):
        points = self.control_points
        while len(points) > 1:
            points = [self.mid_point(points[i], points[i+1], t) for i in range(len(points)-1)]
        return points[0]

    def mid_point(self, point1, point2, t):
        return ((1 - t) * point1[0] + t * point2[0], (1 - t) * point1[1] + t * point2[1])

    def calc(self):
        # Hanya perlu menambahkan titik awal sekali
        self.bezier_points.append(self.control_points[0])
        # Hitung titik Bezier untuk setiap iterasi t
        for i in range(1, self.num_iterate):
            t = i / float(self.num_iterate - 1)
            self.bezier_points.append(self.calculate_bezier_points(t))
        # Menambahkan titik akhir setelah iterasi selesai
        self.bezier_points.append(self.control_points[-1])

# Contoh pemakaian
control_points = [(0, 100), (100, 200) , (300, 100)]
num_iterate = 9  # Atau berapapun jumlah iterasi yang diinginkan
calculator = BezierCurveCalculator(control_points, num_iterate)
calculator.calc()

# Cetak titik-titik hasil perhitungan
for point in calculator.bezier_points:
    print(point)
