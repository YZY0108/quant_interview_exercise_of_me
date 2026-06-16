from typing import List


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            best = float("inf")
            for j in range(max(i - 3, 0), i):
                best = min(best, dp[j] + (i - j) * (i - j))
            dp[i] = best + costs[i - 1]

        return dp[n]
