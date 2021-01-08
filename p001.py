#
# Solutions to Project Euler 
# Problem 1: Multiples of 3 and 5 
# Copyright (c) Joeri King. All rights reserved.
#

counter = 0

for x in range(1000):
        if (x % 3 == 0 or x % 5 == 0):
                counter += x

print(counter)
