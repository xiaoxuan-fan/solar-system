# Author: Xiaoxuan
# Date: 5/11/2021
# Purpose: create a System class to simulate systems of celestial bodies
from math import sqrt
G = 6.67384e-11


class System:
    def __init__(self, body_list):
        self.body_list = body_list

    def update(self, timestep):
        for body in self.body_list:
            body.update_position(timestep)
        for body in self.body_list:
            (ax, ay) = self.compute_acceleration(body)
            body.update_velocity(ax, ay, timestep)

    def draw(self, cx, cy, pixels_per_meter):
        for body in self.body_list:
            body.draw(cx, cy, pixels_per_meter)

    def compute_acceleration(self, body):
        sum_ax = 0
        sum_ay = 0
        for mbody in self.body_list:
            if mbody is not body:
                dx = mbody.x - body.x
                dy = mbody.y - body.y
                d = sqrt(dx * dx + dy * dy)
                a = G * mbody.mass / (d * d)
                ax = a * dx / d
                ay = a * dy / d
                sum_ax += ax
                sum_ay += ay
        return sum_ax, sum_ay
