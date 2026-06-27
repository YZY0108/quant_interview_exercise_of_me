class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dfs(i:int) -> int:
            if i == 0:
                return nums[0]
            if i == 1 :
                return max(nums[0],nums[1])
            return max(dfs(i-1),nums[i]+dfs(i-2))
        return dfs(len(nums)-1)
    def deleteAndEarn(self, nums: List[int]) -> int:
        coqs = [0] * (max(nums)+1)
        for x in nums:
            coqs[x] += x
        return self.rob(coqs)
