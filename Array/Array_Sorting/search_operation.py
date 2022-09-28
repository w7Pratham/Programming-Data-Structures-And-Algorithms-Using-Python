"""
Search operation in an unsorted array by linear traversal from first element to last element.
"""

def findElement(arr, n, key):
    for i in range(n):
        if (arr[i] == key):
            return i
    return -1

arr1 = [7, 9, 1, 5, 3, 2, 40]
n =  len(arr1)
key = 40

findElement(arr1, n, key)

"""
O(n): O(N)
S(n): O(1)
"""
