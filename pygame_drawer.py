
import pygame
import math

_screen_size = (0, 0)
_screen_color = (0, 0, 0)
_car_color = (255, 0, 0)


def check_point(point):
    if math.isinf(point[0]) or math.isinf(point[1]) or math.isnan(point[0]) or math.isnan(point[1]) or \
       not (int(point[0]) in range(0, _screen_size[0]) and int(point[1]) in range(0, _screen_size[1])):
        return False
    return True


def clean_screen(screen):
    pixel_arr = pygame.PixelArray(screen.get_surface())
    for x in range(_screen_size[0]):
        for y in range(_screen_size[1]):
            pixel_arr[x, y] = _screen_color


def init(size):
    pygame.init()
    screen = pygame.display
    screen.init()
    screen.set_mode(size)
    global _screen_size
    _screen_size = size
    return screen


def add_points_to_plot(screen, points, color):
    pixel_arr = pygame.PixelArray(screen.get_surface())
    for p in points:
        if check_point(p):
            pixel_arr[int(p[0]), int(p[1])] = color


def redraw(screen):
    screen.update()


def exit_cond():
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()