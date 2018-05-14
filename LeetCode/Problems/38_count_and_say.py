import sys


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        last_cas = "1"
        if n == 1:
            return last_cas
        for i in range(2, n + 1):
            last_cas = self.gen_next_cas(last_cas)
        return last_cas

    def gen_next_cas(self, cas):
        last_num = None
        num_count = 0
        result = ""
        for j in range(len(cas) + 1):
            if j == 0:
                last_num = cas[j]
                num_count = 1
            elif j == len(cas):
                result += str(num_count)
                result += str(last_num)
            else:
                if last_num == cas[j]:
                    num_count += 1
                else:
                    result += str(num_count)
                    result += str(last_num)
                    last_num = cas[j]
                    num_count = 1
        return result


def main(*args):
    solution = Solution()
    result = solution.countAndSay(6)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
