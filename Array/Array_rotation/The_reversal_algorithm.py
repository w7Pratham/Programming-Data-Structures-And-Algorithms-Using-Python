"""
Approach: • Reverse the first 'd' elements.
• Reverse the 'N-d' elements.
• Reverse the whole array

arr = {1, 2, 3, 4, 5, 6, 7} d = 2
1. As d is 2 arr becomes {2, 1, 3, 4, 5, 6, 7}.
2. Reversing 'N-d' elements {2, 1, 7, 6, 5, 4, 3}.
3. Reversing the whole array (3, 4, 5, 6, 7, 1, 2}.
"""

def reverseArray(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -=  1

def rotateLeft(arr,d):
    if not d: return
    n = len(arr)
    d = d % n
    reverseArray(arr, 0, d-1)
    reverseArray(arr, d, n-1)
    reverseArray(arr, 0, n-1)
    
arr1 = [1, 2, 3, 4, 5, 6, 7]
d = 2
rotateLeft(arr1,d)

"""
T(n): O(N)
S(n): O(1)
"""
