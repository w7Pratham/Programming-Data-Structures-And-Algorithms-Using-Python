"""
T(n): O(N)
S(n): O(log N)
"""
def deleteElement(arr, n, key):
    pos = binarySearch(arr, 0, len(arr), key)
    
    if pos == -1:
        print("No element with value: ", key)
        return n
    
    while pos != n - 1:
        arr[pos] = arr[pos + 1]
        pos += 1
        
    return n-1


def binarySearch(arr, low, high, key):
    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    if arr[mid] > key:
        return binarySearch(arr, low, (mid - 1), key)
    if arr[mid] < key:
        return binarySearch(arr, (mid + 1), high, key)

    return -1


def printArray(arr,n):
    for i in range(n):
        print(arr[i], end=" ")

arr1 = [1,2,3,4,5]
n = len(arr1)

n = deleteElement(arr1,n,2)
printArray(arr1,n)
