n = int(input())
arr = []
for _ in range(n):
    a, b = input().split()
    arr.append([int(a), str(b)])
    
arr.sort(key=lambda x:x[0])

for info in arr:
    print(*info)
