import heapq

input = [12,
         4,
         5,
         3,
         8,
         7]

n = len(input)
a = []
a_i = 0
for a_i in range(n):
    a_t = input[a_i]
    a.append(a_t)
print(a)

mid = 0
left_max_heap = []
right_min_heap = []
for idx in range(len(a)):
    ele = a[idx]
    if idx == 0:
        mid = ele
        print('{0:.1f}'.format(mid))
    elif idx == 1:
        mid = (a[0] + a[1]) / 2
        heapq.heappush(left_max_heap, -min(a[0], a[1]))
        heapq.heappush(right_min_heap, max(a[0], a[1]))
        print('{0:.1f}'.format(mid))
    elif idx % 2 == 0:  # odd
        if a[idx] > mid:
            heapq.heappush(right_min_heap, a[idx])
            mid = heapq.heappop(right_min_heap)
        else:
            heapq.heappush(left_max_heap, - a[idx])
            mid = - heapq.heappop(left_max_heap)
        print('{0:.1f}'.format(mid))
    else:
        if a[idx] > mid:
            heapq.heappush(left_max_heap, -mid)
            heapq.heappush(right_min_heap, a[idx])
        else:
            heapq.heappush(right_min_heap, mid)
            heapq.heappush(left_max_heap, -a[idx])
        mid = (-left_max_heap[0] + right_min_heap[0]) / 2
        print('{0:.1f}'.format(mid))
