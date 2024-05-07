arr = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

word = input()

ans = 0

for c in word:
    for i, corpus in enumerate(arr):
        if c in corpus:
            ans += (i+3)

print(ans)