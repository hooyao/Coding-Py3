input = [1,
         2,
         3,
         4,
         5,
         6,
         7,
         8,
         9,
         10]

n = len(input)
a = []
a_i = 0
for a_i in range(n):
    a_t = input[a_i]
    a.append(a_t)
print(a)

odd_mid = 0
even_left = 0
even_right = 1
median = []
for idx in range(len(a)):
    ele = a[idx]
    if idx == 0:
        odd_mid = 0
        print('{0:.1f}'.format(a[odd_mid]))
    elif idx == 1:
        even_left = 0
        even_right = 1
        print('{0:.1f}'.format((a[even_left] + a[even_right]) / 2))
    elif idx % 2 == 0:  # odd
        if ele < a[odd_mid]:
            mid_odd = even_left
        elif a[even_left] < ele < a[even_right]:
            mid_odd = [mid_even[0], ele, mid_even[1]]
        else:
            mid_odd = mid_even + [ele]
        print('{0:.1f}'.format(mid_odd[1]))
    else:
