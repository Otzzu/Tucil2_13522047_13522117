import turtle

def bezier_curve(control_points, iterations):
    if len(control_points) == 1:
        return control_points[0]

    # Divide
    left_points = control_points[:len(control_points)//2]
    right_points = control_points[len(control_points)//2:]

    # Conquer
    left_curve = bezier_curve(left_points, iterations)
    right_curve = bezier_curve(right_points, iterations)

    # Combine
    x = (1 - iterations) * left_curve[0] + iterations * right_curve[0]
    y = (1 - iterations) * left_curve[1] + iterations * right_curve[1]

    return (x, y)

def draw_bezier_curve(control_points, num_points=100):
    turtle.penup()
    turtle.goto(control_points[0])  # Pindahkan kursor ke titik awal
    turtle.pendown()

    points = []
    for i in range(num_points + 1):
        t = i / num_points
        point = bezier_curve(control_points, t)
        points.append(point)

    print(points)
    

# Contoh penggunaan:
control_points = [(0, 100), (100, 200) , (300, 100)]
draw_bezier_curve(control_points, 8)
