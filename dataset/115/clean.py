"""
A Hamming number is a positive integer of the form 2^i*3^j*5^k, for some
non-negative integers i, j, and k. They are often referred to as regular numbers.
More info at: https://en.wikipedia.org/wiki/Regular_number.
"""

def hamming(n_element: int) -> list:
    """This function creates an ordered list of n length as requested, and afterwards
    returns the last value of the list. It must be given a positive integer.

    :param n_element: The number of elements on the list
    :return: The nth element of the list"""
    n_element = int(n_element)
    if n_element < 1:
        my_error = ValueError('n_element should be a positive number')
        raise my_error
    hamming_list = [1]
    i, j, k = (0, 0, 0)
    index = 1
    while index < n_element:
        while hamming_list[i] * 2 <= hamming_list[-1]:
            i += 1
        while hamming_list[j] * 3 <= hamming_list[-1]:
            j += 1
        while hamming_list[k] * 5 <= hamming_list[-1]:
            k += 1
        hamming_list.append(min(hamming_list[i] * 2, hamming_list[j] * 3, hamming_list[k] * 5))
        index += 1
    return hamming_list