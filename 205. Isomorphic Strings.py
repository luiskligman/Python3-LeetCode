# Time Complexity: O(n)
# Space Complexity: O(2n) -> O(n)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Map two mappings, as it should properly make from s to t and then t to s
        mapST, mapTS = {}, {}
        for a, b in zip(s, t):
            if (a in mapST and mapST[a] != b or b in mapTS and mapTS[b] != a):
                return False
            mapST[a] = b
            mapTS[b] = a
        return True
