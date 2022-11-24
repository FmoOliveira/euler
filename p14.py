'''
Longest Collatz sequence


The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), 
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

'''
import time
start_time = time.time()

def collatz(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


#v1
# def collatz_sequence(n):
#     list.append(int(n))
#     if n == 1:
#         return 1
#     else:
#         return collatz_sequence(collatz(n))
    
# max = 0
# start = 1000000
# list = []

# while start > 800000:
#     collatz_sequence(start)
#     if len(list) > max:
#         max = len(list)
#         print('start: ' + str(start) + ' length: ' + str(max))
#     start -= 1
#     list = []

# print('start: ' + str(start) + ' length: ' + str(max))

#v2
def distance(n, cache={1:1}):
    if n not in cache: 
        cache[n] = distance(collatz(n)) + 1
    return cache[n]


print(max(range(800000,1000000), key=distance))
print("--- %s seconds ---" % (time.time() - start_time))