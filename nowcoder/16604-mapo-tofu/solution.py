import sys
a = sys.stdin.read().split()
t = int(a[0])
i = 1
ans = []
for _ in range(t):
    n = int(a[i])
    i += 1
    k = a[i:i+n].count("0.500000")
    i += n
    ans.append(str((1 << n) - (1 << (n - k))))
print("\n".join(ans))
