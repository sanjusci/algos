
__author__ = "Sanju Sci"
__email__ = "sanju.sci9@gmail.com"


def gcd(a, b):
    if b == 0:
        return a;
    else:
        return gcd(b, a % b)


# util function to print an array */
def print_array(arr):
    for i in range(len(arr)):
        print("% d" % arr[i], end=" ")

