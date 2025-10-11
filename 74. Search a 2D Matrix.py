class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS - 1  # Top and bot are pointers to row ranges

        # Use binary search to determine what row the target will be in
        while top <= bot:
            midRow = (top + bot) // 2
            if target > matrix[midRow][-1]:
                top = midRow + 1
            elif target < matrix[midRow][0]:
                bot = midRow - 1
            else:
                # Top and bot should now pertain to what row the target is in
                break
        
        # Check to see if top pointer is greater than bottom pointer; this should never be the case,
        # This would mean the rows do not contain the target value
        if not (top <= bot):
            return False

        row = (top + bot) // 2  # Calculate the row the target exists in
        # At this point, this problem becomes a normal binary search of a list
        l, r = 0, COLS - 1  # Setup l and r pointers 
        while l <= r:  
            mid = (l + r) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        return False
