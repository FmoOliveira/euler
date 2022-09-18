'''
The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 - 385 = 2640
.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


(1 + 2 + ... + n)^2 = n^2 * (n+1)^2 * 1/4

1^2 + 2^2 + ... + n^2 = n * (n+1) * (2n+1) * 1/6

Thus easily applicable to any n.


'''


import time
start_time = time.time()

def sum_of_squares_first_n(n):
    return (n * (n + 1) * (2 * n + 1)) // 6

def square_of_sum_first_n(n):    
    return ((n * (n + 1)) // 2) ** 2




print(square_of_sum_first_n(100) - sum_of_squares_first_n(100))

print("--- %s seconds ---" % (time.time() - start_time))