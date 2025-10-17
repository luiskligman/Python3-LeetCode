class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_h = len(haystack)
        len_n = len(needle)

        # If len_h = 5, len_n = 3, range(3), there are three possible starting indexes that would be able to leave room for indexes pointing to the other characters of the needle
        for i in range(len_h - len_n + 1):
            # Try from this index, containing all other needed indexes to reach len_n if this string of length len_n is equal to the string needle
            if haystack[i:i+len_n] == needle:
                # If it is, then return the starting index i 
                return i
        return -1
