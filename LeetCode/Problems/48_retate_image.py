import sys


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        edge_len = len(matrix[0])
        idx = 0
        while edge_len > 1:
            for i in range(idx, idx + edge_len - 1):
                self.rotate_4(matrix, idx, i)
            idx += 1
            edge_len -= 2

    def rotate_4(self, m, i, j):
        n = len(m[0])
        temp = m[i][j]
        m[i][j] = m[n - 1 - j][i]
        m[n - 1 - j][i] = m[n - 1 - i][n - 1 - j]
        m[n - 1 - i][n - 1 - j] = m[j][n - 1 - i]
        m[j][n - 1 - i] = temp


def main(*args):
    solution = Solution()
    a = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]
    solution.rotate(a)
    for ele in a:
        print(ele)


if __name__ == '__main__':
    main(*sys.argv[1:])
