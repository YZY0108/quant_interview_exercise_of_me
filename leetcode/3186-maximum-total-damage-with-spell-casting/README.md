# LeetCode 3186 - 施咒的最大总伤害

## 题目链接

- 来源：[力扣 LeetCode](https://leetcode.cn/problems/maximum-total-damage-with-spell-casting/description/)
- 题意：给定若干法术伤害值，选择伤害为 `x` 的法术后，不能再选择伤害为 `x - 2`、`x - 1`、`x + 1`、`x + 2` 的法术。问可以获得的最大总伤害。

## 思路

先用 `Counter` 统计每个伤害值出现的次数。对于同一个伤害值 `x`，如果决定使用它，就应该把所有 `x` 都一起使用，贡献为：

```text
x * cnt[x]
```

把所有不同的伤害值排序为 `a`。记 `dfs(i)` 表示只考虑 `a[0]` 到 `a[i]` 时的最大总伤害。

对于当前伤害 `x = a[i]`，有两种选择：

```text
不选 x：dfs(i - 1)
选 x：dfs(j - 1) + x * cnt[x]
```

其中 `j` 是第一个不会和 `x` 冲突的位置，也就是跳过所有满足 `a[j - 1] >= x - 2` 的伤害值。

所以状态转移为：

```text
dfs(i) = max(dfs(i - 1), dfs(j - 1) + x * cnt[x])
```

## 复杂度

设不同伤害值个数为 `m`。

- 时间复杂度：`O(m^2 + n)`。
- 空间复杂度：`O(m)`。

## 代码

```python
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        a = sorted(cnt)
        @cache  
        def dfs(i: int) -> int:
            if i < 0:
                return 0
            x = a[i]
            j = i
            while j and a[j - 1] >= x - 2:
                j -= 1
            return max(dfs(i - 1), dfs(j - 1) + x * cnt[x])

        return dfs(len(a) - 1)
```
