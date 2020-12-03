import conformal_mapping_toolbox as cmtb
import pygame_drawer
import cmath
import time


def user_area_func(x, y):
    z = complex(x, y)
    return abs(z) < 1


def user_w_func(x, y):
    z = complex(x, y)
    if z == 0:
        return [cmath.inf, cmath.inf]
    res = 1 / z
    return [res.real, res.imag]


def main():
    pg_screen = pygame_drawer.init((cmtb.window_size_x, cmtb.window_size_y))

    s = time.time()
    x_axis, y_axis = cmtb.gen_axis_points()
    x_axis = cmtb.prepare_points_to_pygame(x_axis)
    y_axis = cmtb.prepare_points_to_pygame(y_axis)
    print(time.time() - s)

    s = time.time()
    points = cmtb.gen_area_points(user_area_func)
    points = cmtb.compute_user_w_func(user_w_func, points)
    points = cmtb.prepare_points_to_pygame(points)
    print(time.time() - s)

    s = time.time()
    pygame_drawer.clean_screen(pg_screen)
    pygame_drawer.add_points_to_plot(pg_screen, x_axis)
    pygame_drawer.add_points_to_plot(pg_screen, y_axis)
    pygame_drawer.add_points_to_plot(pg_screen, points)
    pygame_drawer.redraw(pg_screen)
    print(time.time() - s)

    while 1:
        pygame_drawer.exit_cond()

    pass


if __name__ == '__main__':
    main()
    pass

