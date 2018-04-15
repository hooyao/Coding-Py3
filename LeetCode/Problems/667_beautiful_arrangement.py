import sys


class Solution:
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        result = []
        k_left = k
        i = 1
        j = n
        idx = 0
        while i <= j:
            if k == 1:
                result.append(i)
                i += 1
            else:
                if idx == 0:
                    result.append(i)
                    i += 1
                else:
                    if k_left > 1:
                        if idx % 2 == 1:
                            result.append(j)
                            j -= 1
                            k_left -= 1
                        else:
                            result.append(i)
                            i += 1
                            k_left -= 1
                    else:
                        last = result[-1]
                        if last > j:
                            result.append(j)
                            j -= 1
                        else:
                            result.append(i)
                            i += 1

                idx += 1
        return result


def main(*args):
    solution = Solution()
    print(solution.constructArray(6, 3))


if __name__ == '__main__':
    main(*sys.argv[1:])
