class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use defaultdiction with the default value of a list
        res = defaultdict(list)  # mapping charCount to List of Anagrams

        for s in strs:  
            # Create an empty array for each string to count number of letters
            count = [0] * 26  # a ... z

            for c in s:
                # compare ascii values of variable c to reference 'a', then += 1 to that index, ie a = 0, b = 1, z = 25
                count[ord(c) - ord('a')] += 1

            # count is a list, but list cannot be keys so change it to a tuple
            res[tuple(count)].append(s)

        return list(res.values())
