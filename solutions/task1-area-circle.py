# First step is to import the math module. The math module contains all mathematical functionalities.
import math

# Read radius from input
radius = float(input())

# Now you can use 'math.pi' and the square of radius to calculate the area of the circle. 
# Write down the formula and print it.
# Remember the formula to calculate area of circle is pi*r^2.'
circle = math.pi * (radius ** 2)
print(round(circle, 2))