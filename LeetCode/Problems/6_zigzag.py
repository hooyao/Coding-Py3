import sys


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        bt_count = numRows * 2 - 2
        result = ""

        for i in range(numRows):
            j = 0
            while i + j * bt_count < len(s):
                if i == 0 or i == numRows - 1:
                    result += s[i + j * bt_count]
                    j += 1
                else:
                    result += s[i + j * bt_count]
                    pos = i + j * bt_count + (numRows - 1 - i) * 2
                    if pos < len(s):
                        result += s[pos]
                    j += 1
        return result


def main(*args):
    solution = Solution()
    result = solution.convert("PAYPALISHIRING", 2)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
