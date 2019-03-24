import sys


class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        left = 0
        right = len(arr) - 1
        pos = 0
        if x < arr[0]:
            return arr[0:k]
        elif x > arr[-1]:
            return arr[-k:]
        else:
            while left <= right:
                mid = (left + right) / 2
                start = int(mid)
                end = start + 1 if mid - start > 0.1 else start
                if x < arr[start]:
                    right = start
                elif arr[end] < x:
                    left = end
                elif arr[start] < x < arr[end]:
                    pos = mid
                    break
                elif arr[start] == x:
                    pos = start
                    break
                elif arr[end] == x:
                    pos = end
                    break
            return self.expend(arr, pos, x, k)

    def expend(self, arr, center, x, width):
        start = int(center)
        end = start + 1 if center - start > 0.1 else start
        result = []
        max_diff = arr[-1] - arr[0]
        while len(result) < width:
            if start < 0:
                diff1 = max_diff + 1
            else:
                diff1 = x - arr[start]
            if end >= len(arr):
                diff2 = max_diff + 1
            else:
                diff2 = arr[end] - x
            if start == end:
                result = [arr[start]]
                start = start - 1
                end = end + 1
            elif diff1 <= diff2:
                result.insert(0, arr[start])
                start = start - 1
            else:
                result.append(arr[end])
                end = end + 1
        return result


def main(*args):
    result = Solution().findClosestElements([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], 3, 3)
    # result = Solution().expend([1, 2, 4, 6, 7], 1.5, 3, 3)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
