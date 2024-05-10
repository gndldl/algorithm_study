a = set([(i+1) for i in range(30)])
b = []
for _ in range(28):
    b.append(int(input()))
    
c = list(set(a)-set(b))
c.sort()

print(c[0])
print(c[1])