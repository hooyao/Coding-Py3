def findAllSubset(nums):
    if len(nums) == 0:
        return []
    results = []
    cur_num = nums[0]
    results.append({cur_num})
    rest_set = nums[1:]
    tmp = findAllSubset(rest_set)
    for ele in tmp:
        results.append({cur_num} | ele)
    results = results + tmp
    return results


def findAllSubset_bit(nums):
    length = len(nums)
    L = 1 << length  # 2 ^ len
    result = []
    for i in range(L):
        temp = []
        for j in range(length):
            if (i & (1 << j)) != 0:
                temp.append(nums[j])
        result.append(temp)
    return result


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

result = findAllSubset_bit(a)
print(len(result))
print(result)
