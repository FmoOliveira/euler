'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''


'''


    Searching for:

    a^2 + b^2 = c^2 (triplet)
    a + b + c = n   (sum equals input)

    Solve by searching over a (i.e. a fixed for an iteration). With a fixed, we have two equations and two unknowns (b, c):

    b + c = n - a
    c^2 - b^2 = a^2

    Solution is:

    denom = 2*(n-a)
    num = 2*a**2 + n**2 - 2*n*a
    if denom > 0 and num % denom == 0:
        c = num // denom
        b = n - a - c
        if b > a:
            (a, b, c) # is a solution

    Iterate a range(1, n) to get different solutions



Without programming:

a= 2mn; b= m^2 -n^2; c= m^2 + n^2;
a + b + c = 1000;

2mn + (m^2 -n^2) + (m^2 + n^2) = 1000;
2mn + 2m^2 = 1000;
2m(m+n) = 1000;
m(m+n) = 500;

m>n;

m= 20; n= 5;

a= 200; b= 375; c= 425;


'''
import math
import time
start_time = time.time()
def solve_pythagorean_triplets(n):
    " Solves for triplets whose sum equals n "
    solutions = []
    for a in range(1, n):
        denom = 2*(n-a)
        num = 2*a**2 + n**2 - 2*n*a
        if denom > 0 and num % denom == 0:
            c = num // denom
            b = n - a - c
            if b > a:
                solutions.append((a, b, c))

    return solutions

triplet = solve_pythagorean_triplets(1000)[0]

print(triplet)
print(math.prod(triplet))
print("--- %s seconds ---" % (time.time() - start_time))
