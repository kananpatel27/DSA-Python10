def move_zeroes(arr):
    j = 0  # position to place next non-zero

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1

    return arr


# User input
arr = list(map(int, input("Enter elements separated by space: ").split()))

result = move_zeroes(arr)
print("Array after moving zeroes:", result)