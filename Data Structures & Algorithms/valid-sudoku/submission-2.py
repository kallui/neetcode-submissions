class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSets = [set() for _ in range(9)]
        colSets = [set() for _ in range(9)]
        squareSets = [set() for _ in range(9)]

        for i, row in enumerate(board):
            for j, value in enumerate(board[i]):
                squareIndex = int(i/3)*3 + int(j/3)
                if value in rowSets[i] or value in colSets[j] or value in squareSets[squareIndex]:
                    return False
                if value != '.':
                    rowSets[i].add(value)
                    colSets[j].add(value)
                    squareSets[squareIndex].add(value)

        return True

