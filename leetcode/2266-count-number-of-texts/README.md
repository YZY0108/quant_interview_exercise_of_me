# LeetCode 2266 - 统计打字方案数

## 题目链接

- 来源：[力扣 LeetCode](https://leetcode.cn/problems/count-number-of-texts/description/)
- 题意：手机九宫格按键中，数字 `2` 到 `9` 分别对应若干字母。给定按键序列 `pressedKeys`，统计它可能表示多少种文本，答案对 `1_000_000_007` 取模。

## 思路

连续相同的数字可以独立计算方案数，最后把每一段的方案数相乘。

对于普通按键 `2,3,4,5,6,8`，每个按键最多连续按 `3` 次表示一个字母。长度为 `m` 的连续段，可以拆成若干个长度为 `1,2,3` 的块。

因此用 `f[m]` 表示普通按键连续 `m` 次的方案数：

```text
f[m] = f[m - 1] + f[m - 2] + f[m - 3]
```

对于按键 `7` 和 `9`，每个按键最多连续按 `4` 次表示一个字母。长度为 `m` 的连续段，可以拆成若干个长度为 `1,2,3,4` 的块。

因此用 `g[m]` 表示 `7` 或 `9` 连续 `m` 次的方案数：

```text
g[m] = g[m - 1] + g[m - 2] + g[m - 3] + g[m - 4]
```

代码先预处理 `f` 和 `g`，再用 `groupby` 把 `pressedKeys` 按连续相同字符分组。每一组根据字符是否为 `7` 或 `9` 选择 `g[m]` 或 `f[m]`，累乘得到答案。

## 复杂度

- 时间复杂度：`O(10^5 + n)`，预处理数组后扫描一遍字符串。
- 空间复杂度：`O(10^5)`，保存预处理数组。

## 代码

```python
MOD = 1_000_000_007
f = [1, 1, 2, 4]
g = [1, 1, 2, 4]
for _ in range(10 ** 5 - 3):  
    f.append((f[-1] + f[-2] + f[-3]) % MOD)
    g.append((g[-1] + g[-2] + g[-3] + g[-4]) % MOD)

class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        ans = 1
        for ch, s in groupby(pressedKeys):
            m = len(list(s))
            ans = ans * (g[m] if ch in "79" else f[m]) % MOD
        return ans
```
