charge = 1000 - int(input())
count = 0
coin = [500, 100, 50, 10, 5, 1]
for i in coin:
    count += charge // i
    charge %= i
print(count)