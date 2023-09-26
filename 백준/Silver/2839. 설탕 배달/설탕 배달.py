N = int(input())

if N % 5 == 0:
    fiv = N // 5
    thr = 0
elif N % 5 == 1 and N >= 6:
    fiv = ( N // 5 ) - 1
    thr = 2
elif N % 5 == 2 and N >= 12:
    fiv = ( N // 5 ) - 2
    thr = 4
elif N % 5 == 3 and N >= 3:
    fiv = N // 5
    thr = 1
elif N % 5 == 4 and N >= 9:
    fiv = ( N // 5 ) - 1
    thr = 3

else:
    fiv = -1
    thr = 0

print(fiv + thr)
