# authors: Brandon Grant, Dylan Hensley, Ethan Twilley
# date: 10/3/2018
# description: program approximates pi

from pi import *
print('Enter the sample size of points: ')
sample = int(input())
init = Pi(sample)
print('Approximation of pi = ' + init.pi.__str__())
