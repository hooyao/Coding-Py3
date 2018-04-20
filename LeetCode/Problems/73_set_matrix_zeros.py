import sys


class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        cols = set()
        rows = set()
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    cols.add(j)
                    rows.add(i)

        for i in rows:
            matrix[i][:] = [0] * m
        for j in cols:
            for k in range(n):
                matrix[k][j] = 0


def main(*args):
    solution = Solution()
    val = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    solution.setZeroes(val)
    print(val)


if __name__ == '__main__':
    main(*sys.argv[1:])
