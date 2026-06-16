# LeetCode - Climbing Stairs II

## 题目链接

- 来源：[力扣 LeetCode](https://leetcode.cn/problems/climbing-stairs-ii/description/)
- 题意：一共有 `n` 阶楼梯，数组 `costs` 中 `costs[i - 1]` 表示踩到第 `i` 阶需要支付的额外花费。每次最多可以向上爬 `3` 阶。如果从第 `j` 阶跳到第 `i` 阶，还需要支付跳跃代价 `(i - j)^2`。问到达第 `n` 阶的最小总代价。

## 思路

可以从你写的记忆化搜索来理解。

设 `dfs(i)` 表示到达第 `i` 阶的最小总代价。

如果 `i = 0`，表示还在地面，不需要支付任何费用：

```text
dfs(0) = 0
```

如果要到达第 `i` 阶，上一步只能来自：

```text
i - 1, i - 2, i - 3
```

也就是枚举：

```text
j in [max(i - 3, 0), i)
```

从第 `j` 阶跳到第 `i` 阶的总代价是：

```text
dfs(j) + (i - j)^2 + costs[i - 1]
```

所以状态转移为：

```text
dfs(i) = min(dfs(j) + (i - j)^2) + costs[i - 1]
```

其中：

```text
max(i - 3, 0) <= j < i
```

使用 `@cache` 记忆化后，每个状态只会计算一次。

## 复杂度

- 时间复杂度：`O(n)`，每个台阶只枚举最多 `3` 个前驱。
- 空间复杂度：`O(n)`，保存 `0` 到 `n` 的最小代价。

## 代码

```python
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        @cache
        def dfs(i:int) -> int:
            if i==0:
                return 0
            else:
                return min(dfs(j)+(i-j)*(i-j) for j in range(max(i-3,0), i))+costs[i-1]
        return dfs(n)
```
