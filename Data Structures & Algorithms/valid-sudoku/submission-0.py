class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        num_rows = len(board)
        num_cols = len(board[0])

        for r in range(num_rows):
            col_mp = {}
            for c in range(num_cols):
                val = board[r][c]
                if val.isdigit() and val in col_mp:
                    return False
                else:
                    col_mp[val] = 1
        
        for c in range(num_cols):
            row_mp = {}
            for r in range(num_rows):
                val = board[r][c]
                if val.isdigit() and val in row_mp:
                    return False
                else:
                    row_mp[val] = 1

        for r_start in range(0, 9, 3):
            for c_start in range(0, 9, 3):
                box_mp = {}
                
                # Traverse the 3x3 grid starting at (r_start, c_start)
                for i in range(3):
                    for j in range(3):
                        val = board[r_start + i][c_start + j]
                        if val.isdigit():
                            if val in box_mp:
                                return False
                            else:
                                box_mp[val] = 1
                
      
        return True
