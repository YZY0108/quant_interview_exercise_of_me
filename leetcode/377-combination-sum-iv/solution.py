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
