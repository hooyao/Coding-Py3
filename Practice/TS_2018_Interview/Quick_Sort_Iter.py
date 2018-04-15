import random
import sys


class Solution:

    def quickSort(self, arr):
        todo = [[0, len(arr) - 1]]
        while len(todo) > 0:
            new_toto = []
            for ele in todo:
                start, end = ele[0], ele[1]
                if end > start:
                    partial_sorted, pivot_idx = self.partition(arr, ele[0], ele[1])
                    new_toto.append([start, pivot_idx - 1])
                    new_toto.append([pivot_idx + 1, end])
            todo = new_toto
        return arr

    def partition(self, arr, start, end):
        pivot = arr[end]
        left, right = start, end - 1
        while right - left >= 0:
            if arr[left] >= pivot >= arr[right]:
                self.swap(arr, left, right)
                left += 1
                right -= 1
            elif arr[left] <= pivot:
                left += 1
            elif arr[right] >= pivot:
                right -= 1
        self.swap(arr, left, end)
        return arr, left

    def swap(self, arr, i, j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp


def main(*args):
    solution = Solution()
    # arr = [0, 1, 12, 17, 10, 1, 10, 15, 13, 11]
    # solution.quickSort(arr)
    # print(arr)
    for i in range(10000):
        arr = list(random.randrange(200) for i in range(100))
        org_arr = list(arr)
        result = solution.quickSort(arr)
        sorted_arr = sorted(org_arr)
        if result != sorted_arr:
            print(org_arr)
            print(arr)
            print("error")
            break


if __name__ == '__main__':
    main(*sys.argv[1:])
