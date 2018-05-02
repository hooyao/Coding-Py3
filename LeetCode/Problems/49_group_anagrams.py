import sys


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        stats = dict()
        for ele in strs:
            sorted_str = "".join(sorted(ele))
            if sorted_str not in stats:
                stats[sorted_str] =[]
            stats[sorted_str].append(ele)
        results = []
        for k, v in stats.items():
            results.append(v)
        return results

    def groupAnagrams_slow(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        stats = dict()
        for str in strs:
            tmp = self.to_stats(str)
            if tmp not in stats:
                stats[tmp] = []
            stats[tmp].append(str)
        results = []
        for k, v in stats.items():
            results.append(v)
        return results

    def to_stats(self, s):
        tmp = [0] * 127
        for letter in s:
            idx = ord(letter)
            tmp[idx] = tmp[idx] + 1
        result = "".join(str(x) for x in tmp)
        return result


def main(*args):
    solution = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = solution.groupAnagrams(strs)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
