class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_integer = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        sum = 0

        for i, v in enumerate(s):
            prev = roman_to_integer[s[i-1]]
            val = roman_to_integer[v]

            if i > 0 and prev < val:
                sum += val - prev
            # Check if there exists a next index in s, and check if next value is greater than curr
            elif i < (len(s) - 1) and val < roman_to_integer[s[i+1]]:
                continue
            else:
                sum += val
        return sum
                
