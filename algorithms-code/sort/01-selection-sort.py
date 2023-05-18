def find_smallest_index(arr):
    smallest_item = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest_item:
            smallest_item = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    newArr = []
    for i in range(0,len(arr)):
        smallest_index = find_smallest_index(arr)
        newArr.append(arr.pop(smallest_index))
    return newArr


print(selection_sort([3,5,9,6,9,99,44,1,2,2]))
