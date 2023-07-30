# complexity :  O(n)

def linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index
    return None


arr = [1, 2, 5, 8, 9, 11, 12, 6]
target = 9

print(f'index of target= {linear_search(arr, target)}')
