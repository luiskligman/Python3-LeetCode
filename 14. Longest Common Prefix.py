class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        prefix = strs[0]  # Save the first string as prefix
        for i in range(1, len(strs)):  # Iterate through 2nd string till end
            while strs[i].find(prefix) != 0:  # Is prefix in strs[i] and does it start at first index
                prefix = prefix[0 : len(prefix) - 1]  # Decrement prefix, because entire prefix must be a substring in all other strings
                if prefix == "":  # If we decremented prefix all the way to nothing, then there was no common prefix
                    return ""
        return prefix
                    
