# LeetCode 377 - 组合总和 IV

## 题目链接

- 来源：[力扣 LeetCode](https://leetcode.cn/problems/combination-sum-iv/description/)
- 题意：给定一个由不同正整数组成的数组 `nums` 和一个目标整数 `target`，统计可以凑成 `target` 的组合个数。不同顺序的序列视为不同组合。

## 思路

设 `dfs(i)` 表示凑出总和 `i` 的方案数。

如果 `i < 0`，说明当前选择已经超过目标值，不构成合法方案：

```text
dfs(i) = 0, i < 0
```

如果 `i = 0`，说明刚好凑出目标值，这是一种合法方案：

```text
dfs(0) = 1
```

对于一般的 `i`，最后一步可以选择 `nums` 中任意一个数 `nums[j]`。选了它之后，前面需要凑出的值就是 `i - nums[j]`，所以：

```text
dfs(i) = sum(dfs(i - nums[j]))
```

其中：

```text
0 <= j < len(nums)
```

因为题目把不同顺序视为不同组合，所以这里按“最后一步选哪个数”来转移，会自然统计出不同排列顺序。

使用 `@cache` 记忆化后，每个 `i` 只会计算一次。

## 复杂度

- 时间复杂度：`O(target * len(nums))`。
- 空间复杂度：`O(target)`，用于记忆化缓存和递归调用栈。

## 代码

```python
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i:int) -> int:
            if i<0:
                return 0
            if i==0:
                return 1
            return sum(dfs(i-nums[j]) for j in range(len(nums)))
        return dfs(target)
```
