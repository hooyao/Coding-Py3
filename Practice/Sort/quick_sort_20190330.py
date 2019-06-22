import random
import sys
import time


class Solution:

    def recursive_quick_sort(self, unsorted_data):
        self.partition(unsorted_data, 0, len(unsorted_data) - 1)
        return unsorted_data

    def partition(self, data, start, end):
        if end - start > 0:
            pivot = data[end]
            left = start
            right = end - 1
            while right - left >= 0:
                if data[left] >= pivot >= data[right]:
                    data[left], data[right] = data[right], data[left]
                    left += 1
                    right -= 1
                elif data[left] <= pivot:
                    left += 1
                elif data[right] >= pivot:
                    right -= 1
            data[end], data[right + 1] = data[right + 1], data[end]
            self.partition(data, start, right)
            self.partition(data, right + 2, end)

    def iter_quick_sort(self, arr):
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
                        arr[left], arr[right] = arr[right], arr[left]
                        left += 1
                        right -= 1
                    elif arr[left] <= pivot:
                        left += 1
                    elif arr[right] >= pivot:
                        right -= 1
                arr[start], arr[right] = arr[right], arr[start]
                if right - 1 - start > 0:
                    new_todo.append([start, right - 1])
                if end - right - 1 > 0:
                    new_todo.append([right + 1, end])
            todo = new_todo
        return arr

    def find_n_th_number(self, unsorted_data, n):
        return self.recursive_find(unsorted_data, 0, len(unsorted_data) - 1, n)

    def recursive_find(self, data, start, end, n):
        if start < end:
            pivot = data[end]
            left = start
            right = end - 1
            while right - left >= 0:
                if data[left] >= pivot >= data[right]:
                    data[left], data[right] = data[right], data[left]
                    left += 1
                    right -= 1
                elif data[left] <= pivot:
                    left += 1
                elif data[right] >= pivot:
                    right -= 1
            data[end], data[right + 1] = data[right + 1], data[end]
            pivot_pos = right + 1
            if pivot_pos > n:
                return self.recursive_find(data, start, pivot_pos - 1, n)
            elif pivot_pos < n:
                return self.recursive_find(data, pivot_pos + 1, end, n)
            else:
                return data[pivot_pos]
        return data[start]


def main(*args):
    solution = Solution()
    # print(result)
    # arr = random.sample(range(10), 10)
    # test_data_list = []
    # expected_data_list = []
    # for i in range(1000):
    #     test_data = list(random.randrange(10000) for i in range(random.randrange(400, 600)))
    #     test_data_list.append(test_data)
    #     expected_data_list.append(list(sorted(test_data)))
    # t = time.process_time()
    # for idx in range(len(test_data_list)):
    #     test_data = test_data_list[idx]
    #     expected_data = expected_data_list[idx]
    #     solution.iter_quick_sort(test_data)
    #     if test_data != expected_data:
    #         print(test_data)
    #         print(expected_data)
    #         print("error")
    #         break
    # eclapsed = time.process_time() - t
    # print(eclapsed)

    test_data_list = []
    expected_data_list = []
    for i in range(1000):
        test_data = list(random.randrange(10000) for i in range(random.randrange(400, 600)))
        test_data_list.append(test_data)
        n = random.randrange(len(test_data))
        expected_data_list.append([n, list(sorted(test_data))[n]])
    t = time.process_time()
    for idx in range(len(test_data_list)):
        test_data = test_data_list[idx]
        expected_data = expected_data_list[idx]
        result = solution.find_n_th_number(test_data, expected_data[0])
        if result != expected_data[1]:
            print(result)
            print(expected_data[1])
            print("error")
            break
    eclapsed = time.process_time() - t
    print(eclapsed)


if __name__ == '__main__':
    main(*sys.argv[1:])
