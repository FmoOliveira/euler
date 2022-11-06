'''

The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

'''



import time
from unicodedata import digit
start_time = time.time()

#v1

# digit = '73167176531330624919225119674426574742355349194934' \
#         '96983520312774506326239578318016984801869478851843' \
#         '85861560789112949495459501737958331952853208805511' \
#         '12540698747158523863050715693290963295227443043557' \
#         '66896648950445244523161731856403098711121722383113' \
#         '62229893423380308135336276614282806444486645238749' \
#         '30358907296290491560440772390713810515859307960866' \
#         '70172427121883998797908792274921901699720888093776' \
#         '65727333001053367881220235421809751254540594752243' \
#         '52584907711670556013604839586446706324415722155397' \
#         '53697817977846174064955149290862569321978468622482' \
#         '83972241375657056057490261407972968652414535100474' \
#         '82166370484403199890008895243450658541227588666881' \
#         '16427171479924442928230863465674813919123162824586' \
#         '17866458359124566529476545682848912883142607690042' \
#         '24219022671055626321111109370544217506941658960408' \
#         '07198403850962455444362981230987879927244284909188' \
#         '84580156166097919133875499200524063689912560717606' \
#         '05886116467109405077541002256983155200055935729725' \
#         '71636269561882670428252483600823257530420752963450'

# maxProduct = 0
# listProducts = []
# a = 0
# b = 13

# for el in range(0, len(digit)-13):
#     for i in range(a, b):
#         if i == a:
#             maxProduct = int(digit[i])
#         else:
#             maxProduct *= int(digit[i])
#     listProducts.append(maxProduct)
#     a += 1
#     b += 1


# print(max(listProducts))


#v2
# from string import whitespace
# from operator import mul
# from functools import reduce

# data = open('aux/dataP8') # Number pasted to file.
# nos = [int(c) for line in data for c in line if c not in whitespace]
# print (max([reduce(mul, nos[i:i+13]) for i in range(len(nos)-13)]))

#v3
from functools import reduce
digits = '73167176531330624919225119674426574742355349194934' \
        '96983520312774506326239578318016984801869478851843' \
        '85861560789112949495459501737958331952853208805511' \
        '12540698747158523863050715693290963295227443043557' \
        '66896648950445244523161731856403098711121722383113' \
        '62229893423380308135336276614282806444486645238749' \
        '30358907296290491560440772390713810515859307960866' \
        '70172427121883998797908792274921901699720888093776' \
        '65727333001053367881220235421809751254540594752243' \
        '52584907711670556013604839586446706324415722155397' \
        '53697817977846174064955149290862569321978468622482' \
        '83972241375657056057490261407972968652414535100474' \
        '82166370484403199890008895243450658541227588666881' \
        '16427171479924442928230863465674813919123162824586' \
        '17866458359124566529476545682848912883142607690042' \
        '24219022671055626321111109370544217506941658960408' \
        '07198403850962455444362981230987879927244284909188' \
        '84580156166097919133875499200524063689912560717606' \
        '05886116467109405077541002256983155200055935729725' \
        '71636269561882670428252483600823257530420752963450'

# https://www.geeksforgeeks.org/reduce-in-python/
print(max([reduce(lambda x, y: int(x) * int(y), digits[i:i+13]) for i in range(len(digits)- 13)]))

print("--- %s seconds ---" % (time.time() - start_time))