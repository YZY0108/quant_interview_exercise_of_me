MOD = 1_000_000_007
class Solution:
    def countHousePlacements(self, n: int) -> int:
        @cache
        def dfs(i:int) -> int:
            if i == 1:
                return 2
            if i == 2:
                return 3
            return (dfs(i-1)%MOD) + (dfs(i-2)%MOD)
        return ((dfs(n)%MOD)*(dfs(n)%MOD)%MOD)
