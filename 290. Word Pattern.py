# Time Complexity: O(n)
# Space Complexity: O(2n) -> O(n)
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        strings = s.split(' ')

        # Create a two way mapping
        p_to_s = {}
        s_to_p = {}

        if len(pattern) != len(strings):
            return False

        # foo[a] = dog
        # p = b, s = dog
        # if (b in foo $$$ ) false

        for p, s in zip(pattern, strings):
            if (p in p_to_s and p_to_s[p] != s or s in s_to_p and s_to_p[s] != p):
                return False
            p_to_s[p] = s
            s_to_p[s] = p

        return True
