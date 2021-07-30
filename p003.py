#
# Solution to problem 3 of Project Euler
# Copyright (c) 2021 Joeri King. All rights reserved.
# https://github.com/joeriking/project-euler
#

number = 13195

prime_factors = []

i = 1

while i <= number:
    i += 1
    if number % i == 0:
        prime_factors.append(i)
        
print(prime_factors)
