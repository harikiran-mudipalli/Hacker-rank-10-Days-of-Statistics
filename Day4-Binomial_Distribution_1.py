""" Task:
The ratio of boys to girls for babies born in Russia is . If there is  child born per birth, what proportion of Russian families with exactly  children will have at least  boys?
Write a program to compute the answer using the above parameters. Then print your result, rounded to a scale of  decimal places (i.e.,  format).
"""
P,Q = map(float,input().split(' '))
total = P+Q
N = 6
atleast = 3
Sum = 0
def combinations(n,r):
    n1=n
    r1=r
    for j in range(1,r):
        n1*=(n-j)
        r1*=(r-j)
    return n1/r1
def pos(p,x):
    return pow(p,x)
def neg(q,n,x):
    return pow(q,(n-x))
for i in range(atleast,N+1):
    Sum+=combinations(N,i)*pos(P/total,i)*neg(Q/total,N,i)
print(round(Sum,3))
