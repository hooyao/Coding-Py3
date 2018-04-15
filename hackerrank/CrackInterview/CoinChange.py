import sys


class solution:
    def __init__(self, arr):
        self.arr = arr

    def __hash__(self):
        tmp = ''.join(str(e) for e in self.arr)
        return hash(tmp)


def test_append(arr, tmp_dict):
    if tmp_dict not in arr:
        arr.append(tmp_dict)


def make_change(coins, n):
    sorted_coins = sorted(coins)
    dp = [set() for i in range(n + 1)]
    coins_len = len(coins)
    for i in range(1, n + 1):
        for idx, c in enumerate(sorted_coins):
            last_amount = i - c
            if last_amount == 0:
                tmp_solu = [0] * coins_len
                tmp_solu[idx] = 1
                dp[i].add(tuple(tmp_solu))
            elif last_amount > 0:
                if len(dp[last_amount]) > 0:
                    tmp_dict_list = dp[last_amount]
                    tmp_set = set()
                    for ele in tmp_dict_list:
                        tmp_set.add(ele)
                    for ele in tmp_set:
                        tmp_list = list(ele)
                        tmp_list[idx] += 1
                        dp[i].add(tuple(tmp_list))
            else:
                break
    return len(dp[n])


n = 200
coins = [2, 5, 3, 6]
print(make_change(coins, n))
