# LeetCode 213 - 打家劫舍 II

## 题目链接

- 来源：[力扣 LeetCode](https://leetcode.cn/problems/house-robber-ii/description/)
- 题意：房屋围成一圈，不能偷相邻房屋。第一个房屋和最后一个房屋也相邻，问最多能偷到多少钱。

## 思路

环形限制的关键是：第一个房屋和最后一个房屋不能同时偷。

可以分成两类情况：

- 不偷最后一间，只考虑 `0` 到 `n - 2`
- 偷最后一间，则不能偷第一间，也不能偷倒数第二间

代码中 `dfs(i)` 表示考虑从 `0` 到 `i` 的线性房屋时，能偷到的最大金额。

```text
dfs(i) = max(dfs(i - 1), nums[i] + dfs(i - 2))
```

`dfss(i)` 表示从第 `1` 间开始考虑到第 `i` 间时，能偷到的最大金额，用来处理“偷最后一间”时排除第 `0` 间的情况。

最终答案在两种情况里取最大值：

```text
max(dfs(len(nums) - 2), nums[-1] + dfss(len(nums) - 3))
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
            if i < 0:
                return 0
            if i == 0:
                return nums[0]
            if i == 1 :
                return max(nums[0],nums[1])
            return max(dfs(i-1),nums[i]+dfs(i-2))
        @cache
        def dfss(i:int) -> int:
            if i <= 0:
                return 0
            if i == 1 :
                return nums[1]
            if i == 2:
                return max(nums[1],nums[2])
            return max(dfss(i-1),nums[i]+dfss(i-2))
        return max(dfs(len(nums)-2),nums[-1]+dfss(len(nums)-3))
```

