import sys


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapper = dict()
        mapper[2] = "abc"
        mapper[3] = "def"
        mapper[4] = "ghi"
        mapper[5] = "jkl"
        mapper[6] = "mno"
        mapper[7] = "pqrs"
        mapper[8] = "tuv"
        mapper[9] = "wxyz"

        result = []
        for num_str in digits:
            new_result = []
            num = int(num_str)
            if num in mapper:
                map_str = mapper[num]
                if len(result) == 0:
                    for letter in map_str:
                        new_result.append(str(letter))
                else:
                    for letter in map_str:
                        for combi in result:
                            new_result.append(combi + letter)
                result = new_result
        return result

def main(*args):
    solution = Solution()
    result = solution.letterCombinations("23")
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
