class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1count, s2count = [0] * 26, [0] * 26  # Create two empty lists to count character occurances
        for i in range(len(s1)):
            s1count[ord(s1[i]) - ord('a')] += 1
            s2count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            # compare each of the 26 char counts, we could have a permutation at this point
            matches += (1 if s1count[i] == s2count[i] else 0)

        # Have a sliding window l and r, add r to count and remove l from count
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True
            # check for full match each time

            # check if adding s2[r] creates a match
            index = ord(s2[r]) - ord('a')
            s2count[index] += 1
            if s1count[index] == s2count[index]:
                matches += 1
            elif s1count[index] + 1 == s2count[index]:
                matches -= 1

            # check if removing s2[l] creates a match
            index = ord(s2[l]) - ord('a')
            s2count[index] -= 1
            if s1count[index] == s2count[index]:
                matches += 1
            elif s1count[index] - 1 == s2count[index]:
                matches -= 1

            # iterate l each time due to properties of sliding window approach
            l += 1
        return matches == 26
