
__author__ = "Sanju Sci"
__email__ = "sanju.sci9@gmail.com"

import copy


def deepcopy(arr):

    # Coping arr into array2 using deepcopy
    array2 = copy.deepcopy(arr)

    print("The original element before deepcopy:")
    for i in range(0, len(arr)):
        print(arr[i], end=" ")

    # Now updating element to new array2

    array2[4][0] = 0
    print("\n")
    print("List1 : {}".format(arr))
    print("List2 : {}".format(array2))


if __name__ == '__main__':
    arr = [1, 2, 3, 4, [1, 2, 3], 5, 6]
    deepcopy(arr)

"""
Output:

The original element before deepcopy:
1 2 3 4 [1, 2, 3] 5 6 

List1 : [1, 2, 3, 4, [1, 2, 3], 5, 6]
List2 : [1, 2, 3, 4, [0, 2, 3], 5, 6]
"""
