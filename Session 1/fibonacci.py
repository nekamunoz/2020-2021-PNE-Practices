series = [0, 1]
a = 0
b = 1
for i in range(0,10):
    c = b + a
    series.append(c)
    a = b
    b = c
print(series)