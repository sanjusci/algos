
__author__ = "Sanju Sci"
__email__ = "sanju.sci9@gmail.com"


def reverse(array, start=0, end=-1):
    """
    This function is used to reverse a array.
    :param array:
      An array that contains list integer of values.
    :param start:
      A start that contains starting index value.
    :param end:
      An end that contains default -1.
    :return: None
    """
    alen = len(array)
    end = (alen - 1) if end < 0 else end

    while start < end:
        array[start], array[end] = array[end], array[start]
        # print(array)
        start += 1
        end -= 1


if __name__ == '__main__':
    array = [2, 3, 4, 6, 6, 9, 9, 7, 0]
    reverse(array)
