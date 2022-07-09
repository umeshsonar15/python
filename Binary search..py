def binary(arr, x, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2

    if x == arr[mid]:
        return mid
    elif x < arr[mid]:
        high = mid - 1
        return binary(arr, x, low, high)
    else:
        low = mid + 1
        return binary(arr, x, low, high)


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

x = int(input("Enter x :"))

print()
res = binary(arr, x, 0, len(arr) - 1)

if res >= 0:
    print(x, "FOUND at index", res)
else:
    print("NOT FOUND")
