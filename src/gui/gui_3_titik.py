import tkinter as tk
from tkinter import ttk
from algo.bezier_3_titik import BezierCurve3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox


anim = None
canvas = None
canvas2 = None

# fungsi untuk menggambarkan kurva bezier pada gui dengan memanggil fungsi dari class BezierCurveN
# fungsi ini akan menggambarkan kurva dengan pendekatan dnc
def draw_bezier_curve_dnc(control_points, num_iterate, canvas, canvas2, figure, ax, animate, ax2):
    if animate != None:
        animate.event_source.stop()
    ax.clear()
    ax2.clear()
    bezier_curve = BezierCurve3(control_points, num_iterate)
    bezier_curve.calc_dnc()

    anim = bezier_curve.draw_animate(figure, ax)
    bezier_curve.draw(ax2)
    canvas.draw()
    canvas2.draw()
    return anim, canvas, canvas2, bezier_curve


# fungsi untuk menggambarkan kurva bezier pada gui dengan memanggil fungsi dari class BezierCurveN
# fungsi ini akan menggambarkan kurva dengan pendekatan bruteforce
def draw_bezier_curve_bruteforce(control_points, num_iterate, canvas, canvas2, figure, ax, animate, ax2):
    if animate != None:
        animate.event_source.stop()
    ax.clear()
    ax2.clear()
    bezier_curve = BezierCurve3(control_points, num_iterate)
    bezier_curve.calc_bruteforce()

    anim = bezier_curve.draw_animate_bruteforce(figure, ax)
    bezier_curve.draw(ax2)
    canvas.draw()
    canvas2.draw()
    return anim, canvas, canvas2, bezier_curve

# fungsi utama untuk membuat gui dan menjalankan gui
def main():
    # Window dasar utuk gui
    root = tk.Tk()
    root.title("Bezier Curve Visualizer 3 Control Points")

    # Frame untuk masukan user
    input_frame = ttk.Frame(root, padding="10")
    input_frame.pack(fill="both", expand=True)

    # Variabel untuk menyimpan masukan user
    cp_vars = [tk.StringVar() for _ in range(3)]
    num_iterate_var = tk.IntVar()

    # Input fields untuk control points
    for i in range(3):
        ttk.Label(input_frame, text=f"Control Point {i+1} (x,y):", font=("Arial", 14)).grid(column=0, row=i, sticky="w")
        ttk.Entry(input_frame, textvariable=cp_vars[i], width=20, font=("Arial", 14)).grid(column=1, row=i, sticky="ew")

    # Input fields untuk jumlah iterasi
    ttk.Label(input_frame, text="Number of Iterations", font=("Arial", 14)).grid(column=0, row=3, sticky="w")
    ttk.Entry(input_frame, textvariable=num_iterate_var, width=20, font=("Arial", 14)).grid(column=1, row=3, sticky="ew")

    # Label untuk menampilkan waktu eksekusi
    execution_time_label = ttk.Label(input_frame, text="", font=("Arial", 14))
    execution_time_label.grid(column=1, row=7, sticky="ew")

    # Frame utama untuk meletakan gambar dari kurva beserta animasinya
    main_frame = ttk.Frame(root)
    main_frame.pack(fill="both", expand=True)
    
    # Frame untuk animasi kurva
    plot_frame = ttk.Frame(main_frame)
    plot_frame.grid(row=0, column=1, padx=10, pady=10)
    
    # Frame untuk gambar statik kurva
    plot_frame2 = ttk.Frame(main_frame)
    plot_frame2.grid(row=0, column=0, padx=10, pady=10)
    
    # canvas untuk menggambarkan kurva statik
    figure, ax = plt.subplots(figsize=(7,4))
    global canvas
    canvas = FigureCanvasTkAgg(figure, plot_frame)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    
    # canvas untuk menggambarkan kurva animasi  
    figure2, ax2 = plt.subplots(figsize=(7,4))
    global canvas2
    canvas2 = FigureCanvasTkAgg(figure2, plot_frame2)
    canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    
    # fungsi untuk parsing dan validasi masukan titik kontrol dari user
    def validate_control_points(vars):
        points = []
        try:
            for var in vars:
                x, y = map(float, var.get().split(","))
                points.append((x, y))
            return points, True
        except:
            return None, False
    
    # fungsi untuk validasi masukan iterasi user   
    def validate_num_iterate(var):
        num_iterate = 0
        try:
            num_iterate = var.get()
            
            if num_iterate < 0:
                raise ValueError("value les than zero")
            return num_iterate, True
        except:
            return None, False

    # Fungsi yang akan dipanggil ketika user menekan tombol gambar kurva dnc
    def handle_draw_dnc():
        control_points, is_control_points_valid = validate_control_points(cp_vars)
        if not is_control_points_valid:
            messagebox.showerror("Error", "Invalid input format for control points.")
            return
        num_iterate, is_num_iterate_valid = validate_num_iterate(num_iterate_var)
        if not is_num_iterate_valid:
            messagebox.showerror("Error", "Invalid input format for num iterate.")
            return
        global anim, canvas, canvas2
        anim, canvas, canvas2, bezier_curve = draw_bezier_curve_dnc(control_points, num_iterate, canvas, canvas2, figure, ax, anim, ax2)
        execution_time_label.config(text=f"Time Execution DnC: {bezier_curve.time_execution:.8f} seconds")
    
    # fungsi yang akan dipanggil ketika user menekan tombol gambar kurva bruteforce
    def handle_draw_bruteforce():
        control_points, is_control_points_valid = validate_control_points(cp_vars)
        if not is_control_points_valid:
            messagebox.showerror("Error", "Invalid input format for control points.")
            return
        num_iterate, is_num_iterate_valid = validate_num_iterate(num_iterate_var)
        if not is_num_iterate_valid:
            messagebox.showerror("Error", "Invalid input format for num iterate.")
            return
        global anim, canvas, canvas2
        anim, canvas, canvas2, bezier_curve = draw_bezier_curve_bruteforce(control_points, num_iterate, canvas, canvas2, figure, ax, anim, ax2)
        execution_time_label.config(text=f"Time Execution Bruteforce: {bezier_curve.time_execution:.8f} seconds")
    
    # fungsi yang akan dipanggil ketika menekan tombol clear yang akan membersihkan semua input dan canvas
    def clear_all():
        cp_vars[0].set("")
        cp_vars[1].set("")
        cp_vars[2].set("")
        num_iterate_var.set("")
        
        if anim != None:
            anim.event_source.stop()
        
        ax.clear()
        ax2.clear()
        
        canvas.draw()
        canvas2.draw()
        execution_time_label.config(text="")

    # Konfigurasi font untuk TButton
    style = ttk.Style(root)

    # Konfigurasi font untuk TButton
    style.configure('TButton', font=('Arial', 14, 'bold'))

    # Button untuk menggambar kurva
    draw_button_dnc = ttk.Button(input_frame, text="Draw Curve With DnC", command=handle_draw_dnc, style='TButton')
    draw_button_dnc.grid(column=1, row=4, sticky="ew")
    
    draw_button_bruteforce = ttk.Button(input_frame, text="Draw Curve With Bruteforce", command=handle_draw_bruteforce, style='TButton')
    draw_button_bruteforce.grid(column=1, row=5, sticky="ew")
    
    # button untuk membersihkan 
    clear_button = ttk.Button(input_frame, text="Clear", command=clear_all, style='TButton')
    clear_button.grid(column=1, row=6, sticky="ew", pady=5)
    
    # fungsi untuk mematikan semua background runtime saat gui ditutup
    def on_close():
        global anim
        if anim is not None:
            anim.event_source.stop()
      
        plt.close('all')
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)

    # Menjalankan gui
    root.mainloop()