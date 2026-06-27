# LeetCode 2140 - 解决智力问题

## 题目链接

- 来源：[力扣 LeetCode](https://leetcode.cn/problems/solving-questions-with-brainpower/description/)
- 题意：每道题有得分和需要跳过的题数。做第 `i` 题可以获得 `questions[i][0]` 分，但之后必须跳过 `questions[i][1]` 道题；也可以不做当前题。问最多能获得多少分。

## 思路

这是一个从当前位置向后决策的动态规划。

定义 `dfs(i)` 表示从第 `i` 道题开始，最多可以获得多少分。

当 `i` 已经超过题目数量时，没有题可做，返回 `0`。

对于第 `i` 道题，有两种选择：

```text
不做：dfs(i + 1)
做：questions[i][0] + dfs(i + questions[i][1] + 1)
```

取两者最大值即可：

```text
dfs(i) = max(dfs(i + 1), dfs(i + questions[i][1] + 1) + questions[i][0])
```

最终答案是 `dfs(0)`。

## 复杂度

- 时间复杂度：`O(n)`。
- 空间复杂度：`O(n)`。

## 代码

```python
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def dfs(i: int) -> int:
            if i >= len(questions):
                return 0
            return max(dfs(i + 1), dfs(i + questions[i][1] + 1) + questions[i][0])
        return dfs(0)
```
