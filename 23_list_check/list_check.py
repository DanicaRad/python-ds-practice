def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    for item in lst:
        if type(item) != list:
            return False

    # return [type(item) == list for item in lst]
    is_list = tuple(type(item) == list for item in lst)
    if is_list.count(False) >= 1:
        return False
    else:
        return True