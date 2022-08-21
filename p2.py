def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
# n=3
# sum=0
# while n < 4000000:
#     if n % 2 == 0:
#         sum += n
#     n = fibonacci(n)
#
#print(fibonacci(10))
