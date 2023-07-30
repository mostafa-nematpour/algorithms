def binary_search(list, target):
    left = 0
    right = len(list) - 1

    while left <= right:
        middle = (left + right) // 2
        guess = list[middle]

        if guess == target:
            return middle
        if guess > target:
            right = middle - 1
        else:
            left = middle + 1

    return None


list = [1, 2, 3, 5, 6, 8, 7, 9] # list must be sorted (asc)
target = 5

answer = binary_search(list, target)

print(f'index of target = {answer}')
