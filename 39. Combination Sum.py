class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        
        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or i >= len(candidates):
                return
            
            # Add using candidate[i]
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])

            # Increment the candidate, but dont add anything
            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res
