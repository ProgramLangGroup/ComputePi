from pi import *
print('What is your first name?')
first = input()
print('What is your last name?')
last = input()
name = Pi(first, last)
print('Your full name is ' + name.fullname)
print('Your first name is ' + name.first)
print('Your last name is ' + name.last)
