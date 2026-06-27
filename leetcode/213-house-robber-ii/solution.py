class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dfs(i:int) -> int:
            if i < 0:
                return 0
            if i == 0:
                return nums[0]
            if i == 1 :
                return max(nums[0],nums[1])
            return max(dfs(i-1),nums[i]+dfs(i-2))
        @cache
        def dfss(i:int) -> int:
            if i <= 0:
                return 0
            if i == 1 :
                return nums[1]
            if i == 2:
                return max(nums[1],nums[2])
            return max(dfss(i-1),nums[i]+dfss(i-2))
        return max(dfs(len(nums)-2),nums[-1]+dfss(len(nums)-3))
