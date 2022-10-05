"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""
import time
start_time = time.time()

i=100
w=100

max = 0

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_max(n):
    global max
    if n > max:
        max = n

for i in range(100, 1000):
    for w in range(100, 1000):
        if is_palindrome(i*w):
            is_max(i*w)


# while i < 1000:
#     while w < 1000:
#         if is_palindrome(i*w):
#             is_max(i*w)
#         w += 1
#     i += 1
#     w = 100

print(max)
print("--- %s seconds ---" % (time.time() - start_time))