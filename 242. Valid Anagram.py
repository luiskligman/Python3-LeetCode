class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Create two dictionaries, where the key will be the letter and the value will be the number of occurrences
        dictS, dictT = {}, {}

        # If the lengths of s & t do not match, by definition, it is impossible that these two strings can be anagrams
        if len(s) != len(t):
            return False  # Therefore, return false

        # Iterate through elements in the strings (only using len(s) because we know s & t have same length)
        for n in range(len(s)):
            # In dictS, key=[s[n]] -- being the letter in s at index n, increment by 1 since there is a new occurrence, but also add the existing value at the letter if it already exists, handle non-existing error by include ,0 in get()
            dictS[s[n]] = 1 + dictS.get(s[n], 0)
            # Same explanation for dictS
            dictT[t[n]] = 1 + dictT.get(t[n], 0)

        # for each character (key) in dictS, compare dictS[c] to dictT[c], if character does not exist in dictT, it will default to 0
        for c in dictS:
            if dictS[c] != dictT.get(c, 0):
                return False  # If key values are not equal, by definition, s and t cannot be anagrams

        # s and t are anagrams 
        return True
