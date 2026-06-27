# LeetCode 198 - 打家劫舍

## 题目链接

- 来源：[力扣 LeetCode](https://leetcode.cn/problems/house-robber/)
- 题意：给定数组 `nums`，其中 `nums[i]` 表示第 `i` 间房屋的金额。不能偷相邻的两间房，问最多能偷到多少钱。

## 思路

设 `dfs(i)` 表示只考虑下标 `0` 到 `i` 的房屋时，能偷到的最大金额。

边界情况：

```text
dfs(0) = nums[0]
```

只考虑前两间房时，因为不能同时偷相邻房屋，所以只能取较大的那一间：

```text
dfs(1) = max(nums[0], nums[1])
```

对于第 `i` 间房，有两种选择：

- 不偷第 `i` 间，那么收益是 `dfs(i - 1)`
- 偷第 `i` 间，那么第 `i - 1` 间不能偷，收益是 `nums[i] + dfs(i - 2)`

所以状态转移为：

```text
dfs(i) = max(dfs(i - 1), nums[i] + dfs(i - 2))
```

使用 `@cache` 后，每个下标只会计算一次。

## 复杂度

- 时间复杂度：`O(n)`。
- 空间复杂度：`O(n)`，用于记忆化缓存和递归调用栈。

## 代码

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dfs(i:int) -> int:
            if i == 0:
                return nums[0]
            if i == 1 :
                return max(nums[0],nums[1])
            return max(dfs(i-1),nums[i]+dfs(i-2))
        return dfs(len(nums)-1)
```
