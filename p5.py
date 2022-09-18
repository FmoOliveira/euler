'''

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''
import time
start_time = time.time()

# min = 1
# check  = 1
# target = 20
# while check < target:
#     for i in range(target,1,-1):
#         if min % i == 0:
#             check += 1
#         else:
#             check = 1
#             min += 1
#             break
# print(min)


# i = 1
# for k in (range(1, 21)):
#     if i % k > 0:
#         for j in range(1, 21):
#             if (i*j) % k == 0:
#                 i *= j
#                 break
# print (i)


# import functools
# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# def lcm(a, b):
#     return a*b/gcd(a, b)

# print (functools.reduce(lcm, range(1, 20+1)))

#https://en.wikipedia.org/wiki/Least_common_multiple#Reduction_by_the_greatest_common_divisor

import math
print(math.lcm(*range(1, 20+1)))

print("--- %s seconds ---" % (time.time() - start_time))