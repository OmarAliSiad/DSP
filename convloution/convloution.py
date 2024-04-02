def convloution (h,x):
    m = len(h)
    n = len(x)
    y = [0] * (m+n-1)
    for i in range(m):
        for j in range(n):
            y[i+j] += h[i]*x[i]
    return y


h = [0,1,1]
x = [1,1,1]
y = convloution(h,x)
print(y)