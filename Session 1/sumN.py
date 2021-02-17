def fibon(n):
    e = 0
    sum = 0
    a, b = 0, 1
    for i in range(0, n):
        c = b + a
        a, b = b, c
        e += 1
        sum += b + c
        if e == n:
           return sum
n = 5
j = 10
print("Sum of the first", n, "numbers of the Fibonacci series: ", fibon(n))
print("Sum of the first", j, "numbers of the Fibonacci series: ", fibon(j))