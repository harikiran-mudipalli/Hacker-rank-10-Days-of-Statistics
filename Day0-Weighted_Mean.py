size = int(input())
array = list(map(int,input().split()))
weights = list(map(int, input().split()))
ans = []
a = 0
for i in range(size):
    a = array[i]*weights[i]
    ans.append(a)
print(round(sum(ans)/sum(weights),1))