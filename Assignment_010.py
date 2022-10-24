import math

# Make an iterator that delivers all numbers in pairs like (2,1), (3,1), (3,2), (4,1), (4,2), (4,3) etc
def pairs():
    m = 2
    n = 1
    createPairs = True
    while createPairs:
        while m > n:
            for n in range(1,m):
                yield ((m,n))
            m += 1

# From the above iterator exclude coprime and odd numbers
def filterPairs():
    for m,n in pairs():
        if (m%2 == 0 and n%2 == 0):
            if (math.gcd(m,n) == 1):
                yield((m,n))

# Write another iterator that uses the above and yields a tuple (a,b,c) where 
# a = m**2 -n**2
# b = 2*n*m
# c = m**2+n**2
def pythagorian3():
    for m,n in filterPairs():
        a,b,c = m**2 -n**2, 2*n*m, m**2+n**2
        if a<5:
            yield((a,b,c))
        else:
            yield((b,a,c))

for a,b,c in pythagorian3():
    print(a,b,c)
    if b > 1000:
        break


# tpl = pairs()
# i = 0
# while i <= 100:
#     print(next(tpl))
#     i += 1

# tplFiltered = filterPairs()
# print(next(tplFiltered))


