def gcd(n1, n2):
    while n2 > 0:
        n1, n2 = n2, n1 % n2
    return n1

def lcm(n1, n2):
    return n1*n2 // gcd(n1, n2)

a, b = map(int, input().split())

print(gcd(a, b))
print(lcm(a, b))
