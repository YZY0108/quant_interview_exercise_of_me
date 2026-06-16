# 牛客 50569 - 曹冲养猪

## 题目链接

- 来源：[牛客网](https://ac.nowcoder.com/acm/problem/50569)
- 题意：给定 `n` 组同余条件。每组输入两个整数 `a_i, b_i`，表示猪的数量 `x` 满足 `x mod a_i = b_i`。题目保证所有 `a_i` 两两互质，要求输出满足所有条件的最小非负解。

## 思路

这是中国剩余定理。

所有模数两两互质，设：

```text
M = a_1 * a_2 * ... * a_n
```

对于每一组同余条件：

```text
x ≡ b_i (mod a_i)
```

令：

```text
M_i = M / a_i
```

因为 `a_i` 和 `M_i` 互质，所以存在 `M_i` 在模 `a_i` 意义下的逆元 `inv_i`：

```text
M_i * inv_i ≡ 1 (mod a_i)
```

这样：

```text
b_i * M_i * inv_i
```

这一项在模 `a_i` 下等于 `b_i`，在其他模数下等于 `0`。

把所有项相加即可得到一个满足所有同余条件的解：

```text
ans = sum(b_i * M_i * inv_i) mod M
```

代码中用扩展欧几里得 `exgcd` 求逆元。

## 复杂度

- 时间复杂度：`O(n log M)`，每组条件求一次逆元。
- 空间复杂度：`O(n)`，存储模数和余数。

## 代码

```python
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
```
