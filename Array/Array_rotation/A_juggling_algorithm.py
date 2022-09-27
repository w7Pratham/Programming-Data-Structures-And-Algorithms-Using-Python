"""
Approach: ♦ Divide the array into different sets where the number of sets is equal to the GCD of N and d
(say X, so that elements which are X distance apart are part of a set) and rotate the element within sets
by 1 position to the left.
• Calculate the GCD between the length and distance to be moved.
• The element are only shifted within the sets.
• We start with tmp = arr[0] and keep moving arr[i+d] to arr[j] and finally, store tmp at right place.
"""

def rotate(arr, d, n):
    d = d % n
    g_c_d = gcd(d,n)
    for i in range(g_c_d):
        tmp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= n:
                k -= n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = tmp


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5]
    print(rotate(arr1, 2, len(arr1))
    
"""
T(n): O(N)
S(n): O(1)
"""
