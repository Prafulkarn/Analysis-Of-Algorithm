arr = [10, 20, 30, 40]
target = 50


def sequential_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


if sequential_search(arr, target) == -1:
    print(f"The {target} is not found")

else:
    print(f"The {target} is found")
print(sequential_search(arr, target))
