# LeetCode 70 - 爬楼梯

## 题目链接

- 来源：[力扣 LeetCode](https://leetcode.cn/problems/climbing-stairs/)
- 题意：一共有 `n` 阶楼梯，每次可以爬 `1` 阶或 `2` 阶，问爬到第 `n` 阶一共有多少种不同方法。

## 思路

设 `dfs(i)` 表示爬到第 `i` 阶的方法数。

到达第 `i` 阶只有两种可能：

- 从第 `i - 1` 阶再爬 `1` 阶
- 从第 `i - 2` 阶再爬 `2` 阶

所以递推关系是：

```text
dfs(i) = dfs(i - 1) + dfs(i - 2)
```

边界条件：

```text
dfs(0) = 1
dfs(1) = 1
```

这里 `dfs(0) = 1` 可以理解为“不爬也是一种完成方式”，这样递推到 `dfs(2)` 时：

```text
dfs(2) = dfs(1) + dfs(0) = 2
```

直接递归会重复计算大量子问题，例如 `dfs(5)` 会多次算到 `dfs(3)`、`dfs(2)`。用 `@cache` 记忆化后，每个状态只计算一次。

## 复杂度

- 时间复杂度：`O(n)`，一共只会计算 `0` 到 `n` 这些状态。
- 空间复杂度：`O(n)`，记忆化缓存和递归调用栈都可能占用线性空间。

## 代码

```python
from functools import cache


class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dfs(i: int) -> int:
            if i <= 1:
                return 1
            return dfs(i - 1) + dfs(i - 2)

        return dfs(n)
```
