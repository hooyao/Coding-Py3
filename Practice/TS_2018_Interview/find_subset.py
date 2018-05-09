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


a = [1, 2, 3]

result = findAllSubset(a)
print(result)
