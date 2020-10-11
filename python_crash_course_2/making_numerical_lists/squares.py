#!/usr/bin/python3.6


#squares = []


# First way with a variable named square.
#for value in range(1, 11):
#    square = value ** 2
#    squares.append(square)
#
#
# Second way without a variable

#for value in range(1, 11):
#    squares.append(value**2)
#
#
# Third way: list comprehension

squares = [value ** 2 for value in range(1, 11)]

print(squares)
