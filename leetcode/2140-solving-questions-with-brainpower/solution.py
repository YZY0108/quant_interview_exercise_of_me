class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def dfs(i: int) -> int:
            if i >= len(questions):
                return 0
            return max(dfs(i + 1), dfs(i + questions[i][1] + 1) + questions[i][0])
        return dfs(0)
