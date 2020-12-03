import numpy as np

x_axis_max = 5
y_axis_max = 5

x_axis_min = -5
y_axis_min = -5

window_size_x = 1000
window_size_y = 1000

dt = 0.001


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
    x_axis = [[x, 0] for x in np.arange(x_axis_min, x_axis_max, dt)]
    y_axis = [[0, y] for y in np.arange(y_axis_min, y_axis_max, dt)]
    return x_axis, y_axis


def prepare_points_to_pygame(points):
    for p in points:
        p[0] = my_map(p[0], x_axis_min, x_axis_max, 0, window_size_x)
        p[1] = my_map(p[1], y_axis_max, y_axis_min, 0, window_size_y)
    return points


def compute_user_w_func(func, points):
    return [func(p[0], p[1]) for p in points]
