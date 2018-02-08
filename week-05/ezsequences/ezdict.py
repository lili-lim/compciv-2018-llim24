
ez_dict = {'birthdate': '1946-06-14', 'party': 'Republican',
           'gender': 'M',
           'identifiers': {
             'twitter': 'realDonaldTrump',
             'fec': 'P80001571',
           },
           'name': {'first': 'Donald', 'last': 'Trump'},
           'birthplace': {'state': 'NY', 'city': 'New York City'},
           'children': ['Donald', 'Ivanka',
                        'Eric', 'Tiffany', 'Barron'],
            'spouse': 'Melania Trump',
            'terms': [{'start_date': '2017-01-20',
                     'end_date': '2021-01-20'}]
           }
ez_dict.keys()


def foo_hello():
    """
    This function should simply return the `type`
     of the `ez_dict` object.

    This guarantees that you'll past at least one of
      the tests/assertions in test_ezdict.py
    """
    return type(ez_dict)


def foo_a():
    """
    Return the value that corresponds to the `'spouse'`
      property/key of ez_dict
    """
    return ez_dict['spouse']


def foo_b():
    """
    Return the "first name" value
    """
    name = ez_dict['name']
    first_name = name['first']
    return first_name

def foo_bx():
    """
    Return the type of the object that
      the `'terms'` attribute points
    """
    terms_attr = ez_dict['terms']
    return type(terms_attr)

def foo_c():
    """
    Return a string that consists of the
        last and first name together, separated by a comma and
        space, e.g. 'Obama, Barack'
    """
    name_list = ez_dict['name']
    last_first_name = name_list['last'] + ", " + name_list['first']
    return last_first_name



def foo_d():
    """
    Return the number of top-level attributes in `ez_dict`
    e.g. `'name'` is a "top-level" attribute,
      but `'first'` and `'last'` are not

    """
    top_level_atts = len(ez_dict)
    return top_level_atts

def foo_e():
    """
    Return the number of children (based on number of names in
     the `'children'` property)
    """
    number_children = len(ez_dict['children'])
    return number_children


def foo_f():
    """
    Return the name of the last child listed in `'children'`
    """
    children = ez_dict['children']
    last_child = children[-1]
    return last_child

def foo_g():
    """
    Return a string that is a comma-delimited list of the
      names of the spouse and the children. The string
      should start with the spouse's name, followed by
      the children's names

    Hint: Think about how you can create a new list by
      adding two separate lists. Do not use the `append()`
      method.
    """
    spouse_list = []
    #have to add it to a list to make it into a list since it returns from the dictionary as a string
    #used the append method in order to make the two separate lists, to add them as requested
    #       i.e. without using the append() method to add them
    spouse_list.append(ez_dict['spouse'])
    child_list = ez_dict['children']
    family_list = []
    family_list = spouse_list + child_list

    family_string = ""
    number_of_fam = len(family_list)
    index = 1
    for member in family_list:
        family_string += member
        if index != number_of_fam:
            family_string += ','
        index = index + 1

    return family_string

def foo_h():
    """
    Print the start date of President Trump's initial term
    """
    term_dates = ez_dict['terms'][0]
    start_term = term_dates['start_date']
    #instructions say to print the start date
    print(start_term)
    #but it only passes test code if also returns the string
    return start_term

def foo_i():
    """
    Return the age that President Trump will be
     at the end of his initial term, i.e.
     the number of full years between his `'birthdate'`
     and the `'end_date'` of his initial term

    Hint: You should be using the third-party `dateutil`
      library for this.
    """

    import dateutil.parser
    from dateutil.relativedelta import relativedelta

    term = ez_dict['terms'][0]
    end_init_term = dateutil.parser.parse(term['end_date'])
    trump_bd = dateutil.parser.parse(ez_dict['birthdate'])
    diff = relativedelta(end_init_term, trump_bd)
    return diff.years
 

def foo_j():
    """
    Return the full URL for the FEC.gov page for
     *candidate* President Trump.

    Example: President Obama's and VP Biden's
      FEC.gov candidacy page URL is:

      http://docquery.fec.gov/cgi-bin/fecimg/?P80003338
    """
    trump_ids = ez_dict['identifiers']
    trump_fec = trump_ids['fec']
    fec_gov_trump = 'http://docquery.fec.gov/cgi-bin/fecimg/?' + trump_fec

    return fec_gov_trump
