def number_needed(a, b):
    dict_a, dict_b = dict(), dict()
    for ele in a:
        if ele not in dict_a:
            dict_a[ele] = 0
        dict_a[ele] += 1
    for ele in b:
        if ele not in dict_b:
            dict_b[ele] = 0
        dict_b[ele] += 1

    result_dict = dict(dict_a)
    for k, v in dict_b.items():
        if k in result_dict:
            result_dict[k] -= v
        else:
            result_dict[k] = -v
    return sum(abs(v) for k, v in result_dict.items())


print(number_needed('cde', 'abc'))
