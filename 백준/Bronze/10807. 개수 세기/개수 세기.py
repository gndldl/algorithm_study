n = int(input())

arr = list(map(int, input().split()))
target = int(input())

answer = arr.count(target)
print(answer)