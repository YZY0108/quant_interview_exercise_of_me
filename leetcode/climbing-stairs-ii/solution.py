class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        @cache
        def dfs(i:int) -> int:
            if i==0:
                return 0
            else:
                return min(dfs(j)+(i-j)*(i-j) for j in range(max(i-3,0), i))+costs[i-1]
        return dfs(n)
