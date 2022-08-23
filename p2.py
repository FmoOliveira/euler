def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# sum = 0
# term = 1

# while term < 4000000:
#     if term % 2 == 0:
#         sum += term
#     term = fibonacci(term)
i=1
sum=0
n=0
while n < 4000000:
    n = fibonacci(i)
    if n % 2 == 0:
        sum += n
    i += 1

print(sum)
