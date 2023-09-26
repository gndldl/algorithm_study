n, k = map(int, input().split())
a = []
count = 0
for i in range(n):
    a.append(int(input()))
a.sort(reverse=True)

for j in range(n):
    if k >= a[j]:
        count += k // a[j]
        k %= a[j]
print(count)