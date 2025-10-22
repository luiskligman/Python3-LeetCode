class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # DFS can be used as a way to explore all configurations, paths, or combinations. 
        # Contrary to my previous thought process of only using it to traverse pre-existing trees.
        res = []
        subset = []
        def dfs(index):
            if index >= len(nums):
                # We have handled all cases
                res.append(subset.copy())
                return
            
            # Handle the case where we add next element in nums
            subset.append(nums[index])
            dfs(index + 1)

            # Handle the case where we dont add the next element
            subset.pop()  # Pop the element we just added in prev step
            dfs(index + 1)
            
            return res

        return dfs(0)
