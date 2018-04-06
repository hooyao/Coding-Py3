def array_left_rotation(a, n, k):
    t = k % n
    return a[-(n - t):] + a[0:t]


answer = array_left_rotation([1, 2, 3, 4, 5], 5, 4)
print(*answer, sep=' ')
