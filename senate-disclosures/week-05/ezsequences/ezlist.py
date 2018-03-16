#################################
# ezsequences/ezlist.py
#
# This skeleton script contains a series of functions that
#  return

ez_list = [0, 1, 2, 3, 4, ['a', 'b', 'c'], 5, ['apples', 'oranges'], 42]



def foo_hello():
    """
    This function should simply return the `type`
     of the `ez_list` object.

    This guarantees that you'll past at least one of
      the tests/assertions in test_ezlist.py
    """
    return type(ez_list)



##################
# Exercises foo_a through foo_e cover basic list access
##################

def foo_a():
    """
    Return the very first member of `ez_list`
    """
    return ez_list[0]

def foo_b():
    """
    Return the sum of the 2nd and 4th members of
      `ezlist`
    """
    b = ez_list[1] + ez_list[3]
    return b

def foo_c():
    """
    Return the very last member of `ez_list`.

    Use a negative index to specify this member
    """
    last_member = ez_list[-1]
    return last_member

def foo_cx():
    """
    Return the type of the object that is the
        second-to-last member of `ez_list`
    """
    penultimate_type = type(ez_list[-2])
    return penultimate_type

def foo_d():
    """
    Return the very last member of the sequence that itself
        is the second-to-last member of `ez_list`
    """
    penultimate = ez_list[-2]
    return penultimate[-1]

def foo_e():
    """
    Calculate and return the length of `ez_list`,  i.e., the
      number of members it contains.
    """
    number_members = len(ez_list)
    return number_members

def foo_f():
    """
    Return the 6th member of `ez_list` as a single,
      semi-colon delimited string

      i.e. the separate values are joined with the
        semi-colon character
    """
    sixth_element = ez_list[5]
    semi_string = ""
    how_many_index = len(sixth_element)
    current_index = 1

    for member in sixth_element:
        semi_string += member
        if current_index != how_many_index:
            semi_string += ';'
        current_index = current_index + 1

    return semi_string
        
def foo_g():
    """
    Return a list that contains the 2nd through 5th
      elements of `ez_list`

      (it should have 4 members total)
    """
    partial_list = []
    n = 1
    while n <= 4:
        partial_list.append(ez_list[n])
        n = n + 1
    return partial_list

def foo_h():
    """
    Return a list that consists of the last
      3 members of `ez_list` in *reverse* order
    """
    last_three = []
    n = -1
    while n >= -3:
        last_three.append(ez_list[n])
        n = n - 1
    return last_three
    

