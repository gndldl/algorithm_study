white = list(map(int, input().split()))
black = [1, 1, 2, 2, 2, 8]
answer = []

for w, b in zip(white, black):
    answer.append(b-w)

print(*answer)