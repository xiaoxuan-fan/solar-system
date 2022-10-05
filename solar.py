# Author: Xiaoxuan
# Date: 5/11/2021
# Purpose: simulate the solar system (first four planets)
from cs1lib import *
from system import System
from body import Body

WINDOW_WIDTH = 400          # pixels
WINDOW_HEIGHT = 400         # pixels

FRAMERATE = 30              # frames per second
TIMESTEP = 1 / FRAMERATE    # seconds per frame

TIME_SCALE = 3e6            # simulated seconds per second
DISTANCE_SCALE = 7 / 1e10   # pixels per meter


def main():
    set_clear_color(0, 0, 0)    # black background
    clear()

    solar_system.draw(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, DISTANCE_SCALE)
    solar_system.update(TIMESTEP * TIME_SCALE)


sun = Body(1.98892e30, 0, 0, 0, 0, 15, 1, 1, 0)
mercury = Body(0.33e24, -57.9e9, 0, 0, 47890, 3, 0, 1, 1)
venus = Body(4.87e24, -108.2e9, 0, 0, 35040, 6, 1, 0, 1)
earth = Body(5.97e24, -149.6e9, 0, 0, 29790, 6, 0, 0, 1)
mars = Body(0.642e24, -227.9e9, 0, 0, 24140, 4, 1, 0, 0)
solar_system = System([sun, mercury, venus, earth, mars])

start_graphics(main, framerate=FRAMERATE)
