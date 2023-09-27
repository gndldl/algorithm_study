import sys
import heapq
input = sys.stdin.readline

t = int(input())
a = []
for i in range(t):
    heapq.heappush(a, int(input()))
if len(a) == 1:
    print(0)
else:
    ans = 0
    while len(a) > 1:
        temp1 = heapq.heappop(a)
        temp2 = heapq.heappop(a)
        ans += temp1 + temp2
        heapq.heappush(a, temp1 + temp2)
    print(ans)