import random
import sys


class Solution:

    def merge_sort_rec(self, arr):
        left_len = len(arr) // 2
        right_len = len(arr) - left_len
        self.merge_rec(arr, 0, left_len, right_len)
        return arr

    def merge_rec(self, arr, left, left_len, right_len):
        if left_len == 0 or right_len == 0:
            return arr[left:left + left_len + right_len]
        right_idx = left + left_len
        left_left_len = left_len // 2
        left_right_len = left_len - left_left_len
        sorted_left = self.merge_rec(arr, left, left_left_len, left_right_len)
        
        right_left_len = right_len // 2
        right_right_len = right_len - right_left_len
        sorted_right = self.merge_rec(arr, right_idx, right_left_len, right_right_len)

        sorted_arr = [0] * (left_len + right_len)
        idx = 0
        left_idx = 0
        right_idx = 0
        while idx < len(sorted_arr):
            if left_idx <= len(sorted_left) - 1 and right_idx <= len(sorted_right) - 1:
                if sorted_left[left_idx] <= sorted_right[right_idx]:
                    sorted_arr[idx] = sorted_left[left_idx]
                    left_idx += 1
                else:
                    sorted_arr[idx] = sorted_right[right_idx]
                    right_idx += 1
            elif left_idx <= len(sorted_left) - 1:
                sorted_arr[idx] = sorted_left[left_idx]
                left_idx += 1
            else:
                sorted_arr[idx] = sorted_right[right_idx]
                right_idx += 1
            idx += 1
        return sorted_arr

    def merge_sort_iter(self, arr):
        pass

    def swap(self, arr, a1, a2):
        tmp = arr[a1]
        arr[a1] = arr[a2]
        arr[a2] = tmp


def main(*args):
    solution = Solution()
    # print(result)
    # arr = random.sample(range(10), 10)
    for i in range(1000):
        arr = list(sorted(random.randrange(2000) for i in range(1234)))
        result = solution.merge_sort_rec(arr)
        sorted_arr = sorted(arr)
        if result != sorted_arr:
            print(arr)
            print(sorted_arr)
            print("error")
            break
    # result = solution.merge_rec([1,3,4,6,2,3,4,8],0,4,4)
    # print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
