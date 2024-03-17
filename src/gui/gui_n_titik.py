import tkinter as tk
from tkinter import ttk
from algo.bezier_n_titik import BezierCurveN
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox

anim = None
canvas = None
canvas2 = None

def draw_bezier_curve_dnc(control_points, num_iterate, canvas, canvas2, figure, ax, animate, ax2):
    if animate != None:
        animate.event_source.stop()
    ax.clear()
    ax2.clear()
    bezier_curve = BezierCurveN(control_points, num_iterate)
    bezier_curve.calc_dnc()

    anim = bezier_curve.draw_animate(figure, ax)
    bezier_curve.draw(ax2)
    canvas.draw()
    canvas2.draw()
    return anim, canvas, canvas2, bezier_curve

def draw_bezier_curve_bruteforce(control_points, num_iterate, canvas, canvas2, figure, ax, animate, ax2):
    if animate != None:
        animate.event_source.stop()
    ax.clear()
    ax2.clear()
    
    bezier_curve = BezierCurveN(control_points, num_iterate)
    bezier_curve.calc_bruteforce()

    anim = bezier_curve.draw_animate_bruteforce(figure, ax)
    bezier_curve.draw(ax2)
    canvas.draw()
    canvas2.draw()
    return anim, canvas, canvas2, bezier_curve

def main():
    
    root = tk.Tk()
    root.title("Bezier Curve Visualizer N Control Points")

    # Frame for the input form
    input_frame = ttk.Frame(root, padding="10")
    input_frame.pack(fill="both", expand=True)

    # Variables to store control points and iterations
    control_points_var = tk.StringVar()
    num_iterate_var = tk.IntVar()

    # Input fields
    ttk.Label(input_frame, text="Control Points (x1,y1;x2,y2;...): ", font=("Arial", 14)).grid(column=0, row=0, sticky="w")
    control_points_entry = ttk.Entry(input_frame, textvariable=control_points_var, width=40, font=("Arial", 14))
    control_points_entry.grid(column=1, row=0, sticky="ew")

    ttk.Label(input_frame, text="Number of Iterations: ", font=("Arial", 14)).grid(column=0, row=1, sticky="w")
    num_iterate_entry = ttk.Entry(input_frame, textvariable=num_iterate_var, width=40, font=("Arial", 14))
    num_iterate_entry.grid(column=1, row=1, sticky="ew")
    
    execution_time_label = ttk.Label(input_frame, text="", font=("Arial", 14))
    execution_time_label.grid(column=1, row=5, sticky="ew")

    # Frame for the plot
    main_frame = ttk.Frame(root)
    main_frame.pack(fill="both", expand=True)
    
    
    plot_frame = ttk.Frame(main_frame)
    plot_frame.grid(row=0, column=1, padx=10, pady=10)
    
    plot_frame2 = ttk.Frame(main_frame)
    plot_frame2.grid(row=0, column=0, padx=10, pady=10)
    
    
    figure, ax = plt.subplots(figsize=(7,4))
    global canvas
    canvas = FigureCanvasTkAgg(figure, plot_frame)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    
    figure2, ax2 = plt.subplots(figsize=(7,4))
    global canvas2
    canvas2 = FigureCanvasTkAgg(figure2, plot_frame2)
    canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    

    # Function to parse control points input
    def parse_and_validate_control_points(var):
        input_str = var.get()
        points = []
        try:
            for point_str in input_str.split(";"):
                x, y = map(float, point_str.split(","))
                points.append((x, y))
                
            if len(points) <= 0:
                raise ValueError("Many points must be > 0")
            return points, True
        except:
            return None, False
        
    def validate_num_iterate(var):
        num_iterate = 0
        try:
            num_iterate = var.get()
            
            if num_iterate < 0:
                raise ValueError("value les than zero")
            return num_iterate, True
        except:
            return None, False
        

    # Function to handle drawing the curve
    def handle_draw_dnc():
        control_points, is_control_points_valid = parse_and_validate_control_points(control_points_var)
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
    
    def handle_draw_bruteforce():
        control_points, is_control_points_valid = parse_and_validate_control_points(control_points_var)
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

    def clear_all():
        control_points_var.set("")
        num_iterate_var.set("")
        
        if anim != None:
            anim.event_source.stop()
        
        ax.clear()
        ax2.clear()
        
        canvas.draw()
        canvas2.draw()
        execution_time_label.config(text="")
    
    style = ttk.Style(root)

    # Konfigurasi font untuk TButton
    style.configure('TButton', font=('Arial', 14, 'bold'))

    # Button to draw the curve
    draw_button_dnc = ttk.Button(input_frame, text="Draw Curve With DnC", command=handle_draw_dnc, style='TButton')
    draw_button_dnc.grid(column=1, row=2, sticky="ew")
    
    draw_button_bruteforce = ttk.Button(input_frame, text="Draw Curve With Bruteforce", command=handle_draw_bruteforce, style='TButton')
    draw_button_bruteforce.grid(column=1, row=3, sticky="ew")
    
    clear_button = ttk.Button(input_frame, text="Clear", command=clear_all, style='TButton')
    clear_button.grid(column=1, row=4, sticky="ew", pady=5)


    def on_close():
        global anim
        if anim is not None:
            anim.event_source.stop()

        
        plt.close('all')
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)

    # Start the GUI event loop
    root.mainloop()



