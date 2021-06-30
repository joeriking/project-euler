#Copyright (c) 2021 Joeri King

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

#Solution to Problem 1 of Project Euler:
n = 1000

#Use integer division to arrive at the largest multiple of 3 or 5.
largest_multiple_3 = (n - 1) // 3
largest_multiple_5 = (n - 1) // 5

#Create a list of multiples of 3 or 5.
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

#Combine lists and remove duplicates.
multiples = multiples_3 + multiples_5
multiples = list(dict.fromkeys(multiples))
multiples.sort()

#Calculate the sum of all multiples.
solution = sum(multiples)
print(solution)
