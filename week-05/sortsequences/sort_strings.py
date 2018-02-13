from datastubs import STRING_LIST


def reverse_alpha():
    """
    return the list of strings sorted in
    reverse alphabetical order.
    """

    return sorted(STRING_LIST, reverse=True)


def alpha_case_insensitive():
    """
    return the list of strings sorted in
    alphabetical order, but without regard to
    capitalization
    """
    def all_caps(string):
        return string.upper()

    return sorted(STRING_LIST, key = all_caps)


def by_longest_length():
    """
    Sort in descending order of length of strings
    """
    desc_length = sorted(STRING_LIST, key = len, reverse = True)
    return desc_length


def filter_and_sort_number_strings():
    """
    Filter the original list for strings that
    contain numbers. Then sort that list of number
    strings but as strings (i.e. alphabetical order)
    """
    new_list = []
    for string in STRING_LIST:
        if string.isdigit():
            new_list.append(string)

    return sorted([str(d) for d in new_list])


def filter_and_sort_number_strings_as_numbers():
    """
    Filter the list for strings that contain numbers
    and then sort that list of strings in *numerical* order
    """

    new_list = []
    for string in STRING_LIST:
        if string.isdigit():
            new_list.append(string)
    strings_as_nums = sorted(new_list, key = int)

    return strings_as_nums
