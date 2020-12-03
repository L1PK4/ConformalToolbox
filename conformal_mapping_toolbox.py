import numpy as np

_x_axis_max = 10
_y_axis_max = 10

_x_axis_min = -10
_y_axis_min = -10

_window_size_x = 1000
_window_size_y = 1000

_dt = 0.01


def _convert_complex_to_real(p):
    return [p.real, p.imag]


def _my_map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def setup_axis_values(x_min, x_max, y_min, y_max):
    global _x_axis_min
    global _x_axis_max
    global _y_axis_min
    global _y_axis_max

    _x_axis_min = x_min
    _x_axis_max = x_max
    _y_axis_min = y_min
    _y_axis_max = y_max


def setup_dt_value(dt):
    global _dt
    _dt = dt


def setup_window_size(win_x, win_y):
    global _window_size_x
    global _window_size_y

    _window_size_x = win_x
    _window_size_y = win_y


def get_window_size():
    return _window_size_x, _window_size_y


def gen_area_points(area):
    points = []
    for x in np.arange(_x_axis_min, _x_axis_max, _dt):
        for y in np.arange(_y_axis_min, _y_axis_max, _dt):
            if area(complex(x, y)):
                points.append([x, y])
    return points


def gen_axis_points():
    x_axis = [[x, 0] for x in np.arange(_x_axis_min, _x_axis_max, _dt)]
    y_axis = [[0, y] for y in np.arange(_y_axis_min, _y_axis_max, _dt)]
    return x_axis, y_axis


def prepare_points_to_pygame(points):
    for p in points:
        p[0] = _my_map(p[0], _x_axis_min, _x_axis_max, 0, _window_size_x)
        p[1] = _my_map(p[1], _y_axis_max, _y_axis_min, 0, _window_size_y)
    return points


def compute_user_w_func(func, points):
    return [_convert_complex_to_real(func(complex(p[0], p[1]))) for p in points]
