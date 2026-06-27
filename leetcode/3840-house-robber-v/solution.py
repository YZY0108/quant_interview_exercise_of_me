class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        @cache
        def dfs(i:int,pre_color:int) -> int :
            if i < 0:
                return 0
            if pre_color == colors[i]:
                return dfs(i-1,100001)
            else:
                if i == 0:
                    return nums[0]
                if i == 1 :
                    return max(nums[1]+dfs(0,colors[1]),dfs(0,100001))
                return max(dfs(i-1,colors[i])+nums[i],dfs(i-1,100001))
        return dfs(len(colors)-1,100001)
