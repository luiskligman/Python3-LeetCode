# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1  # Create two pointers, l at start and r at end
        while l < r:  # Prevents cross over
            while l < r and not self.alphaNum(s[l]):  # If non-alphnumeric, skip to next index
                l += 1
            while l < r and not self.alphaNum(s[r]):  # If non-alphnumeric, skip to next index
                r -= 1

            if s[l].lower() != s[r].lower():  # Convert character at left and right pointer to lowercase, then check for equality
                return False
            # Current left and right pointers are equal, iterate left and right to check the next index
            l, r = l + 1, r - 1
        return True
        
    # Helper function to determine if a character is alphanumeric without using the built-in Python function .isalumn()
    def alphaNum(self, c):
        if (ord('A') <= ord(c) <= ord('Z') or 
              ord('a') <= ord(c) <= ord('z') or
              ord('0') <= ord(c) <= ord('9')):
            return True
        return False
