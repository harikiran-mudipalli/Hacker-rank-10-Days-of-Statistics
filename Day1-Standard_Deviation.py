import math
N = int(input())
X = list(map(int,input().split(' ')))
mean = sum(X)/N
distance = 0
for i in range(0,N):
    distance+=(X[i]-mean)**2

variance = math.sqrt(distance/N)
print(round(variance,1))