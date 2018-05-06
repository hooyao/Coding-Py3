import sys


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if len(board) != 9 or len(board[0]) != 9:
            raise Exception()
        # test block
        for i in range(3):
            for j in range(3):
                block = [row[j * 3:j * 3 + 3] for row in board[i * 3:i * 3 + 3]]
                if not self.test_block(block):
                    return False
        # test row
        for i in range(9):
            row = board[i]
            if not self.test_arr(row):
                return False
        # test col
        for i in range(9):
            col = [row[i] for row in board]
            if not self.test_arr(col):
                return False
        return True

    def test_block(self, block):
        if len(block) != 3 or len(block[0]) != 3:
            raise Exception()
        stats = [0] * 10
        for i in range(3):
            for j in range(3):
                if block[i][j] != ".":
                    val = int(block[i][j])
                    if stats[val] > 0:
                        return False
                    else:
                        stats[val] = 1
        return True

    def test_arr(self, arr):
        if len(arr) != 9:
            raise Exception()
        stats = [0] * 10
        for i in range(9):
            if arr[i] != ".":
                val = int(arr[i])
                if stats[val] > 0:
                    return False
                else:
                    stats[val] = 1
        return True


def main(*args):
    mat1 = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    mat2 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    solution = Solution()
    result = solution.isValidSudoku(mat2)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
