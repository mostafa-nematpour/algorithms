# complexity :  O(n log n)


def quick_sort(arr):
    if (len(arr) < 2):
        return arr
    else:
        pivotal_item = arr[0]
        smaller_arr = [i for i in arr[1:] if i <= pivotal_item]
        greater_arr = [i for i in arr[1:] if i > pivotal_item]
    return quick_sort(smaller_arr) + [pivotal_item] + quick_sort(greater_arr)


arr = [99, 98, 1, 5, 2, 3, 4, 98, 5, 5, 0, 586, 56, 3, 1, 1, 1, 1, 1, 2, 3, 57]
sorted_arr = quick_sort(arr)

print(sorted_arr)
