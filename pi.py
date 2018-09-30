# authors: Brandon Grant, Dylan Hensley, Ethan Twilley
# date: 10/3/2018
# description: program approximates pi

import random as r


class Pi:

    within, pi = 0, 0

    # constructor initializes sample size, iterates x and y, and calculates pi
    def __init__(self, sample):

        for _ in range(sample):
            self.x = r.random() ** 2
            self.y = r.random() ** 2
            self.is_within()

        self.pi = 4 * self.within / sample

    # getter function for x
    @property
    def x(self):
        return self.__x

    # setter function for x
    @x.setter
    def x(self, point):
        self.__x = point

    # getter function for y
    @property
    def y(self):
        return self.__y

    # setter function for y
    @y.setter
    def y(self, point):
        self.__y = point

    # function determines if x and y points are within circle
    def is_within(self):
        if self.__x + self.__y <= 1:
            self.within += 1
        return
