'''
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
'''
import time
start_time = time.time()
# read numbers from file
f = open('aux/largeNumber.txt', 'r')
numbers = []
for lines in f:
    numbers.append(lines)
f.close()

# convert to int
numbers = [int(x) for x in numbers]

print(str(sum(numbers))[:10])
print("--- %s seconds ---" % (time.time() - start_time))