def binarySearch(arr, low, high, key):
    mid = (low + high)//2
    if (key == arr[mid]):
        return mid
    if (key > arr[mid]):
        return binarySearch(arr, (mid+1), high, key)
    if (key < arr[mid]):
        return binarySearch(arr, low, (mid-1), key)
    return 0

arr1 = [3, 4, 5, 6, 7, 8, 9, 10, 11]
key = 10
print("index of ", key, " is ", binarySearch(arr1, 0, len(arr1), 10))
