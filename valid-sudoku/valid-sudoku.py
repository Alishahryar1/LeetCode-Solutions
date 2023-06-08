class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            counts = {}
            for num in row:
                if num == '.':
                    continue
                counts[num] = False
            for num in row:
                if num == '.':
                    continue
                if counts[num]:
                    return False
                counts[num] = True
        
        for j in range(9):
            col = []
            for i in range(9):
                col.append(board[i][j])
            counts = {}
            for num in col:
                if num == '.':
                    continue
                counts[num] = False
            for num in col:
                if num == '.':
                    continue
                if counts[num]:
                    return False
                counts[num] = True

        for a in range(0, len(board), 3):
            for b in range(0, len(board), 3):
                box = []
                for row in range(a, a + 3):
                    box += board[row][b:b + 3]
                counts = {}
                for num in box:
                    if num == '.':
                        continue
                    counts[num] = False
                for num in box:
                    if num == '.':
                        continue
                    if counts[num]:
                        return False
                    counts[num] = True    

        return True