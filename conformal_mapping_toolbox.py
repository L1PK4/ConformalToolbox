import numpy as np


x_axis_max = 15
y_axis_max = 15

x_axis_min = -5
y_axis_min = -5

window_size_x = 1000
window_size_y = 1000

dt = 0.005


def my_map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def gen_area_points(area):
    points = []
    for x in np.arange(x_axis_min, x_axis_max, dt):
        for y in np.arange(y_axis_min, y_axis_max, dt):
            if area(x, y):
                points.append([x, y])
    return points


def gen_axis_points():
    x_axis = []
    y_axis = []
    for x in np.arange(x_axis_min, x_axis_max, dt):
        x_axis.append([x, 0])
    for y in np.arange(y_axis_min, y_axis_max, dt):
        y_axis.append([0, y])
    return x_axis, y_axis


def prepare_points_to_pygame(points):
    for p in points:
        p[0] = my_map(p[0], x_axis_min, x_axis_max, 0, window_size_x)
        p[1] = my_map(p[1], y_axis_max, y_axis_min, 0, window_size_y)
    return points


def compute_user_w_func(func, points):
    res = []
    for i in range(len(points)):
        res.append(func(points[i][0], points[i][1]))
    return res
