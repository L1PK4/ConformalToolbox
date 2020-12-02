import conformal_mapping_toolbox as cmtb
import pygame_drawer


def user_area_func(x, y):
    return x ** 2 + y ** 2 < 1 and x > -1/2 and y < 0


def user_w_func(x, y):
    z = complex(x, y)
    res = 1j * (z - 1) / (z + 1)
    return [res.real, res.imag]


def main():
    pg_screen = pygame_drawer.init((cmtb.window_size_x, cmtb.window_size_y))

    x_axis, y_axis = cmtb.gen_axis_points()
    x_axis = cmtb.prepare_points_to_pygame(x_axis)
    y_axis = cmtb.prepare_points_to_pygame(y_axis)

    points = cmtb.gen_area_points(user_area_func)
    points = cmtb.compute_user_w_func(user_w_func, points)
    points = cmtb.prepare_points_to_pygame(points)

    pygame_drawer.clean_screen(pg_screen)
    pygame_drawer.add_points_to_plot(pg_screen, x_axis)
    pygame_drawer.add_points_to_plot(pg_screen, y_axis)
    pygame_drawer.add_points_to_plot(pg_screen, points)
    pygame_drawer.redraw(pg_screen)
    
    while 1:
        pygame_drawer.exit_cond()

    pass


if __name__ == '__main__':
    main()
    pass
