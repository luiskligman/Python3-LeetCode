# Time Complextiy O(n)
# Space Complexity O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''  # Create a new empty string
        for c in s:  # Iterate through each char in string
            if c.isalnum():  # Filter out non alphernumic characters
                newStr += c.lower()  # Append character to newStr while also making it lowercase
        return newStr == newStr[::-1]  # Check if newStr is equal to newStr backwards
