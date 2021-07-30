#
# Solution to problem 2 of Project Euler
# Copyright (c) 2021 Joeri King. All rights reserved.
# https://github.com/joeriking/project-euler
#

fibonacci = [1]
i = 2
while i < 4000000:
    fibonacci.append(i)
    i += fibonacci[-2]

even = []
for j in fibonacci:
    if j % 2 == 0:
        even.append(j)

print(sum(even))
