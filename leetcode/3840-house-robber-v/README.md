# LeetCode 3840 - 打家劫舍 V

## 题目链接

- 来源：[力扣 LeetCode](https://leetcode.cn/problems/house-robber-v/description/)
- 题意：给定两个数组 `nums` 和 `colors`。`nums[i]` 表示第 `i` 间房屋的钱数，`colors[i]` 表示第 `i` 间房屋的颜色。若两间相邻房屋颜色相同，则不能同时偷。问最多能偷到多少钱。

## 思路

设 `dfs(i, pre_color)` 表示处理到第 `i` 间房屋时，右侧相邻已选择房屋的颜色为 `pre_color` 时，最多能偷到的钱。

如果 `i < 0`，说明已经没有房屋可以考虑：

```text
dfs(i, pre_color) = 0
```

如果当前房屋颜色和右侧相邻已选择房屋颜色相同：

```text
pre_color == colors[i]
```

那么当前房屋不能偷，只能跳过当前房屋，继续考虑前一间。

否则，当前房屋可以偷，也可以不偷：

- 偷当前房屋：收益为 `nums[i] + dfs(i - 1, colors[i])`
- 不偷当前房屋：收益为 `dfs(i - 1, 100001)`

其中 `100001` 是一个哨兵值，表示右侧相邻位置没有已选择房屋的颜色限制。

最后从最后一间房屋开始递归：

```text
dfs(len(colors) - 1, 100001)
```

使用 `@cache` 后，状态会被记忆化。

## 复杂度

- 时间复杂度：`O(n)`。
- 空间复杂度：`O(n)`，用于记忆化缓存和递归调用栈。

## 代码

```python
class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        @cache
        def dfs(i:int,pre_color:int) -> int :
            if i < 0:
                return 0
            if pre_color == colors[i]:
                return dfs(i-1,100001)
            else:
                if i == 0:
                    return nums[0]
                if i == 1 :
                    return max(nums[1]+dfs(0,colors[1]),dfs(0,100001))
                return max(dfs(i-1,colors[i])+nums[i],dfs(i-1,100001))
        return dfs(len(colors)-1,100001)
```

