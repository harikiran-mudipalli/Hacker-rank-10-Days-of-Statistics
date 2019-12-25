N = int(input())
X = list(map(int, input().split(' ')))
F = list(map(int, input().split(' ')))
S = []
for i in range(0,N):
    S+=[X[i]]*F[i]
for i in range(0,len(S)):
    for j in range(i+1,len(S)):
        if S[i]>S[j]:
            temp = S[i]
            S[i] = S[j]
            S[j] = temp
def q(x):
    if x%2==0:
        return (S[int(x/2)-1]+S[int(x/2)])/2
    else:
        return S[int(x/2)]
def q3(x):
    if x%2==0:
        return (S[(len(S)-int(x/2)-1)]+S[(len(S)-int(x/2))])/2
    else:
        return S[(len(S)-int(x/2)-1)]
k=int(len(S)/2)
Q1=q(k) 
Q3=q3(k)
print(float(Q3-Q1))
