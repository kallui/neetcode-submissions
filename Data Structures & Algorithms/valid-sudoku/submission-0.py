class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #input:
        # [["1","2",".",".","3",".",".",".","."],
        # ["4",".",".","5",".",".",".",".","."],
        # [".","9","8",".",".",".",".",".","3"],
        # ["5",".",".",".","6",".",".",".","4"],
        # [".",".",".","8",".","3",".",".","5"],
        # ["7",".",".",".","2",".",".",".","6"],
        # [".",".",".",".",".",".","2",".","."],
        # [".",".",".","4","1","9",".",".","8"],
        # [".",".",".",".","8",".",".","7","9"]]
        # check column and rows using Set
        rowSets = [set() for _ in range(9)]
        colSets = [set() for _ in range(9)]

        # square sets:
        # [0, 1, 2]
        # [3, 4, 5]
        # [6, 7, 8]
        squareSets = [set() for _ in range(9)]

        for i, row in enumerate(board):
            for j, col in enumerate(board[i]):
                squareIndex = int(i/3) * 3 + int(j/3)
                if col in rowSets[i] or col in colSets[j] or col in squareSets[squareIndex]:
                    return False
                if col != '.':
                    rowSets[i].add(col)
                    colSets[j].add(col)
                    # check each 3x3 squares
                    # i = 0-8, j = 0-8
                    # (0,0) = 0, (4,0) = 3, (4,7) = 5
                    squareSets[squareIndex].add(col)
        
        return True


