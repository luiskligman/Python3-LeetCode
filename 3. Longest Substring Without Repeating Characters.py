class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        l = 0  # Pointer to the left side of the window
        charSet = set()  # A set to store chars in the current window

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])  # Remove this value from our set
                l += 1  # Move the left pointer forward 
            charSet.add(s[r])  # Once we know s[r] is not in set, we add it
            maxLen = max(maxLen, r - l + 1)  # Compute max between maxLen or r - l + 1
                                             # r - l + 1 = #
                                             # 0 - 0 + 1 = 1
                                             # 3 - 2 + 1 = 2
        return maxLen
