# LeetCode 2320 - 统计放置房子的方式数

## 题目链接

- 来源：[力扣 LeetCode](https://leetcode.cn/problems/count-number-of-ways-to-place-houses/description/)
- 题意：街道两侧各有 `n` 个地块，可以选择在某些地块上建房子，但同一侧相邻地块不能同时建房。问两侧一共有多少种放置方式，答案对 `1_000_000_007` 取模。

## 思路

先只考虑街道一侧。

设 `dfs(i)` 表示一侧有 `i` 个地块时的合法放置方案数。

边界：

```text
dfs(1) = 2
dfs(2) = 3
```

对于第 `i` 个地块，有两种情况：

- 不放房子：前 `i - 1` 个地块任意合法放置，方案数为 `dfs(i - 1)`
- 放房子：第 `i - 1` 个地块不能放，前 `i - 2` 个地块任意合法放置，方案数为 `dfs(i - 2)`

所以：

```text
dfs(i) = dfs(i - 1) + dfs(i - 2)
```

左右两侧互相独立，因此总方案数是：

```text
dfs(n) * dfs(n)
```

使用 `@cache` 后，每个 `i` 只会计算一次。

## 复杂度

- 时间复杂度：`O(n)`。
- 空间复杂度：`O(n)`，用于记忆化缓存和递归调用栈。

## 代码

```python
MOD = 1_000_000_007
class Solution:
    def countHousePlacements(self, n: int) -> int:
        @cache
        def dfs(i:int) -> int:
            if i == 1:
                return 2
            if i == 2:
                return 3
            return (dfs(i-1)%MOD) + (dfs(i-2)%MOD)
        return ((dfs(n)%MOD)*(dfs(n)%MOD)%MOD)
```

