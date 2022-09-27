"""
Approach: •At each iteration, shifting the elements to left (i.e. first becomes last),
•after d iterations all elements are shifted by d.
"""

def rotate(arr, d, n):
    while d:
        tmp_last = arr[0]
        for i in range(n-1):
            arr[i] = arr[i+1]
        arr[n-1] = tmp_last
        d--

if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5]
    print(rotate(arr1, 2, len(arr1))

"""
T(n): O(N*d)
S(n): O(1)
"""
