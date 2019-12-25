n = int(input())
a = list(map(int,input().split(' ')))
for i in range(0,n):
    for j in range(i+1,n):
        if a[i]>a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
def q(x):
    if x%2==0:
        return (a[int(x/2)-1]+a[int(x/2)])/2
    else:
        return a[int(x/2)]

def q3(x):
    if x%2==0:
        return (a[(n-int(x/2)-1)]+a[(n-int(x/2))])/2
    else:
        return a[(n-int(x/2)-1)]
Q2 = q(n)
k=int(n/2)
Q1=q(k) 
Q3=q3(k)
print(int(Q1))
print(int(Q2))
print(int(Q3))