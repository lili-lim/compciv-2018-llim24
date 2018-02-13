from datastubs import PEOPLE_LIST

def longest_name():
    """
    sort by length of name in descending order
    """
    def foolen(p): # nothing wrong with having a function inside a function
        return len(p['name'])

    return sorted(PEOPLE_LIST, key=foolen, reverse=True)

def youngest():
    """
    sort by age in ascending order
    """
    def get_age(person_list):
        return person_list['age']
    return sorted(PEOPLE_LIST, key = get_age)

def oldest():
    """
    sort by age in descending order
    """
    def get_age(person_list):
        return person_list['age']
    return sorted(PEOPLE_LIST, key = get_age, reverse=True)


def name_reverse_alpha():

    def get_name(person_list):
        return person_list['name']
    return sorted(PEOPLE_LIST, key = get_name, reverse=True)

def country_then_age():
#alphabetize by country, then within same country, sort by age
    def sort_by_country_age(person_list):
        return (person_list['country'], person_list['age'])

    final_list = sorted(PEOPLE_LIST, key = sort_by_country_age)

    return final_list

   
