import sys
def exgcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = exgcd(b, a % b)
    return g, y, x - (a // b) * y
def crt(remainders, moduli):
    M = 1
    for m in moduli:
        M *= m
    ans = 0
    for a, m in zip(remainders, moduli):
        Mi = M // m
        _, inv, _ = exgcd(Mi, m) 
        ans = (ans + a * Mi * inv) % M
    return (ans % M + M) % M
data = sys.stdin.read().split()
idx = 0
n = int(data[idx]); idx += 1
mods, rems = [], []
for _ in range(n):
    mods.append(int(data[idx])); rems.append(int(data[idx+1])); idx += 2
print(crt(rems, mods))
