
#
# Solution to Project Euler problem 254
# Copyright (c) Project Nayuki. All rights reserved.
#
# https://www.nayuki.io/page/project-euler-solutions
# https://github.com/nayuki/Project-Euler-solutions
#

def factorial(n):
    if (n==0):
        return 1
    return n * factorial(n-1)

def f(n):
    str_of_n = str(n) # to get each digit
    total_sum = 0
    for digit in str_of_n:
        if (digit == '0'): #0! is 1 -> lead to a problem
            total_sum += 0
        else:
            total_sum += factorial(int(digit))
    return total_sum

def sf(n):
    str_of_fn = str(f(n))
    total_sum = 0
    for digit in str_of_fn:
        total_sum += int(digit)
    return total_sum

def g(i):
    n = 0
    while sf(n) != i:
         n += 1
    return n

def sg(i):
    str_of_gi = str(g(i))
    total_sum = 0
    for digit in str_of_gi:
        total_sum += int(digit)
    return total_sum

# sum of sg(i) for 1 less or equal i less or equal 150
def final_sum(border1, border2):
    sum = 0
    for i in range(border1,border2+1):
        print("Sum is ",sum)
        print("currently at i=",i)
        sum += sg(i)
        print("Final Sum:",sum)
    return sum

# for testing:
print(f(0))
print(sf(342))
print(g(5))
print(sg(5))
print(final_sum(1,20))
# to get actual solution:
print(final_sum(1,150))

# solution is:
