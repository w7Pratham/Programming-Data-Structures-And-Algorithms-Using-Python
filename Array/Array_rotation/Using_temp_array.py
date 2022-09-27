"""
Approach: •First store the elements from d to n-1 in a temp array.
•later store the d elements from original array into tmp array.
•Copy elements from tmp array into the orginal array.
"""

def rotate(ls, d):
    tmp = []
    tmp.extend(ls[d:] + ls[:d])
    return tmp

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(rotate(arr, 2))

"""
T(n): O(N)
S(n): O(N)
"""
