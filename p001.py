#
# Solution to problem 1 of Project Euler
# Copyright (c) 2021 Joeri King. All rights reserved.
# https://github.com/joeriking/project-euler
#

# Find the sum of all multiples below n.
n = 1000

# Use integer division to arrive at the largest multiple of 3 or 5.
largest_multiple_3 = (n - 1) // 3
largest_multiple_5 = (n - 1) // 5

# Create a list of multiples of 3 or 5.
i = 1
multiples_3 = []
while i <= largest_multiple_3:
    multiple = 3 * i
    multiples_3.append(multiple)
    i += 1

i = 1
multiples_5 = []
while i <= largest_multiple_5:
    multiple = 5 * i
    multiples_5.append(multiple)
    i += 1

# Combine lists and remove duplicates.
multiples = multiples_3 + multiples_5
multiples = list(dict.fromkeys(multiples))
multiples.sort()

# Calculate the sum of all multiples.
solution = sum(multiples)
print(solution)
