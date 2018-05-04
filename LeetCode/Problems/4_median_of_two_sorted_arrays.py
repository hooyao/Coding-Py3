import sys


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i, j = 0, 0
        merged = []
        while i < len(nums1) or j < len(nums2):
            if i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    merged.append(nums1[i])
                    i += 1
                else:
                    merged.append(nums2[j])
                    j += 1
            elif i < len(nums1):
                merged += nums1[i:]
                break
            else:
                merged += nums2[j:]
                break
        print(merged)
        if len(merged) % 2 == 0:
            return (merged[len(merged) // 2 - 1] + merged[len(merged) // 2]) / 2
        else:
            return merged[len(merged) // 2]


def main(*args):
    solution = Solution()
    result = solution.findMedianSortedArrays([1, 2, 3, 4, 5], [3, 4, 5, 6, 7, 8, 9, 10])
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
