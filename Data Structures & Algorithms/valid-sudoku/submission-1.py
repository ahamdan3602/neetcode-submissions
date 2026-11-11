class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Valid Rows
        for row in range(len(board)):
            if not self.isValidRow(board[row]):
                return False
        # Valid Cols    
        for col in range(len(board[0])):
            s = set()
            for row in range(len(board)):
                if not self.isValidCol(board[row][col], s):
                    return False
                if board[row][col].isdigit():
                    s.add(board[row][col])
        # Valid matrix
        for st_row in range(0, len(board), 3):
            for st_col in range(0, len(board[0]), 3):
                sub_matrix = [row[st_col : st_col + 3] for row in board[st_row : st_row + 3]]
                if not self.validMatrix(sub_matrix):
                    return False
        
        return True


    def validMatrix(self, matrix):
        s = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c].isdigit() and matrix[r][c] in s:
                    return False
                elif matrix[r][c].isdigit():
                    s.add(matrix[r][c])
                    
        return True

    def isValidRow(self, row):
        s = set()
        for num in row:
            if num.isdigit() and num in s:
                return False
            s.add(num)
        return True
    
    def isValidCol(self, val, s):
        if val in s:
            return False
        return True