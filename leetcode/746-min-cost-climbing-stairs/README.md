# LeetCode 746 - 使用最小花费爬楼梯

## 题目链接

- 来源：[力扣 LeetCode](https://leetcode.cn/problems/min-cost-climbing-stairs/)
- 题意：给定数组 `cost`，其中 `cost[i]` 表示踩到第 `i` 阶楼梯需要支付的花费。每次可以爬 `1` 阶或 `2` 阶，可以从第 `0` 阶或第 `1` 阶开始，问到达楼梯顶部的最小花费。

## 思路

可以从递归角度理解：设 `dfs(i)` 表示从第 `i` 阶开始爬到楼梯顶部，至少需要支付多少花费。

站到第 `i` 阶时，需要先支付 `cost[i]`，然后有两种选择：

- 爬到第 `i + 1` 阶
- 爬到第 `i + 2` 阶

所以状态转移是：

```text
dfs(i) = cost[i] + min(dfs(i + 1), dfs(i + 2))
```

当 `i` 已经是最后两阶之一时，踩上这一阶后可以直接到达顶部，所以：

```text
dfs(i) = cost[i], i >= len(cost) - 2
```

题目允许从第 `0` 阶或第 `1` 阶开始，因此最终答案是：

```text
min(dfs(0), dfs(1))
```

直接递归会重复计算很多状态。使用 `@cache` 记忆化后，每个下标只会计算一次。

不过这题 `cost.length` 最大可以到 `1000`，Python 递归写法在边界数据上可能触发递归深度限制。最终代码使用等价的自底向上动态规划。

设 `dp[i]` 表示到达第 `i` 阶并支付 `cost[i]` 后的最小花费，则：

```text
dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
```

最后可以从最后一阶或倒数第二阶直接到达顶部，所以答案是：

```text
min(dp[n - 1], dp[n - 2])
```

代码里只保留前两个状态，把空间优化到 `O(1)`。

## 复杂度

- 时间复杂度：`O(n)`，每个下标最多计算一次。
- 空间复杂度：`O(1)`，只保存最近两个状态。

## 代码

```python
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2 = cost[0]
        prev1 = cost[1]

        for i in range(2, len(cost)):
            curr = cost[i] + min(prev1, prev2)
            prev2, prev1 = prev1, curr

        return min(prev1, prev2)
```
