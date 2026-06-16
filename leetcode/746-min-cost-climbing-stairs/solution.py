class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def dfs(i :int) -> int:
            if i>=len(cost)-2:
                return cost[i]
            else:
                return min(cost[i]+dfs(i+1),cost[i]+dfs(i+2))
        return min(dfs(0),dfs(1))
