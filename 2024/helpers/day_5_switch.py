# coding: utf-8
""" switch """


def switch(arr, i, j):
    """
        switch()
            switch elements at indices i and j
    """
    arr[i], arr[j] = arr[j], arr[i]
    return arr
