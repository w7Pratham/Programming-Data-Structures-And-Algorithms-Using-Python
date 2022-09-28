def insertSorted(arr, n, key):
    arr.append(0)
    while arr[n-1] > key:
        print(n)
        arr[n] = arr[n-1]
        n -= 1
    arr[n] = key
    
arr1 = [1,2,3,4,6,7]
insertSorted(arr1, 6, 5)
print(arr1)
