# Time Complexity: O(log n)
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''
        # Treat the columnNumber as if it is base26
        while columnNumber > 0:
            # chr() will convert the ascii code into a character
            # Since columns are indexed starting at 1
            res += chr((columnNumber - 1) % 26 + ord('A'))
            columnNumber = (columnNumber -1) // 26

        return res[::-1]
