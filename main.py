import conformal_mapping_toolbox as cmtb
import pygame_drawer
import cmath
import time


user_area_color = (255, 255, 255)
axis_color = (0, 255, 0)


def user_area_func(z):
    return abs(z) < 2


def user_w1_func(z):
    return -1 / z


def main():
    cmtb.setup_axis_values(-5, 5, -5, 5)
    cmtb.setup_dt_value(0.01)
    cmtb.setup_window_size(1000, 1000)

    pg_screen = pygame_drawer.init(cmtb.get_window_size())

    s = time.time()
    x_axis, y_axis = cmtb.gen_axis_points()
    x_axis = cmtb.prepare_points_to_pygame(x_axis)
    y_axis = cmtb.prepare_points_to_pygame(y_axis)
    print(time.time() - s)

    s = time.time()
    points = cmtb.gen_area_points(user_area_func)
    points = cmtb.compute_user_w_func(user_w1_func, points)
    points = cmtb.prepare_points_to_pygame(points)
    print(time.time() - s)

    s = time.time()
    pygame_drawer.clean_screen(pg_screen)
    pygame_drawer.add_points_to_plot(pg_screen, points, user_area_color)
    pygame_drawer.add_points_to_plot(pg_screen, x_axis, axis_color)
    pygame_drawer.add_points_to_plot(pg_screen, y_axis, axis_color)
    pygame_drawer.redraw(pg_screen)
    print(time.time() - s)

    while 1:
        pygame_drawer.exit_cond()

    pass


if __name__ == '__main__':
    main()
    pass

