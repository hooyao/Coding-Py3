def oddNumbers(l, r):
    result = []
    for i in range(l, r + 1):
        if i % 2 == 1:
            result.append(i)
    return result
