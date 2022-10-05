# Based on example code earthmoon.py
# Author: Xiaoxuan
# Date: 5/11/2021
# Purpose: simulate the earth-moon system
from cs1lib import *
from system import System
from body import Body

WINDOW_WIDTH = 400          # pixels
WINDOW_HEIGHT = 400         # pixels

FRAMERATE = 30              # frames per second
TIMESTEP = 1 / FRAMERATE    # seconds per frame

TIME_SCALE = 100000         # simulated seconds per second
DISTANCE_SCALE = 3 / 1e7    # pixels per meter


def main():
    set_clear_color(0, 0, 0)    # black background
    clear()

    earth_moon.draw(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, DISTANCE_SCALE)
    earth_moon.update(TIMESTEP * TIME_SCALE)


earth = Body(5.9736e24, 0, 0, 0, 0, 24, 0, 0, 1)           # blue earth
moon = Body(7.3477e22, 3.84403e8, 0, 0, 1022, 4, 1, 1, 1)  # white moon
earth_moon = System([earth, moon])

start_graphics(main, framerate=FRAMERATE)
