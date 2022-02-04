def add(a, b):
    return [a[0]+b[0], a[1]+b[1]]
def sub(a, b):
    return [a[0]-b[0], a[1]-b[1]]
def dist(a, b):
    v = sub(a, b)
    return (v[0]**2 + v[1]**2)**0.5
def points(a, b, n):
    L = []  # a, b in R^2, t in [0,1]
    for t in range(n+1): # Vector x = (b-a)t + a
        x = (b[0]-a[0])*t/n + a[0]
        y = (b[1]-a[1])*t/n + a[1]
        X, Y = [round(10*x)/10, round(10*y)/10]
        L.append([X, Y])
    return L
