# coding: utf-8
"""
    f*ck docstrings
"""


def my_median(ll: list, index: bool = True):
    """
        median()
            return median and (optionally)
            index of the median element (if any)
    """
    len_ll = len(ll)
    if len_ll % 2 == 1:  # odd number of elements
        median_index = int((len_ll - 1) / 2)
        median_element = ll[median_index]
        if index:
            return (median_index, median_element)
        return median_element
    median_indices = (int(len_ll / 2) - 1, int(len_ll / 2) + 1)
    median_elements = (ll[median_indices[0]], ll[median_indices[1]])
    if index:
        return (median_indices, median_elements)
    return sum(median_elements) / 2


def main():
    """f*ck dis"""
    test_list_even = list(range(11, 21))
    test_list_odd = list(range(11, 20))
    print(my_median(test_list_even, index=True))
    print(my_median(test_list_even, index=False))
    print(my_median(test_list_odd, index=True))
    print(my_median(test_list_odd, index=False))


if __name__ == "__main__":
    main()
