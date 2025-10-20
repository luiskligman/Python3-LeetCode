# Time Complexity: O(len(columnTitle))
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # # Reverse string to start with ls val
        # columnTitle = columnTitle[::-1]

        columnNumber = 0

        # # Convert chars into the numerical value
        # for pow, c in enumerate(columnTitle):
        #     columnNumber += (ord(c) - ord('A') + 1) * 26 ** pow

        # Method without reversing the string
        for c in columnTitle:
            # Multiplies previous values by 26, incrementing previous values by a factor of 26^1 each time
            columnNumber = columnNumber * 26 + (ord(c) - ord('A') + 1)
        return columnNumber
