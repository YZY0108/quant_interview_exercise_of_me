# LeetCode 740 - 删除并获得点数

## 题目链接

- 来源：[力扣 LeetCode](https://leetcode.cn/problems/delete-and-earn/description/)
- 题意：选择一个数 `x` 可以获得 `x` 的点数，同时会删除所有 `x - 1` 和 `x + 1`。问最多能获得多少点数。

## 思路

这题可以转化成打家劫舍。

先统计每个数值能贡献的总点数：

```text
coqs[x] += x
```

这样 `coqs[i]` 表示选择数字 `i` 时，一共可以得到多少点数。

由于选择 `i` 后不能再选择 `i - 1` 和 `i + 1`，这就等价于在数组 `coqs` 上做打家劫舍：相邻位置不能同时选。

代码中 `rob` 函数就是打家劫舍的记忆化搜索：

```text
dfs(i) = max(dfs(i - 1), nums[i] + dfs(i - 2))
```

最后对统计后的 `coqs` 调用 `rob` 即可。

## 复杂度

- 时间复杂度：`O(n + max(nums))`。
- 空间复杂度：`O(max(nums))`。

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
    def deleteAndEarn(self, nums: List[int]) -> int:
        coqs = [0] * (max(nums)+1)
        for x in nums:
            coqs[x] += x
        return self.rob(coqs)
```

