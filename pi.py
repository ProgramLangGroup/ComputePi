# authors: Brandon Grant, Dylan Hensley, Ethan Twilley
# date: 10/3/2018
# description: program approximates pi

import random as point


class Pi:

    within = 0
    pi = 0

    # constructor initializes sample size, iterates x and y, and calculates pi
    def __init__(self, sample):
        self.sample = sample

        for _ in range(sample):
            self.x = point.random() ** 2
            self.y = point.random() ** 2
            self.is_within()

        self.pi = 4 * self.within / sample

    # getter function for x
    @property
    def x(self):
        return self.__x

    # getter function for y
    @property
    def y(self):
        return self.__y

    # setter function for x
    @x.setter
    def x(self, points):
        self.__x = points

    # setter function for y
    @y.setter
    def y(self, points):
        self.__y = points

    # function determines if x and y points are within circle
    def is_within(self):
        if self.__x + self.__y <= 1:
            self.within += 1
        return self.within
