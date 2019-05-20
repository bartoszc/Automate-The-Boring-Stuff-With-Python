def nth_smallest(arr, pos):
    n = sorted(arr)
    return n[pos-1]


print(nth_smallest([15, 20, 7, 10, 4, 3], 3))


