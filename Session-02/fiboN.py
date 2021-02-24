def fibon(n):
    e = 0
    a, b = 0, 1
    for i in range(0, n):
        c = b + a
        a, b = b, c
        e += 1
        if e == n:
           return a

n = 5
j = 10
w = 15
print(n, "th Fibonacci term: ", fibon(n))
print(j, "th Fibonacci term: ", fibon(j))
print(w, "th Fibonacci term: ", fibon(w))
