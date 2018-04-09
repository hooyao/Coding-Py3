import random
import sys
import time


class Solution:

    def quickSort_Rec(self, arr):
        self.sort_rec(arr, 0, len(arr) - 1)
        return arr

    def sort_rec(self, arr, start, end):
        if end - start > 0:
            pivot = arr[start]
            left = start + 1
            right = end
            while right - left >= 0:
                if arr[left] >= pivot >= arr[right]:
                    self.swap(arr, left, right)
                    left += 1
                    right -= 1
                elif arr[left] <= pivot:
                    left += 1
                elif arr[right] >= pivot:
                    right -= 1
            self.swap(arr, start, right)
            self.sort_rec(arr, start, right - 1)
            self.sort_rec(arr, right + 1, end)

    def quickSort_Iter(self, arr):
        init_start = 0
        init_end = len(arr) - 1
        todo = [[init_start, init_end]]
        while len(todo) > 0:
            new_todo = []
            for ele in todo:
                start = ele[0]
                end = ele[1]
                pivot = arr[start]
                left = start + 1
                right = end
                while right - left >= 0:
                    if arr[left] >= pivot >= arr[right]:
                        self.swap(arr, left, right)
                        left += 1
                        right -= 1
                    elif arr[left] <= pivot:
                        left += 1
                    elif arr[right] >= pivot:
                        right -= 1
                self.swap(arr, start, right)
                if right - 1 - start > 0:
                    new_todo.append([start, right - 1])
                if end - right - 1 > 0:
                    new_todo.append([right + 1, end])
            todo = new_todo
        return arr

    def swap(self, arr, a1, a2):
        tmp = arr[a1]
        arr[a1] = arr[a2]
        arr[a2] = tmp


def main(*args):
    solution = Solution()
    # print(result)
    #arr = random.sample(range(10), 10)
    for i in range(1000):
        arr = list(random.randrange(2000) for i in range(1000))
        start = time.time()
        result = solution.quickSort_Iter(arr)
        end = time.time()
        #print(end - start)
        #print(arr)
        sorted_arr = sorted(arr)
        if result != sorted_arr:
            print(arr)
            print("error")
            break


if __name__ == '__main__':
    main(*sys.argv[1:])
