import sys


class Activity:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return '[{},{}]'.format(self.start, self.end)

    def __repr__(self):
        return '[{},{}]'.format(self.start, self.end)

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end


class Solution:
    def max_compatible_set(self, activities):
        end_sorted = sorted(activities, key=lambda x: x.end)
        result = []
        for ele in end_sorted:
            if len(result) == 0:
                result.append(ele)
            else:
                if self.isCompatible(ele, result[-1]):
                    result.append(ele)
        return result

    def isCompatible(self, a1, a2):
        return a1.end < a2.start or a2.end < a1.start

    def max_compatible_set_within(self, activities, S, F):
        end_sorted = sorted(activities, key=lambda x: x.end)
        result = []
        for ele in end_sorted:
            if ele.start > S and ele.end < F:
                if len(result) == 0:
                    result.append(ele)
                else:
                    if self.isCompatible(ele, result[-1]):
                        result.append(ele)
        return result

    def max_duration(self, activities):
        key_points = []
        for ele in activities:
            key_points.append(ele.start)
            key_points.append(ele.end)
        time_points = list(sorted(dict.fromkeys(key_points)))
        dp = [[0] * len(time_points) for i in range(len(time_points))]

        for i in range(len(time_points)):
            for j in reversed(range(i + 1)):
                start = time_points[j]
                end = time_points[i]
                tmp_a = Activity(start, end)
                if start == end:
                    dp[j][i] = 0
                elif tmp_a in activities:
                    dp[j][i] = end - start
                else:
                    max_len = 0
                    for k in range(j + 1, i):
                        tmp_len = dp[j][k] + dp[k][i]
                        max_len = max_len if tmp_len <= max_len else tmp_len
                    dp[j][i] = max_len
        return dp[0][-1]


def main(*args):
    a1 = Activity(1, 3)
    a2 = Activity(4, 5)
    a3 = Activity(6, 9)
    a4 = Activity(7, 8)
    activities = [a1, a2, a3, a4]
    solution = Solution()
    print(solution.part3(activities))


if __name__ == '__main__':
    main(*sys.argv[1:])
