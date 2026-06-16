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

## 复杂度

- 时间复杂度：`O(n)`，每个下标最多计算一次。
- 空间复杂度：`O(n)`，记忆化缓存和递归调用栈都可能占用线性空间。

## 代码

```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def dfs(i :int) -> int:
            if i>=len(cost)-2:
                return cost[i]
            else:
                return min(cost[i]+dfs(i+1),cost[i]+dfs(i+2))
        return min(dfs(0),dfs(1))
```
