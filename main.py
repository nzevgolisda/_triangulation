from Board import points
# (x, y) in Ω = [0,1]x[0,1] counter-clockwise
a, b, c, d = [[0,0], [1,0], [1,1], [0,1]]
n = 10
ab = points(a, b, n)
bc = points(b, c, n)
ac = points(a, c, n) # diagonal
cd = points(c, d, n)
da = points(d, a, n)
print(ab)
print(bc)
print(ac)
print(cd)
print(da)