import random
import sys
import time


class Solution:

    def heapSort(self, arr):
        heap = self.heapify(arr)
        result = []
        for i in range(len(heap)):
            result.append(heap[0])
            self.swap(heap, 0, len(heap) - 1)
            heap = heap[0:-1]

            max_parent_idx = (len(heap) - 2) // 2
            max_idx = len(heap) - 1

            idx = 0
            while idx <= max_parent_idx:
                # reach last left
                if 2 * idx + 2 > max_idx:
                    left = heap[idx * 2 + 1]
                    if heap[idx] > left:
                        self.swap(heap, idx, idx * 2 + 1)
                    break
                else:
                    left = heap[idx * 2 + 1]
                    right = heap[idx * 2 + 2]
                    if heap[idx] > min(left, right):
                        if left < right:
                            self.swap(heap, idx, idx * 2 + 1)
                            idx = idx * 2 + 1
                        elif right < left:
                            self.swap(heap, idx, idx * 2 + 2)
                            idx = idx * 2 + 2
                        else:
                            break
                    else:
                        break
        #     print(heap)
        # print(heap)
        return result

    def heapify(self, arr):
        # build a heap
        heap = [0] + list(arr)
        arr_len = len(arr)
        for i in reversed(range(2, arr_len + 1)):
            # right node
            parent_idx = i // 2
            parent = heap[parent_idx]
            if heap[i] < parent:
                self.swap(heap, i, parent_idx)
                j = i
                max_idx = len(heap) - 1
                max_parent_idx = max_idx // 2
                while j <= max_parent_idx:
                    # only has left
                    if 2 * j + 1 > max_idx:
                        if heap[2 * j] < heap[j]:
                            self.swap(heap, 2 * j, j)
                        break
                    else:
                        left = heap[2 * j]
                        right = heap[2 * j + 1]
                        if left < right:
                            if heap[j] > left:
                                self.swap(heap, 2 * j, j)
                                j = j * 2
                            else:
                                break
                        else:
                            if heap[j] > right:
                                self.swap(heap, 2 * j + 1, j)
                                j = j * 2 + 1
                            else:
                                break
        return heap[1:]

    def swap(self, heap, i, j):
        tmp = heap[i]
        heap[i] = heap[j]
        heap[j] = tmp

    def validate_heap(self, heap):
        max_parent_idx = (len(heap) - 2) // 2
        max_idx = len(heap) - 1

        for i in range(0, max_parent_idx + 1):
            if 2 * i + 2 <= max_idx:
                if heap[i] > min(heap[2 * i + 1], heap[2 * i + 2]):
                    return False
            elif 2 * i + 1 <= max_idx:
                if heap[i] > heap[2 * i + 1]:
                    return False
        return True


def main(*args):
    solution = Solution()
    # for i in range(100):
    #     arr = random.sample(range(10000), 5000)
    #     start = time.time()
    #     result = solution.heapify(arr)
    #     end = time.time()
    #     # print(end - start)
    #     if not solution.validate_heap(result):
    #         print(arr)
    #         print(result)
    #         break
    # solution = Solution()
    # arr = random.sample(range(20), 8)
    # print(arr)
    # result = solution.heapSort([7, 9, 13, 3, 0, 16, 18, 17])
    # print(result)
    for i in range(100):
        arr = random.sample(range(30000), 10000)
        start = time.time()
        result = solution.heapSort(arr)
        end = time.time()
        print(end - start)
        sorted_arr = sorted(arr)
        if result != sorted_arr:
            print("error")
            break


solution = Solution()

if __name__ == '__main__':
    main(*sys.argv[1:])
