import tkinter as tk
from tkinter import ttk
from bezier import BezierCurve
from bruteforce3 import BezierCurve3Points
from bruteforce4 import BezierCurve4Points
from bruteforce5 import BezierCurve5Points
from bruteforce6 import BezierCurve6Points
from bruteforce7 import BezierCurve7Points
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

anim = None
anim2 = None
canvas = None
canvas2 = None
canvas3 = None
canvas4 = None

def draw_bezier_curve_animation(control_points, num_iterate, canvas, canvas2, figure, ax, animate,  ax2):
    if animate != None:
        animate.event_source.stop()
    ax.clear()
    ax2.clear()
    bezier_curve = BezierCurve(control_points, num_iterate)
    bezier_curve.calc()

    anim = bezier_curve.draw_animate(figure, ax)
    bezier_curve.draw(ax2)
    canvas.draw()
    canvas2.draw()
    return anim, canvas, canvas2

def draw_brute_force_curve_animation(control_points, num_iterate, canvas3, canvas4, figure, ax3, animate, ax4):
    if animate != None:
        animate.event_source.stop()
    ax3.clear()
    ax4.clear()
    
    if len(control_points) == 3:
        brute_force_curve = BezierCurve3Points(control_points[0], control_points[1], control_points[2], num_iterate)
    elif len(control_points) == 4:
        brute_force_curve = BezierCurve4Points(control_points[0], control_points[1], control_points[2], control_points[3], num_iterate)
    elif len(control_points) == 5:
        brute_force_curve = BezierCurve5Points(control_points[0], control_points[1], control_points[2], control_points[3], control_points[4], num_iterate)
    elif len(control_points) == 6:
        brute_force_curve = BezierCurve6Points(control_points[0], control_points[1], control_points[2], control_points[3], control_points[4], control_points[5], num_iterate)
    elif len(control_points) == 7:
        brute_force_curve = BezierCurve7Points(control_points[0], control_points[1], control_points[2], control_points[3], control_points[4], control_points[5], control_points[6], num_iterate)
    else:
        raise ValueError("Unsupported number of control points")

    anim = brute_force_curve.draw_animation_curve(figure, ax3)
    brute_force_curve.draw_curve(ax4)
    canvas3.draw()
    canvas4.draw()
    return anim, canvas3, canvas4

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
    ttk.Label(input_frame, text="Control Points (x1,y1;x2,y2;...)").grid(column=0, row=0, sticky="w")
    control_points_entry = ttk.Entry(input_frame, textvariable=control_points_var, width=40)
    control_points_entry.grid(column=1, row=0, sticky="ew")

    ttk.Label(input_frame, text="Number of Iterations").grid(column=0, row=1, sticky="w")
    num_iterate_entry = ttk.Entry(input_frame, textvariable=num_iterate_var, width=40)
    num_iterate_entry.grid(column=1, row=1, sticky="ew")

    # Frame for the plot
    main_frame = ttk.Frame(root)
    main_frame.pack(fill="both", expand=True)
    
    
    plot_frame = ttk.Frame(main_frame)
    plot_frame.grid(row=0, column=1, padx=10, pady=10)
    
    plot_frame2 = ttk.Frame(main_frame)
    plot_frame2.grid(row=0, column=0, padx=10, pady=10)
    
    plot_frame3 = ttk.Frame(main_frame)
    plot_frame3.grid(row=1, column=1, padx=10, pady=10)
    
    plot_frame4 = ttk.Frame(main_frame)
    plot_frame4.grid(row=1, column=0, padx=10, pady=10)
    
    
    figure, ax = plt.subplots(figsize=(7,4))
    global canvas
    canvas = FigureCanvasTkAgg(figure, plot_frame)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    
    figure2, ax2 = plt.subplots(figsize=(7,4))
    global canvas2
    canvas2 = FigureCanvasTkAgg(figure2, plot_frame2)
    canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    
    figure3, ax3 = plt.subplots(figsize=(7,4))
    global canvas3
    canvas3 = FigureCanvasTkAgg(figure3, plot_frame3)
    canvas3.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    
    figure4, ax4 = plt.subplots(figsize=(7,4))
    global canvas4
    canvas4 = FigureCanvasTkAgg(figure4, plot_frame4)
    canvas4.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    

    # Function to parse control points input
    def parse_control_points(input_str):
        points = []
        for point_str in input_str.split(";"):
            x, y = map(float, point_str.split(","))
            points.append((x, y))
        return points

    # Function to handle drawing the curve
    def handle_draw():
        control_points = parse_control_points(control_points_var.get())
        num_iterate = num_iterate_var.get()
        global anim, canvas, canvas2, canvas3, canvas4
        anim, canvas, canvas2 = draw_bezier_curve_animation(control_points, num_iterate, canvas, canvas2, figure, ax, anim, ax2)
        anim, canvas3, canvas4 = draw_brute_force_curve_animation(control_points, num_iterate, canvas3, canvas4, figure3, ax3, anim2, ax4)

    # Button to draw the curve
    draw_button = ttk.Button(input_frame, text="Draw Curve", command=handle_draw)
    draw_button.grid(column=1, row=2, sticky="ew")

    def on_close():
        global anim, anim2
        if anim is not None:
            anim.event_source.stop()
        if anim2 is not None:
            anim2.event_source.stop()
        
        plt.close('all')
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)

    # Start the GUI event loop
    root.mainloop()


if __name__ == "__main__":
    main()
