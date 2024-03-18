from matplotlib.animation import FuncAnimation
import timeit

class BezierCurveN:
    #inisialisasi objek
    def __init__(self, control_points, num_iterate):
        self.control_points = control_points 
        self.num_iterate = num_iterate
        self.bezier_points = [] # titik-titik pada kurva (solusi)
        self.time_execution = 0 # waktu eksekusi algoritma murni
        self.num_points = 0 # banyak titik di kurva pada suatu iterasi
        self.data_bruteforce=[] # data bruteforce untuk membuat animasi
        self.data_dnc = [[] for _ in range(5)] # data dnc untuk membuat animasi

    # fungsi untuk menghitung titik tengah diantara dua buah titik
    def mid_point(self, point1, point2):
        mid_x = (point1[0] + point2[0]) / 2
        mid_y = (point1[1] + point2[1]) / 2
        return mid_x, mid_y

    # fungsi rekursif untuk menghitung titik-titik pada kurva bezier dengan pendekatan dnc
    def calculate_bezier_points_dnc(self, points, current_iteration):
        if current_iteration < self.num_iterate:
            # tahap conquer
            all = [] # menyimpan semua data titik tengah yang didapatkan
            all.append(points)
            
            # pencarian titik tengah yang berada pada garis terakhir yang dibentuk
            for j in range(0, len(points) - 1):
                mid_points = []
                for i in range(0, len(all[j]) - 1):
                    mid_point = self.mid_point(all[j][i], all[j][i+1])
                    mid_points.append(mid_point)
                
                all.append(mid_points)
            
            #tahap divide
            left = [all[i][0] for i in range(len(all))]
            right = [all[len(all) - i - 1][-1] for i in range(len(all))]
            
            # penyimpanan data untuk mempermudah pembuatan animasi
            if current_iteration + 1 < 5:
                self.data_dnc[current_iteration + 1].append(all)
            
            # pemanggilan rekursif dan penggabungan solusi
            self.calculate_bezier_points_dnc(left, current_iteration + 1)
            self.bezier_points.append(all[-1][0])
            self.calculate_bezier_points_dnc(right, current_iteration + 1)
            
    # fungsi yang menjadi entry point untuk pemanggilan fungsi rekursif dnc
    def calc_dnc(self):
        start_time = timeit.default_timer()
        self.bezier_points.append(self.control_points[0])
        self.calculate_bezier_points_dnc(self.control_points, 0)
        self.bezier_points.append(self.control_points[-1])
        end_time = timeit.default_timer()
        self.time_execution = end_time - start_time
    
    # fungsi untuk menghitug berapa banyak titik yang akan dicari pada suatu iterasi
    def count_points(self):
        count=3
        for _ in range (1,self.num_iterate):
            count= count*2-1
        
        if self.num_iterate == 0:
            count = 2
        
        return count
    
    # fungsi untuk menghitung titik-titik pada kurva bezier secara bruteforce
    def calculate_bezier_points_bruteforce(self, num_points):
        curve_points = []
        
        for t in range(num_points):
            t /= num_points - 1
            data = []
            data.append(self.control_points)
            for i in range(len(self.control_points) - 1):
                value = []
                for j in range(len(data[i]) - 1):
                    # menggunakan persamaan dua titik
                    x = (1-t) * data[i][j][0] + t *data[i][j+1][0]
                    y = (1-t) * data[i][j][1] + t *data[i][j+1][1]
                    value.append((x, y))
                
                data.append(value)
            curve_points.append(data[-1][0])
            self.data_bruteforce.append(data)
            
        self.bezier_points = curve_points.copy()

    # fungsi yang menjadi entry points untuk melakukan pembentukan kurva bezier secara bruteforce
    def calc_bruteforce(self):
        start_time = timeit.default_timer()
        self.num_points=self.count_points()
        self.calculate_bezier_points_bruteforce(self.num_points)
        end_time = timeit.default_timer()
        self.time_execution = end_time - start_time
        
    # fungsi untuk menggambar animasi pembentukan kurva secara dnc
    def draw_animate(self, fig, ax):
        ctrl_x, ctrl_y = zip(*self.control_points)
        
        x, y = zip(*[self.control_points[0], self.control_points[-1]])

        line, = ax.plot(x, y, 'bo-', label='Bezier Curve', ms=3)
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
            
            new_line = []
            
            if i > 0 and i < 5:
                for j in range(1,i+1):
                    data2 = self.data_dnc[j]
                    if len(data2) > 1:
                        for k in range(1,len(data2[0]) - 1):
                            data3 = data2[0][k]
                            data4 = data2[1][k]
                            xh, yh = zip(*data3)
                            xhh, yhh = zip(*data4)
                            line_h, = ax.plot(xh, yh, 'go--', ms=3)
                            line_hh, = ax.plot(xhh, yhh, 'go--', ms=3)
                            new_line.extend([line_h, line_hh])
                    else:
                        for k in range(1,len(data2[0]) - 1):
                            data3 = data2[0][k]
                            xh, yh = zip(*data3)
                            line_h, = ax.plot(xh, yh, 'go--', ms=3)
                            new_line.append(line_h)
                            
            return [line] + new_line

        anim = FuncAnimation(fig, animate, frames=self.num_iterate + 1, interval=800, blit=True)

        return anim
    
    # fungsi untuk membuat animasi pembentukan kurva secara bruteforce
    def draw_animate_bruteforce(self, fig, ax):
        ctrl_x, ctrl_y = zip(*self.control_points)
        
        line, = ax.plot([], [], 'bo-', label='Bezier Curve', ms=3)
        
        helper_lines = []
        for i in range(len(self.control_points) - 1):
            line2, = ax.plot([], [], 'go--', ms=2.5)
            helper_lines.append(line2)
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
            last_index = i + 1
            line.set_data(*zip(*self.bezier_points[:last_index]))
            
            data_helper = self.data_bruteforce[i]
            for j in range(len(helper_lines)):
                help_x, help_y = zip(*data_helper[j])
                
                helper_lines[j].set_data(help_x, help_y)
            
            
            return [line] + helper_lines

        anim = FuncAnimation(fig, animate, frames=self.num_points, interval=600/self.num_points, blit=True)

        return anim
    
    # fungsi untuk menggambar kurva tanpa animasi (gambar statik)
    def draw(self, ax):
        ctrl_x, ctrl_y = zip(*self.control_points)
        x, y = zip(*self.bezier_points)
    
        ax.plot(x, y, 'bo-', label='Bezier Curve', ms = 3)
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
