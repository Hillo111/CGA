import ctypes
import pynput as pyn
from gradients import do_gradient
import random
import datetime as dt
from math import *

last_done = dt.datetime.now()
wait = 5


def change_background(*args):
    global last_done
    if dt.timedelta.total_seconds(dt.datetime.now() - last_done) > wait:
        colour_count = 4
        colours = []
        a, b = map(int, pyn.mouse.Controller().position)
        a, b = floor(a / 1463 * 255), floor(b / 823 * 255)
        a, b = min(a, b), max(a, b)
        for i in range(colour_count):
            colours.append([random.randint(a, b), random.randint(a, b), random.randint(a, b)])

        try:
            do_gradient(1463, 823, colours, 'HORIZONTAL', 'art.png')
        except:
            pass

        ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:/users/max/pycharmprojects/art/art.png", 0)

        last_done = dt.datetime.now()


with pyn.mouse.Listener(
        on_click=change_background) as listener2:
    listener2.join()

'''
import ctypes
import pynput as pyn
from gradients import do_gradient
import random
import datetime as dt
from math import *

last_done = dt.datetime.now()
to = 5


def change_background(*args):
    global last_done
    if dt.timedelta.total_seconds(dt.datetime.now() - last_done) > 5:
        pos = pyn.mouse.Controller().position
        colours = []
        colour_count = floor((pos[0] + pos[1]) / 2286 * 3) + 2
        for i in range(colour_count):
            colours.append([floor(pos[0] / 1463 * 255), floor(pos[1] / 823 * 255), floor((pos[0] + pos[1]) / 2286 * 255)])
        print('in change', colours)
        print('position', pos)
        print('first', pos[0] / 1463 * 255)
        print('second', pos[1] / 823 * 255)
        print('third', (pos[0] + pos[1]) / 2286 * 255)

        try:
            do_gradient(1463, 823, colours, 'HORIZONTAL', 'art.png')
        except:
            pass

        ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:/users/max/pycharmprojects/art/art.png", 0)

        last_done = dt.datetime.now()


with pyn.mouse.Listener(
        on_click=change_background) as listener2:
    listener2.join()
'''