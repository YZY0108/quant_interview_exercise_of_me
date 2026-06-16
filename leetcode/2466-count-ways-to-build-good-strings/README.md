# LeetCode 2466 - 统计构造好字符串的方案数

## 题目链接

- 来源：[力扣 LeetCode](https://leetcode.cn/problems/count-ways-to-build-good-strings/)
- 题意：每次可以向当前字符串末尾添加 `zero` 个字符 `0`，或者添加 `one` 个字符 `1`。问最终字符串长度在 `[low, high]` 范围内的构造方案数，答案对 `1_000_000_007` 取模。

## 思路

设 `dfs(i)` 表示构造出长度为 `i` 的字符串有多少种方案。

如果 `i < 0`，说明长度已经减过头，不是合法方案：

```text
dfs(i) = 0, i < 0
```

如果 `i = 0`，说明刚好构造完成，这是一种合法方案：

```text
dfs(0) = 1
```

对于一般的 `i`，最后一步只有两种可能：

- 最后添加了 `zero` 个 `0`，前面需要构造长度 `i - zero`
- 最后添加了 `one` 个 `1`，前面需要构造长度 `i - one`

所以状态转移为：

```text
dfs(i) = dfs(i - zero) + dfs(i - one)
```

每个状态都对 `MOD` 取模。

题目要求长度在 `[low, high]` 之间的所有方案数，因此最终答案是：

```text
sum(dfs(j) for j in range(low, high + 1))
```

使用 `@cache` 记忆化后，每个长度最多计算一次。

## 复杂度

- 时间复杂度：`O(high)`。
- 空间复杂度：`O(high)`，用于记忆化缓存和递归调用栈。

## 代码

```python
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 1_000_000_007
        @cache
        def dfs(i:int) -> int:
            if i < 0:
                return 0
            if i ==0:
                return 1
            return (dfs(i-zero)+dfs(i-one)) % MOD
        return sum(dfs(j) for j in range(low,high+1))%MOD
```
