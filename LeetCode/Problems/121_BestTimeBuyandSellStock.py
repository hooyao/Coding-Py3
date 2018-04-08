import sys


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        lowest_prices = [0] * (len(prices))
        lowest_prices[0] = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < lowest_prices[i - 1]:
                lowest_prices[i] = prices[i]
            else:
                lowest_prices[i] = lowest_prices[i - 1]
        max_profit = 0
        for i in range(len(prices)):
            profit = prices[i] - lowest_prices[i]
            if profit > max_profit:
                max_profit = profit
        return max_profit


def main(*args):
    solution = Solution()
    result = solution.maxProfit([7, 6, 4, 3, 1])
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
