import sys


class Solution(object):
    def changeCoin_rec(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        empty_result = [0] * len(coins)
        if amount == 0:
            return empty_result
        best = [-1] * len(coins)
        for idx, coin in enumerate(coins):
            if amount >= coin:
                tmp = self.changeCoin_rec(amount - coin, coins)
                tmp[idx] += 1
                if sum(best) < 0 or sum(tmp) < sum(best):
                    best = tmp
        return best

    def changeCoin_dp(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        d = [[-1] * (len(coins) + 1) for i in range(amount + 1)]
        d[0] = [0] * (len(coins) + 1)
        for i in range(amount + 1):
            for idx, coin in enumerate(coins):
                if i >= coin:
                    tmp = list(d[i - coin])
                    if tmp[-1] >= 0:  # has solution
                        tmp[idx] += 1
                        tmp[-1] += 1
                        if d[i][-1] < 0 or d[i][-1] > tmp[-1]:
                            d[i] = tmp
        return d[amount]

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        d = [-1] * (amount + 1)
        d[0] = 0
        for i in range(amount + 1):
            for idx, coin in enumerate(coins):
                if i >= coin:
                    tmp = d[i - coin]
                    if tmp >= 0:  # has solution
                        tmp += 1
                        if d[i] < 0 or tmp < d[i]:
                            d[i] = tmp
        return d[amount]


def main(*args):
    coins1 = [1, 5, 10, 25]
    amount1 = 6
    coins2 = [1, 4, 6, 10]
    coins3 = [2]
    coins4 = [461, 307, 4, 97, 352, 446, 479, 243]
    amount4 = 7265
    solution = Solution()
    result = solution.changeCoin_dp(coins4, amount4)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
