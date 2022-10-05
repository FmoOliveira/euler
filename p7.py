'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

'''

# https://geekflare.com/prime-number-in-python/

import time
start_time = time.time()

import math
def is_prime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if (n%i) == 0:
      return False
  return True



primes = []
i=2
while len(primes) < 10001:
    if is_prime(i):
        primes.append(i)
    i+=1


print(primes[-1])
print("--- %s seconds ---" % (time.time() - start_time))