
__author__ = "Sanju Sci"
__email__ = "sanju.sci9@gmail.com"

from Arrays import gcd, print_array
from Arrays.reverse import reverse


# Using temp array https://www.geeksforgeeks.org/array-rotation/
# Time complexity : O(n)
# Auxiliary Space : O(d)

def left_rotate_s1(arr, d):
    """
    This function is used to left rotate arr[] of size n by d.
    :param arr:
      An arr that contains a list.
    :param d:
      A d that contains rotation value.
    :return:
    """
    i = 0
    j = 0
    temp = []
    while j < d:
        temp.append(arr[i])
        # arr = arr[:i] + arr[i+1:]
        del arr[i]
        j += 1
    arr.extend(temp)


# A Juggling Algorithm: https://www.geeksforgeeks.org/array-rotation/
# Time complexity : O(n)
# Auxiliary Space : O(1)

def left_rotate_s2(arr, d):
    """
    This function is used to left rotate arr[] of size n by d.
    :param arr:
      An arr that contains a list.
    :param d:
      A d that contains rotation value.
    :return:
    """
    n = len(arr)
    for i in range(d):
        for i in range(n-1):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]


# Time complexity : O(d)
# Auxiliary Space : O(1)
def left_rotate_s3(arr, d):
    """
    This function is used to left rotate arr[] of size n by d.
    :param arr:
      An arr that contains a list.
    :param d:
      A d that contains rotation value.
    :return:
    """
    n = len(arr)
    for i in range(d):
        temp = arr[0]
        del arr[0]
        arr.append(temp)


# A Juggling Algorithm: https://www.geeksforgeeks.org/array-rotation/
# Time complexity : O(n)
# Auxiliary Space : O(1)

def left_rotate_s4(arr, d):
    """
    This function is used to left rotate arr[] of size n by d.
    :param arr:
      An arr that contains a list.
    :param d:
      A d that contains rotation value.
    :return:
    """
    n = len(arr)
    g = gcd(d, n)
    for i in range(g):

        # move i-th values of blocks
        temp = arr[i]
        j = i
        while 1:
            k = j + d
            # print("K >= n : {} >= {}".format(k, n), end="\n")
            if k >= n:
                k = k - n
            # print("K == i : {} == {}".format(k, i), end="\n")
            if k == i:
                break
            # print("i: {}, j: {},  k: {}".format(i, j, k), end="\n")
            arr[j] = arr[k]
            j = k

        arr[j] = temp


# The Reversal Algorithm: https://www.geeksforgeeks.org/program-for-array-rotation-continued-reversal-algorithm/
# Time complexity : O(d)
# Auxiliary Space : O(1)
def left_rotate_s5(arr, d):
    """
    This function is used to left rotate arr[] of size n by d.
    :param arr:
      An arr that contains a list.
    :param d:
      A d that contains rotation value.
    :return:
    """
    n = len(arr)
    reverse(arr, 0, d - 1)
    reverse(arr, d, n - 1)
    reverse(arr, 0, n - 1)

if __name__ == '__main__':
    from copy import deepcopy
    d = 3
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr_copy1 = deepcopy(arr)
    arr_copy2 = deepcopy(arr)
    arr_copy3 = deepcopy(arr)
    arr_copy4 = deepcopy(arr)

    print("\n---- Using S1 ----\n")
    left_rotate_s1(arr, d)
    print_array(arr)

    print("\n---- Using S2 ----\n")
    left_rotate_s2(arr_copy1, d)
    print_array(arr_copy1)

    print("\n---- Using S3 ----\n")
    left_rotate_s3(arr_copy2, d)
    print_array(arr_copy2)

    print("\n---- Using S4 ----\n")
    left_rotate_s4(arr_copy3, d)
    print_array(arr_copy3)

    print("\n---- Using S5 ----\n")
    left_rotate_s5(arr_copy4, d)
    print_array(arr_copy4)

