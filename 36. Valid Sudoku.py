class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)  # key is the column number and the value is another set of all values in this column
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r / 3, c / 3)  KEY IS A TUPLE

        # hard-coding range(9) since Sudoku boards must be 9 by 9
        for r in range(9):
            for c in range(9):
                # if board[r][c] is blank, continue
                if board[r][c] == '.':
                    continue
                # check if board[r][c] value is in any of the hashsets, if it already is, then the board must be invalid
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3, c // 3)] ):
                    return False
                # since value is not in any hashset, add it for future checking
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[ (r // 3, c // 3)].add(board[r][c])
        return True        
