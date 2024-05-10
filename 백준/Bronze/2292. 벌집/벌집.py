n = int(input())

temp = 1
i = 1

while True:
    if n <= temp:
        break
    temp += i*6
    i += 1

print(i)