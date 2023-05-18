def binary_search(list, item):
    left = 0
    right = len(list) - 1

    while left <= right:
        middle = (left + right) // 2
        guess = list[middle]

        if guess == item:
            return middle
        if guess > item:
            right = middle - 1
        else:
            left = middle + 1

    return None


first_list = [1, 2, 3, 5, 6, 8, 7, 9]

answer = binary_search(first_list, 5)

print(answer)
